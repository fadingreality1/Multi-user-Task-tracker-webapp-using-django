from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class TaskForm(forms.Form):
    title = forms.CharField(label="Task")
    due_date = forms.DateField(widget=DateInput)
    