from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("category/<str:val>/", views.CategoryView.as_view(), name="category")
]
