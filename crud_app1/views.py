from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User


# Create your views here.

def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pwd = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pwd)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'addandshow.html', {'fm': fm, 'stud': stud})


# This function will Update/Edit.
def update_data(request, id):
    if request.method == 'POST':
        sp = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=sp)
        if fm.is_valid():
            fm.save()
    else:
        sp = User.objects.get(pk=id)
        fm = StudentRegistration(instance=sp)
    return render(request, 'updatestudent.html', {'fm': fm})


#  This function will delete Data.
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
