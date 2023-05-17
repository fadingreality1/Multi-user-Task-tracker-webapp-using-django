from django import forms
from django.forms import ModelForm
from tasks.models import Tasks

class DateInput(forms.DateInput):
    input_type = 'date'

class TaskForm(ModelForm):
    class Meta:
        model = Tasks
        widgets = {
            'due_date': DateInput(),
        }
        fields = ['title', 'due_date',]

class UpdateForm(forms.Form):
    nt = forms.CharField(max_length=150, label="New Title", widget=forms.Textarea(attrs={'rows':3, 'cols':30}))
    nd = forms.DateField(widget=DateInput)