from django.shortcuts import render
from ToDoListApp.models import AddTask

# Create your views here.

def homepage(request):
    context = {'success' : False}
    if request.method == 'POST':
        task_title = request.POST['task_title']
        task_desc = request.POST['task_desc']
        task_img = request.POST['task_img']
        # print(task_title, task_desc)

        insert_task = AddTask(taskTitle=task_title, taskDesc=task_desc, taskImg = task_img)
        insert_task.save()
        context = {'success' : True}

    return render(request, 'Homepage.html', context)

def tasks(request):
    allTasks = AddTask.objects.all()
    context = {'tasks' : allTasks}
    return render(request, 'tasks.html', context)
