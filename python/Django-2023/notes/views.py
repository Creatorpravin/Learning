from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView,DetailView,ListView,UpdateView
from django.views.generic.edit import DeleteView

from .forms import NotesForm
from .models import Notes

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm    

class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
     
class NotesListView(ListView): #end point create
    model = Notes
    context_object_name = 'notes'
    template_name = "notes/notes_list.html" # don't need if we follow the proper name for the class

class NotesDetailView(DetailView):
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