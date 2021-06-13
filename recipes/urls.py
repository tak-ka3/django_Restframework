from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListRecipes.as_view()), #日報一覧
    path('<int:pk>/', views.DetailRecipes.as_view()), #1日の詳細
]