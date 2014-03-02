#FILE app urls roster/urls.py
from django.conf.urls import patterns, url

from roster import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='roster_home'),
    url(r'^best/$', views.bestList, name='roster_best_list'),
    url(r'^athlete/$', views.athleteList, name='roster_athlete_list'),
    url(r'^best/(?P<pk>\d+)$', views.best, name='roster_best'),
    url(r'^athlete/(?P<pk>\d+)$', views.athlete, name='roster_athlete'),
    #url(r'^$', views.map, name='roster_map')
    )