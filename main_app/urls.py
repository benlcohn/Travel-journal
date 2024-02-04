from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('journals/', views.journals_index, name='journals'),
    path('journals/<int:journal_id>/', views.journals_detail, name='detail'),
    path('journals/create/', views.JournalCreate.as_view(), name='journals_create'),
    path('accounts/signup/', views.signup, name='signup'),
]