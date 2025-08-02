from django.urls import path
from .views import newView
urlpatterns=[
    path("",newView.as_view(),name="home")
]