from django.urls import path
from app.views import HomeView, CreateListView,  RegisterView, ListListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', HomeView.as_view(), name='home'),
    path('lists/', ListListView.as_view(), name='lists'),
    path('create-list/', CreateListView.as_view(), name='create'),
]

