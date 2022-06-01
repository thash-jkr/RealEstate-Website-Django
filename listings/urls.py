from django.urls import path
from . import views

app_name = "listings"

urlpatterns = [
    path('', views.home, name="home"),
    path('listings/', views.listing_list, name="listings"),
    path('listings/<int:pk>/detail/', views.listing_detail, name="details"),
    path('listings/create/', views.listing_create, name="create"),
]