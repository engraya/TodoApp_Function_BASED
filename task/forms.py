from django import forms

from django.forms import ModelForm

from .models import Task



class TodoForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class' : 'form-control', 'placeholder' : 'Add Task'})
    