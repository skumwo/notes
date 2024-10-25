from django.shortcuts import render, redirect

from .forms import NoteForm
from .models import Note


def index(request):
    notes = Note.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Main Page of site', 'notes': notes})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form is invalid'

    form = NoteForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)


from django.shortcuts import render, get_object_or_404, redirect


def note_info(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('home')  # Redirecting to the homepage after deletion
    return render(request, 'main/note_info.html', {'note': note})



