from django.urls import path
from . import views

urlpatterns = [
    path('first/', views.first, name="first"),
    path('second/', views.second, name="second"),
    path('third/', views.third, name="third"),
    path('firth/', views.firth, name="firth"),
    path('fifth/', views.fifth, name="fifth"),
    path('sixth/', views.sixth, name="sixth"),
    path('seventh/', views.seventh, name="seventh"),
    path('eighth/', views.eighth, name="eighth"),
    path('ninth/', views.ninth, name="ninth"),
    path('tenth/', views.tenth, name="tenth"),
    path('finish/', views.finish, name="finish"),
    
]