from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('',views.Landing,name='landing'),
    path('assosrecherche/',views.landingRecherche,name='landingRecherche'),
    path('profile/',UserEdit.as_view(),name='profile'),
    path('<int:pk>/profil/',ShowProfilePersonne.as_view(),name='ShowProfilePersonne'),
    path('annonce/',views.annonce,name='annonce'),
    path('login/',views.Loginin,name='login'),
    path('signup/',views.Register,name='signup'),
    path('logout/',views.Logoutt,name='logout'),
    path('createuser/',views.RegisterUser,name='createuser'),
    path('select/',views.Select,name='select'),
    path('cagniote/',views.ListCagniote,name='cagniote'),
    path('delete_annonce/<str:myid>/',delete_annonce,name='delete_annonce'),
    path('delete_comment/<str:myid>/',delete_comment,name='delete_comment'),
    path('signaler_annonce/<str:myid>/',signaler_annonce,name='signaler_annonce'),
    path('signaler_user/<str:myid>/',signaler_user,name='signaler_user'),
    path('administrateur/',views.Admin,name='administrateur'),
    path('arreter/<str:myid>/',Arreter,name='arreter'),
    path('control/',views.Control,name='control'),
    path('list_association/',views.List_Association,name='list_association'),
    path('valider/<str:myid>/',Valider,name='valider'),
    path('deleteAssociation/<str:myid>/',deleteAssociation,name='deleteAssociation'),
    path('deleteuser/<str:myid>/',deleteUser,name='deleteuser'),
    path('deleteAnnonce/<str:myid>/',deleteAnnonce,name='deleteAnnonce'),
    path('add_comment/<str:myid>/',views.add_comment,name='add_comment'),
    path('updateAnnonce/<int:pk>/',views.updateAnnonce , name="updateAnnonce"),
    path('password/',PasswordChange.as_view()),
    path('password_success/',views.password_success,name="password_success"),
    path('<int:pk>/depotArgent/',depotArgent.as_view(),name="depotArgent"),
    path('benevole/',views.ListeBenevole,name='benevole'),
    path('<int:pk>/profilBenevole/',ShowProfileBenevole.as_view(),name='ShowProfileBenevole'),
]