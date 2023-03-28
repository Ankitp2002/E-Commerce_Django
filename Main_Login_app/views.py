from django.shortcuts import  render , redirect
from .models import *
from E_commerce_App.views import *

# Create your views here.
def Registrationview(request):
    cat_data=commenPro_Cat_views(request)
    if request.method == 'POST':
        username=request.POST['name']
        usernumber=request.POST['number']
        useremail=request.POST['email']
        userpass=request.POST['pas']
        userre_pass=request.POST['re_pas']
        user_img = request.FILES.get('image')
        if userpass == userre_pass:
            CheckEmail=Registermodal.objects.all().filter(Email=useremail)
            Checknumber=Registermodal.objects.all().filter(Mo_No=usernumber)
            if len(CheckEmail)>0 and len(Checknumber)>0:
                return render (request,'Registration.html' , {"Error":"number and email both already exiset  "})
            elif len(Checknumber)>0:
                return render (request,'Registration.html' , {"Error":"number already exiset "})
            elif len(CheckEmail)>0 :
                return render (request,'Registration.html' , {"Error":"email  already exiset "})
            else:
                registerModal=Registermodal()
                registerModal.Name=username
                registerModal.Mo_No=usernumber
                registerModal.Email=useremail
                registerModal.Password=userpass
                registerModal.image = user_img
                registerModal.save()
                return redirect('Login')
        else :
            return render (request,'Registration.html' , {"Error":"password dose'nt match"})
    return render (request , 'Registration.html',{'nav_cat':cat_data})

def Loginview(request):
    if request.method == "POST":
        useremail=request.POST['Loginemail']
        userpass=request.POST['pass']
        if userpass != "" and useremail != "":
            register_data=Registermodal.objects.all().filter(Email=useremail) 
            password_user =Registermodal.objects.all().filter(Password=userpass)
            if len(register_data)>0 and len(password_user)>0:
                request.session['sessionId']=register_data[0].pk
                request.session['sessionName']=register_data[0].Name
                request.session['sessionEmail']=register_data[0].Email
                request.session['sessioncontect']=register_data[0].Mo_No
                request.session['sessionPassword']=register_data[0].Password
                # request.session['sessionImage']=register_data[0].image
                return redirect('Catogery')
        else:
            return render(request,'Login.html',{"Error":"Please enter Email/password"})
    return render(request,'Login.html')

def Logoutview(request):
    request.session.clear()
    return redirect ('Login')

def profileview(request):
    cat_data=commenPro_Cat_views(request)
    if request.method == "POST":
        if request.POST['type1'] == "search":
            request.session['search'] == request.POST['searchbutton']
            return redirect('searchurl')
    else:
        img = Registermodal.objects.get(Name= request.session['sessionName'])
        return render(request,'profile.html',{'nav_cat':cat_data,'img':img.image})

def aboutview(request):
    cat_data=commenPro_Cat_views(request)
    if request.method == "POST":
        if request.POST['type1']=="search":
            request.session['search'] = request.POST['searchbutton']
            return redirect('searchurl')
    return render(request,'about.html',{'nav_cat':cat_data})
