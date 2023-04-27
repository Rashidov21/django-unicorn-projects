from django_unicorn.components import UnicornView
from django.contrib import messages
from unicornapp.models import Category, TodoList

class AddTodoFormView(UnicornView):
    name = 'Add'
    categories = Category.objects.all()
    
    message = {}

    
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        title, category, content = self.request.POST.get('title'),self.request.POST.get('category'),self.request.POST.get('content')
        # print(self.request.GET.get('title'))
        # print(self.request.GET.get('category'))
        # print(self.request.GET.get('content'))
        if self.request.method == "POST":
            if title and category:
                cat = Category.objects.get(name=category)
                TodoList.objects.create(title=title,category=cat,content=content)
                # self.message_box_state = True
                if not self.message:
                    self.message.update({'tag':'success','message':"Success !"})
                else:
                    self.message = {}  
            else:
                # self.message_box_state = True
                if not self.message:
                    self.message.update({'tag':'error','message':"Error !"})                                
                else:
                    self.message = {}  
  
            
            
    def close_message_box(self):
        self.message = {}
        

