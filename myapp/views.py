from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from myapp.forms import MyModelForm

def create_model(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = MyModelForm()
    return render(request, 'create_model.html', {'form': form})

def success(request):
    return render(request, 'success.html')


from django.shortcuts import render
from .models import MyModel  # Import your model

 

def my_model(request):
    port_instances = MyModel.objects.all()
    return render(request, 'my_model.html', {'port_instances': port_instances})
