from django.urls import path
from . import views
# Here . means from this directory

urlpatterns = [
    path('',views.HomeView.as_view(), name="Home" ),
]