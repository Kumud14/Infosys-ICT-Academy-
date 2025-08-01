from django.shortcuts import render, redirect
from main.models import Test
# Create your views here.
from django.shortcuts import render
from .models import Task



def home(request):
    data = Test.objects.all()  # This line runs before new data is saved
 #getting all the data from tablle to django 
    
    if request.method == 'POST':
        var1 = request.POST.get('name')
        var2 = request.POST.get('number')

        # Save to DB
        data1 = Test(name=var1, number=var2)
        data1.save()

    return render(request, 'home.html',{'data':data,})


def about(request):
    if request.method == 'POST':
        task_title = request.POST.get('task')
        if task_title:  
            Task.objects.create(title=task_title)

    tasks = Task.objects.all()
    return render(request, 'about.html', {'tasks': tasks})

def edit(request, id):
    data = Test.objects.get(id=id)
    
    if request.method == 'POST':
        var1 = request.POST.get('name')
        var2 = request.POST.get('number')
        
        data.name = var1
        data.number = var2
        data.save()  # only this save is needed

        return redirect('home')  # make sure this matches your URL name

    return render(request, 'edit.html', {'data': data})

    

def delete(request, id):
    data = Test.objects.get(id=id)
    data.delete()
    return redirect('home')




def login_view(request):
    return render(request, 'login.html')
