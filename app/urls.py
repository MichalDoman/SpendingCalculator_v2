from django.urls import path
from app.views import HomeView, CreateListView,  RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', HomeView.as_view(), name='home'),
    path('create-list', CreateListView.as_view(), name='create'),
]