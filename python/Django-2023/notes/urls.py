from django.urls import path

from . import views

urlpatterns = [
    path('notes', views.NoteListView.as_view()),
    path('notes/<int:pk>', views.NoteDetailView.as_view()),
]