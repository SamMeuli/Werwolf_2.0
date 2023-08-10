from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('create-game', views.new_game, name='new_game'),
    path('join-game', views.join_game, name='join_game'),
    path('lobby/<int:pk>/', views.lobby, name='lobby'),

]
