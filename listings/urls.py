from django.urls import path
from . import views

app_name = "listings"

urlpatterns = [
    path('', views.home, name="home"),
    path('listings/', views.listing_list, name="listings"),
    path('listings/<int:pk>/detail/', views.listing_detail, name="details"),
    path('listings/<int:pk>/update/', views.listing_update, name="update"),
    path('listings/<int:pk>/delete/', views.listing_delete, name="delete"),
    path('listings/create/', views.listing_create, name="create"),
]