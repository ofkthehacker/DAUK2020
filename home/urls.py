from django.urls import path
from home import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('argali/', views.argali),
    path('argali-documentation/', views.argali_documentation)
]