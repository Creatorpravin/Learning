from django.shortcuts import render
from django.http import Http404
from django.views.generic import DetailView,ListView
from .models import Notes
# Create your views here.

class NoteListView(ListView): #end point create
    model = Notes
    context_object_name = 'notes'
    template_name = "notes/notes_list.html" #don't need if we follow the proper name for the class

class NoteDetailView(DetailView):
    model = Notes
    context_object_name = 'note' # it default handle the exception
    template_name = "notes/notes_details.html"

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, "notes/notes_list.html", {"notes": all_notes})

# def details(request, pk):
#     try:
#        note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note does't exist")
#     return render(request, "notes/notes_details.html", {"note": note})