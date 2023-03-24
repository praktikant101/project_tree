from django.urls import path
from .views import MenuListView, MenuView


urlpatterns = [
    path("", MenuListView.as_view()),
    path("<int:pk>/", MenuView.as_view(), name="menu-detail")
]