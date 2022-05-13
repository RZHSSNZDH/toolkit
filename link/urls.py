from django.urls import path
from . import views

app_name = "link"
urlpatterns=[
    path('', views.index, name="index"),
    path('create/', views.create_short, name="create")
]
