"""medics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf.urls import url

# from accounts import views as accounts_views
# from boards import views as board_views
from accounts import views as views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^signup/doctors/$', views.signup_doctors, name='signup doctors'),
    url(r'^signup/patients/$', views.signup_patients, name='signup patients'),
    url(r'^admin/', admin.site.urls),
    url(r'^add_patients', views.AddPatients, name='add_patients'),
    url(r'^add_doctors', views.AddDoctors, name='add_doctors'),
    url(r'^login_doctors', views.LoginDoctors, name='login_doctors'),
    url(r'^all_patients/', views.AllPatients, name='all_patients'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='addDoctors.html'), name='login'),
    
    # path('admin/', admin.site.urls),
]
