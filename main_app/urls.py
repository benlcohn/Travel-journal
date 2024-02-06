from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('journals/', views.journals_index, name='journals'),
    path('journals/<int:journal_id>/', views.journals_detail, name='journals_detail'),
    path('journals/create/', views.JournalCreate.as_view(), name='journals_create'),
    path('journals/<int:journal_id>/add_entry/', views.add_entry, name='add_entry'),
    path('journals/<int:journal_id>/add_comment/', views.add_comment, name='add_comment'),
    path('journals/<int:journal_id>/add_entry/', views.add_entry, name='add_entry'),
    path('journals/<int:journal_id>/edit/', views.journals_edit, name='journals_edit'),
    path('journals/<int:journal_id>/delete/', views.journals_delete, name='journals_delete'),
    path('entries/<int:pk>/', views.EntryDetail.as_view(), name='entry_detail'),
    path('entries/<int:pk>/update/', views.EntryUpdate.as_view(), name='entries_update'),
    path('entries/<int:pk>/delete/', views.EntryDelete.as_view(), name='entries_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]
