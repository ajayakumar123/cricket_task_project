from django.shortcuts import render
from cricketApp.models import Team,Player,Match
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from cricketApp.forms import MatchForm

# Create your views here.


def team_list_view(request):

    print("teams list view")
    team_list=Team.objects.all()
    return render(request, 'cricket/team_list.html', context={'team_list':team_list})


def team_detail_view(request,id):
    print("team detail view")
    team_obj = Team.objects.get(id=id)
    player_list=team_obj.players.all()
    print(player_list,type(player_list))
    return render(request, 'cricket/team_detail.html', 
                  context={'team_obj': team_obj,'player_list':player_list})


def player_detail_view(request,id):
    print("player detail view")
    player_obj = Player.objects.get(id=id)
    return render(request, 'cricket/player_detail.html', context={'player_obj': player_obj})

def match_list_view(request):

    print("match list view")
    match_list=Match.objects.all()
    return render(request, 'cricket/match_list.html', context={'match_list':match_list})


class MatchListView(ListView):
    model=Match
    template_name='cricket/match_list.html'
    context_object_name='match_list'


class MatchCreateView(CreateView):
    model=Match
    form_class = MatchForm
    template_name = 'cricket/match_create.html'
    # fields = ('match_date','location','team1','team2','team1_score','team2_score','match_winner')



class MatchUpdateView(UpdateView):
    model=Match
    form_class = MatchForm
    template_name = 'cricket/match_create.html'



class MatchDeleteView(DeleteView):
    model=Match
    template_name = 'cricket/match_delete.html'
    success_url = reverse_lazy('match_list')



def point_list_view(request):

    print("points list view")
    team_list=Team.objects.all()
    return render(request, 'cricket/points.html', context={'team_list':team_list})