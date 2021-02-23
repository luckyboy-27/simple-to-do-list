from django.shortcuts import render, HttpResponse, redirect
from api.models import Todo

def index(request):
    tasks = Todo.objects.all()
    default_status = False
    if request.method == 'POST':
        if request.POST.get("save"):
            for i in tasks:
                if request.POST.get(str(i.id)) == "clicked":
                    i.completed = True
                else:
                    i.completed = False
                i.save()
        
        elif request.POST.get("delete") == "delete":
            for i in tasks:
                i.delete()

        else:
            new_task = Todo(
                title = request.POST['title'],
                completed = default_status
            )
            new_task.save()

        return redirect('/')

    return render(request, 'index.html', {'tasks': tasks})

def delete(request, pk):
    tasks = Todo.objects.get(id=pk)
    tasks.delete()
    return redirect('/')
    
