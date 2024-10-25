from .models import Note
from django.forms import ModelForm, TextInput, Textarea


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ["title", "content"]
        widgets = {"title": TextInput(attrs={
            'class': "form-control",
            'placeholder': "Enter Note Title",
        }),
            "content": Textarea(attrs={
                'class': "form-control",
                'placeholder': "Enter Note Content",
            }),
        }

