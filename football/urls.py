from django.conf.urls import patterns, url

from football import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add_team/$', views.add_team, name='add_team'),
    url(r'^add_new_team/$', views.add_new_team, name='add_new_team'),
    url(r'^add_league/$', views.add_league, name='add_league'),
    url(r'^add_new_league/$', views.add_new_league, name='add_new_league'),
    url(r'^add_match/$', views.add_match, name='add_match'),
    url(r'^add_new_match/$', views.add_new_match, name='add_new_match'),
    url(r'^add_result/$', views.add_result, name='add_result'),
    url(r'^add_new_result/$', views.add_new_result, name='add_new_result'),
    url(r'^league/(?P<league_id>\d+)/$', views.league, name='league'),
    url(r'^match/$', views.match, name='match'),
    url(r'^team/$', views.team, name='team'),
)
