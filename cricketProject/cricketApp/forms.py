from django import forms
from cricketApp.models import Match


class MatchForm(forms.ModelForm):
    match_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),label='Match Date')
    class Meta:
        model=Match
        fields=('match_date','location','team1','team2','team1_score','team2_score','match_winner')