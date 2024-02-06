from django.urls import path
from app.views import HomeListView, AddItemView, RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', HomeListView.as_view(), name='home'),
    path('add-item/', AddItemView.as_view(), name="add_item"),
]