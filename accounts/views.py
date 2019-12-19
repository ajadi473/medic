from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import accounts_patientmodel
from .forms import LoginDoctorsForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def signup_doctors(request):
    return render(request, 'addDoctors.html')

def signup_patients(request):
    return render(request, 'addPatients.html')

@login_required
def AllPatients(request):
    accounts_patients = accounts_patientmodel.objects.all()
    return render(request, 'allPatients.html', {'accounts_get': accounts_patients})

# form submission_ patients
def AddPatients(request):
    if request.method == 'POST':
        
        email = request.POST['email']
        name = request.POST['name']
        password = request.POST['password']
        address = request.POST['address']
        dob = request.POST['dob']
        country = request.POST['country']
        disease = request.POST['disease']

        patient = accounts_patientmodel.objects.create(
                    email=email, 
                    name=name,
                    password=password, 
                    address = address,
                    dob = dob,
                    nationality = country,
                    diseased = disease,
                )

        return redirect('/')
    
    return render(request, 'index.html')

# form submission_ patients
def AddDoctors(request):
    if request.method == 'POST':
        
        email = request.POST['email']
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        

        if User.objects.filter(username=username).exists():
            message.info(request, 'Username already exists')
            return redirect('add_doctors')
        else:
            user = User.objects.create_user(
                username=username,
                first_name = first_name,
                last_name = last_name,
                password = password,
                email = email,
            )

            user.save()
            print ('User created')
            return redirect('all_patients/')
  
    
    return render(request, 'index.html')

def LoginDoctors(request):
    # user = User.objects.first() 
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print ('logging in after post...')

        user = auth.authenticate(
            username = username,
            password = password,
        )

        if user is not None:
            auth.login(request, user)
            return redirect('all_patients')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('home')


        return redirect('all_patients')

    else:
        return render(request,'index.html')
