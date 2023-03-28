from django.shortcuts import render
from Main_Login_app.models import Registermodal
from E_commerce_App.views import commenPro_Cat_views 
# Create your views here.
def socialview(request):
    comman = comman_profiledata(request)
    return render(request,'Social_Home.html',{'profile' : comman})
def profile_view(request):
    cat_data= commenPro_Cat_views(request)
    comman = comman_profiledata(request)
    userID = request.session['sessionId']
    profile_user_login = Registermodal.objects.get(pk =userID)
    return render(request ,'profile_social.html',{'profile' : comman ,'profile_user' :profile_user_login})
def comman_profiledata(request):
    userID = request.session['sessionId']
    profile_user_login = Registermodal.objects.get(pk =userID)
    main = []
    profile_data = Registermodal.objects.all().exclude(pk =userID)
    profile_all_array=[]
    for i in profile_data:
        dict_profile_all = {'Name':i.Name ,'Contact':i.Mo_No ,'Email':i.Email,'img':i.image}
        profile_all_array.append(dict_profile_all)
    dict_profile ={ 'profile_all':profile_all_array,'profile_user' :profile_user_login}
    main.append(dict_profile)
    print(main)
    return main