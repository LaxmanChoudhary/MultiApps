from django import forms
from todo.models import *

class TaskForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user')
		super(TaskForm, self).__init__(*args, **kwargs)
		self.fields['task_group'].queryset = TaskGroup.objects.filter(creator=user)

    class Meta:
        model = Task
        fields = ['title', 'text', 'task_group']
    