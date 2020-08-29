from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.urls import reverse
import pytz
utc=pytz.UTC

# Create your models here.


class Team(models.Model):

    name=models.CharField(max_length=30)
    logo_uri=models.ImageField(max_length=255,upload_to='team_logo/')
    club_state=models.CharField(max_length=30)
    matches_played = models.IntegerField(default=0)
    matches_won = models.IntegerField(default=0)
    matches_lost = models.IntegerField(default=0)
    team_points = models.IntegerField(default=0)

    class Meta:
        ordering = ['-team_points']

    def __str__(self):
        return self.name


class Player(models.Model):

    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    profile_picture=models.ImageField(max_length=255,upload_to='profiles/')
    jersey_number=models.IntegerField()
    country=models.CharField(max_length=30)
    team=models.ForeignKey(Team,related_name='players', related_query_name='players',on_delete=models.CASCADE)
    no_of_matches=models.IntegerField('No of Matches Played')
    runs=models.IntegerField()
    highest_score=models.IntegerField()
    fifties=models.IntegerField()
    hundreds=models.IntegerField()
    strike_rate=models.FloatField()

    @property
    def full_name(self):
        "Returns the player's full name."
        return '%s %s' % (self.first_name, self.last_name)

    def __str__(self):
        "Returns the string representation of player object"
        return self.full_name


class Match(models.Model):
    MATCH_CHOICES=(('team1','Team1'),('team2','Team2'))
    match_date=models.DateTimeField()
    location=models.CharField(max_length=30)
    team1=models.ForeignKey(Team,related_name='matches1', related_query_name='matches1',on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='matches2', related_query_name='matches2', on_delete=models.CASCADE)
    team1_score=models.IntegerField(blank=True,null=True)
    team2_score=models.IntegerField(blank=True,null=True)
    match_winner = models.CharField('Winner of the match',choices=MATCH_CHOICES,max_length=15,blank=True,null=True)

    class Meta:
        ordering = ['-match_date']

    @property
    def match_name(self):
        "Returns the match's full name."
        return '%s-%s' % (self.team1, self.team2)

    def get_absolute_url(self):
        return reverse('match_list')

    def __str__(self):
        "Returns the string representation of match object"
        return self.match_name

    @property
    def match_status(self):
        "Returns the match status is it completed or upcoming"
        today = datetime.now()
        print("match date", self.match_date, self.team1, self.team2)
        today = utc.localize(today)
        res=True
        if self.match_date > today:
            res=False
        return res

    def match_winner_team(self):
        ''' Returns the winner match team'''
        if self.match_winner:
            if self.match_winner == 'team1':
                return self.team1
            else:
                return self.team2
        else:
            return False

    def clean(self):
        '''helpful to validate weather match date is grater than today or mot
        and differentiate team1 whenever selecting'''
        today=datetime.now()
        print("match date",self.match_date,self.team1,self.team2)
        today=utc.localize(today)
        print("today is:", today)
        if self.team1 == self.team2:
            raise ValidationError('team1 and team2 must be different')

        if self.match_date > today:
            if self.team1_score or self.team2_score or self.match_winner:
                raise ValidationError(' " we can not add team1 score,team2 score and match winner for upcoming matches')

        else:
            if not (self.team1_score and self.team2_score and self.match_winner):
                raise ValidationError(' " we must add team1 score,team2 score and match winner for completed matches')


    def save(self, *args, **kwargs):
        '''it will update Team table based on match results'''
        print("1111111111",self, *args, **kwargs)
        print("222222222",self.match_winner,self.team1,self.team2)
        print("222222222",self.id)
        if self.id is None:
            if self.match_winner and self.team1 and self.team2:
                team1_obj = Team.objects.get(id=self.team1.id)
                team2_obj = Team.objects.get(id=self.team2.id)
                team1_obj.matches_played = team1_obj.matches_played + 1
                team2_obj.matches_played = team2_obj.matches_played + 1

                if self.match_winner=='team1':
                    team1_obj.matches_won=team1_obj.matches_won+1
                    team1_obj.team_points = team1_obj.team_points + 2
                else:
                    team2_obj.matches_won = team2_obj.matches_won + 1
                    team2_obj.team_points = team2_obj.team_points + 2

                team1_obj.matches_lost = team1_obj.matches_played - team1_obj.matches_won
                team2_obj.matches_lost = team2_obj.matches_played - team2_obj.matches_won
                team1_obj.save()
                team2_obj.save()
        else:
            orig_obj=Match.objects.get(id=self.id)
            if orig_obj.match_winner != self.match_winner:
                if orig_obj.match_winner is None:
                    if self.match_winner and self.team1 and self.team2:
                        team1_obj = Team.objects.get(id=self.team1.id)
                        team2_obj = Team.objects.get(id=self.team2.id)
                        team1_obj.matches_played = team1_obj.matches_played + 1
                        team2_obj.matches_played = team2_obj.matches_played + 1

                        if self.match_winner == 'team1':
                            team1_obj.matches_won = team1_obj.matches_won + 1
                            team1_obj.team_points = team1_obj.team_points + 2
                        else:
                            team2_obj.matches_won = team2_obj.matches_won + 1
                            team2_obj.team_points = team2_obj.team_points + 2

                        team1_obj.matches_lost = team1_obj.matches_played - team1_obj.matches_won
                        team2_obj.matches_lost = team2_obj.matches_played - team2_obj.matches_won
                        team1_obj.save()
                        team2_obj.save()

                else:
                    if self.match_winner and self.team1 and self.team2:
                        team1_obj = Team.objects.get(id=self.team1.id)
                        team2_obj = Team.objects.get(id=self.team2.id)
                        if self.match_winner == 'team1':
                            team1_obj.matches_won = team1_obj.matches_won + 1
                            team1_obj.team_points = team1_obj.team_points + 2
                            team2_obj.matches_won = team2_obj.matches_won - 1
                            team2_obj.team_points = team2_obj.team_points - 2
                        else:
                            team2_obj.matches_won = team2_obj.matches_won + 1
                            team2_obj.team_points = team2_obj.team_points + 2
                            team1_obj.matches_won = team1_obj.matches_won - 1
                            team1_obj.team_points = team1_obj.team_points - 2

                        team1_obj.matches_lost = team1_obj.matches_played - team1_obj.matches_won
                        team2_obj.matches_lost = team2_obj.matches_played - team2_obj.matches_won
                        team1_obj.save()
                        team2_obj.save()


        super(Match, self).save(*args, **kwargs)



@receiver(pre_delete, sender=Match)
def handle_deleted_match(**kwargs):
    match_obj = kwargs['instance']
    if match_obj.match_winner and match_obj.team1 and match_obj.team2:
        team1_obj = Team.objects.get(id=match_obj.team1.id)
        team2_obj = Team.objects.get(id=match_obj.team2.id)
        team1_obj.matches_played = team1_obj.matches_played-1
        team2_obj.matches_played = team2_obj.matches_played-1
        print("reciver function")
        if match_obj.match_winner == 'team1':
            team1_obj.matches_won = team1_obj.matches_won - 1
            team1_obj.team_points = team1_obj.team_points - 2
        else:
            team2_obj.matches_won = team2_obj.matches_won - 1
            team2_obj.team_points = team2_obj.team_points - 2

        team1_obj.matches_lost = team1_obj.matches_played - team1_obj.matches_won
        team2_obj.matches_lost = team2_obj.matches_played - team2_obj.matches_won
        team1_obj.save()
        team2_obj.save()





