from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('associations/', views.associations, name='associations'),
    path('associations/<int:bhv_id>/districts/', views.association_districts, name='association_districts'),
    path('districts/<int:bhv_id>/seasons/', views.district_seasons, name='district_seasons'),
    path('districts/<int:bhv_id>/seasons/<int:start_year>/leagues/',
         views.district_season_leagues, name='district_season_leagues'),
    path('leagues/<int:bhv_id>/teams/', views.league_teams, name='league_teams'),
]