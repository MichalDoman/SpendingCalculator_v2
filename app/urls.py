from django.urls import path
from app.views import HomeView, RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', HomeView.as_view(), name='home'),
]