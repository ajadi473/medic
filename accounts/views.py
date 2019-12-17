from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import accounts_patientmodel 

# Create your views here.
def home(request):
    return render(request, 'index.html')

def signup_doctors(request):
    return render(request, 'signup.html')

def signup_patients(request):
    return render(request, 'addPatients.html')

def AllPatients(request):
    accounts_patients = accounts_patientmodel.objects.all()
    # accounts_patients_names = list()

    # for val in accounts_patients:
    #     accounts_patients_names.append(val.name)

    # response_html = '<br'.join(accounts_patients_names)
    # return HttpResponse(response_html)
    return render(request, 'allPatients.html', {'accounts_get': accounts_patients})

# form submission_ patients
def AddPatients(request):
    if request.method == 'POST':
        print ('howdy')
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

        # accounts_patient = accounts_patientmodel(email=email, name=name,
        #                          password=password, address = address) 

        # accounts_patient.save()
    
    return render(request, 'index.html')


# def signup_2(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})