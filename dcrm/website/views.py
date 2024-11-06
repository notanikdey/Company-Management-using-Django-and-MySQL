from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages 
from .models import Record
from .forms import AddRecordForm



# Create your views here.

def home(request):
    records = Record.objects.all()
    return render(request, 'home.html',{'records':records})

# def login_user(request):
#     pass 

# def logout_user(request):
#     pass

def customer_record(request, pk):
    customer_record = Record.objects.get(id=pk)
    return render(request, 'record.html',{'customer_record':customer_record})

def delete_record(request,pk):
    delete_it = Record.objects.get(id=pk)
    delete_it.delete()
    messages.success(request, "Record Deleted Successfully...")
    return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            add_record = form.save()
            messages.success(request, "Record Added.....")
            return redirect('home')
    return render(request, 'add_record.html',{'form':form})