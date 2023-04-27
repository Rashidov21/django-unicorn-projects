from django_unicorn.components import UnicornView
from django.shortcuts import redirect
from unicornapp.models import Category, TodoList

class TodoListView(UnicornView):
    # component_name = "todo_list"   
    # template_name = 'index.html'
    # add_form = True
    todos = TodoList.objects.all()
    
    def __init__(self, *args,**kwargs):
        super().__init__(**kwargs)

    def todo_done(self,todo_id):
        todo = TodoList.objects.get(pk=int(todo_id))
        todo.done = True 
        todo.save()
        return redirect('/')