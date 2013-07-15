from django.http import HttpResponse
from django.shortcuts import render 
from football.models import Team
from football.models import League
from football.models import Match
from football.models import Result
from django import forms
from django.forms.formsets import formset_factory
import datetime
# index page with all leagues 
def index(request):
    leagues = []    	    	

    for leag in League.objects.all():
	leagues.append({'league':leag, 'team_no':len(leag.teams.all()) })
    context = {'league': leagues} 
    return render(request, 'football/index.html', context)

# league with all list
def league(request, league_id):
     league = League.objects.get(id=league_id)
     teams = league.teams.all()
     context = {'league': league.name, 'teams':teams}
     return render(request, 'football/league.html', context)

# index page for all matches
def match(request):
     matches = Match.objects.all()
     match1 = []
     date = []
     team1 = []
     for each_match in matches:
         result = Result.objects.all()
	 res = "N/A"	
         for each_r in result:
	    if each_r.match.id == each_match.id:
               if each_r.name == 'DRAW':
                   res = "DRAW"
               else:
                   if not  each_r.team_won == 0 :
                        twon = Team.objects.get(id=each_r.team_won)
                        res = twon.name
	 match1.append({'league':each_match.league, 'date':each_match.date, 'teams':each_match.teams.all(), 'match_result':res})
     context = {'match': match1}

     return render(request, 'football/match.html', context)

# index page for all teams
def team(request):
     t = []
     teams = Team.objects.all()
     
     for each_team in teams:
	tname = each_team.name
	league = League.objects.filter(teams=each_team)
	t.append({'name':tname, 'leagues':league})
		 
     context = {'teams': t}

     return render(request, 'football/team.html', context)
	
# form to add new team
class AddTeamForm(forms.Form):
    name = forms.CharField(max_length=200)

# form to add new league
class AddLeagueForm(forms.Form):
    name = forms.CharField(max_length=200)
    OPTIONS = {}

    for x in range(1,32):
	OPTIONS[x] = x
    OPTIONS = tuple(OPTIONS.items())
    teams = forms.MultipleChoiceField(widget=forms.SelectMultiple, choices=OPTIONS)

    class Meta:
        model = Team

class AddMatchForm(forms.Form):
    league = forms.IntegerField()
    OPTIONS = {}

    for x in range(1,32):
	OPTIONS[x] = x
    OPTIONS = tuple(OPTIONS.items())

    teams = forms.MultipleChoiceField(widget=forms.SelectMultiple, choices=OPTIONS)

    class Meta:
        model = Team

class AddResultForm(forms.Form):
    match = forms.IntegerField()
    OPTIONS = {}

    for x in range(1,32):
	OPTIONS[x] = x
    OPTIONS = tuple(OPTIONS.items())
	
    result = forms.IntegerField() 
    

    class Meta:
        model = Team


def add_new_team(request):
    print "add new item"
    context={}
    if request.method == 'POST':
	form = AddTeamForm(request.POST)
	form.is_valid()
	new_name = form.cleaned_data['name']
	team = Team(name=new_name)
	team.save()
	context={'msg':"new Team added, want to add more teams??"}

    return render(request, 'football/add_team.html',context)

def add_team(request):
    return render(request, 'football/add_team.html',)

def add_new_league(request): #  method to add leagues
    context={}

    if request.method == 'POST':
	form = AddLeagueForm(request.POST)
	form.is_valid()
	league = League(name=form.cleaned_data['name'])
	league.save()
	teams = form.cleaned_data.get('teams')

	for team_id in list(teams):
	     team = Team.objects.get(id=int(team_id))
	     league.teams.add(team)
	context={'msg':"new Team added, want to add more teams??"}

    return render(request, 'football/add_league.html',context)

def add_league(request): # form for the league
    context = {'teams': Team.objects.all()}
    return render(request, 'football/add_league.html',context)

def add_new_match(request): # method to add new matches
    context={}

    if request.method == 'POST':
	form = AddMatchForm(request.POST)
	form.is_valid()
	league_id = form.cleaned_data.get('league')
	league1 = League.objects.get(id=league_id)
	match = Match(league=league1,date=datetime.date.today())
	match.save()
	teams = form.cleaned_data.get('teams')

	for team_id in list(teams):
	     team = Team.objects.get(id=int(team_id))
	     match.teams.add(team)
	context={'msg':"new Match Added added, want to add more matches??"}

    return render(request, 'football/add_match.html',context)

def add_match(request):
    context = {'teams': Team.objects.all(), 'leagues':League.objects.all()}
    return render(request, 'football/add_match.html',context)


def add_new_team(request):
    print "add new item"
    context={}
    if request.method == 'POST':
	form = AddTeamForm(request.POST)
	form.is_valid()
	new_name = form.cleaned_data['name']
	team = Team(name=new_name)
	team.save()
	context={'msg':"new Team added, want to add more teams??"}

    return render(request, 'football/add_team.html',context)

def add_team(request):
    return render(request, 'football/add_team.html',)

def add_new_league(request): #  method to add leagues
    context={}

    if request.method == 'POST':
	form = AddLeagueForm(request.POST)
	form.is_valid()
	league = League(name=form.cleaned_data['name'])
	league.save()
	teams = form.cleaned_data.get('teams')

	for team_id in list(teams):
	     team = Team.objects.get(id=int(team_id))
	     league.teams.add(team)
	context={'msg':"new Team added, want to add more teams??"}

    return render(request, 'football/add_league.html',context)

def add_league(request): # form for the league
    context = {'teams': Team.objects.all()}
    return render(request, 'football/add_league.html',context)

def add_new_match(request): # method to add new matches
    context={}

    if request.method == 'POST':
	form = AddMatchForm(request.POST)
	form.is_valid()
	league_id = form.cleaned_data.get('league')
	league1 = League.objects.get(id=league_id)
	match = Match(league=league1,date=datetime.date.today())
	match.save()
	teams = form.cleaned_data.get('teams')

	for team_id in list(teams):
	     team = Team.objects.get(id=int(team_id))
	     match.teams.add(team)
	context={'msg':"new Match Added added, want to add more matches??"}

    return render(request, 'football/add_match.html',context)

def add_match(request):
    context = {'teams': Team.objects.all(), 'leagues':League.objects.all()}
    return render(request, 'football/add_match.html',context)


# form and submit view for match result
def add_new_result(request): # method to add new result
    context={}

    if request.method == 'POST':
	form = AddResultForm(request.POST)
	form.is_valid()
	print form.cleaned_data
	match_id = form.cleaned_data.get('match')
	result1 = form.cleaned_data.get('result')
        match1 = Match.objects.get(id=match_id)
	if result1 == 0:
            res = Result(match=match1, name="DRAW")
        else:
	    res = Result(match=match1, team_won=result1)
        res.save()
	context={'msg':"new Match Added added, want to add more matches??"}

    return render(request, 'football/add_result.html',context)

def add_result(request):
    context = {'teams': Team.objects.all(), 'matches':Match.objects.all()}
    return render(request, 'football/add_result.html',context)
