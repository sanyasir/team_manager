from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=200)


class League(models.Model):
    name = models.CharField(max_length=200)
    teams =  models.ManyToManyField(Team) # has many teams
   
    def __unicode__(self):
        return self.name

class Match(models.Model):
    league = models.ForeignKey(League) # has a league
    date = models.DateField()
    teams = models.ManyToManyField(Team) # has many teams
      
    def matches_won(self, team_id):# convinient menthod to return no of matches a team won
	result = Result.objects.filter(team_won=team_id)
	return len(result)

    def matches_draw(self, team_id): # convineient method to return no of matches a team draw
	matches = Match.objects.filter(result=0, team_id=team_id)
	return len(matches)
	
    def matches_loss(self, team_id):
	matches = Match.objects.filter(result=1, teams_draw=team_id)
	return len(matches)

class Result(models.Model): # table which holds results of all the matches
     match = models.ForeignKey(Match)
     team_won = models.IntegerField(default=0)
     team_loss = models.IntegerField(default=0)
     name = models.CharField(max_length=10, default='no result' ) # "won" if one team wins 'draw' if its a draw 

