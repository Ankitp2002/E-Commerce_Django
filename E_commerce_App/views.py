from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *
# Create your views here.

# ==============================================================================================================================

def Catogeryviews(request):
    cat_data=commenPro_Cat_views(request)
    if request.method == "POST":
        if request.POST['type1'] == "search":
            request.session['search'] = request.POST['searchbutton']
            return redirect('searchurl')
    catogery=Catogerymodel.objects.all()       
    return render(request,'Catogery.html',{'Catogery_key':catogery,'nav_cat':cat_data })

# ==============================================================================================================================

def SubCatogeryviews(request,subCatId):
    cat_data=commenPro_Cat_views(request)
    if request.method == "POST":
        if request.POST['type1'] == "search":
            request.session['search'] = request.POST['searchbutton']
            return redirect('searchurl')
    catogery=sub_catogerymodel.objects.all().filter(Catogery=subCatId)      
    return render(request,'sub_catogery.html',{'subCatogery_key':catogery,'nav_cat':cat_data})

# ==============================================================================================================================

def productviews(request,procatId):
    cat_data=commenPro_Cat_views(request)
    userId = request.session['sessionId']
    product =Productmodel.objects.all().filter(sub_catogery=procatId)
    if request.method=='POST':
        selectedType = request.POST['type1']
        if selectedType == 'detail':
            request.session['proId']= PID
            PID=request.POST['proId']
            # CID = request.POST['cart']
            return redirect('prodetails')
        elif selectedType == 'search':
            request.session['search'] = request.POST['searchbutton']
            return redirect('searchurl')
        elif selectedType == "fev":
            PID=request.POST['proId']
            product_data = Productmodel.objects.get(pk = PID)
            check_prodata = faviourate_model.objects.filter(userId = userId) &  faviourate_model.objects.filter(productID = PID)
            print("test :::::::::::",check_prodata)
           
            if len(check_prodata)>0 :
                return render (request ,'Product.html',{'Product_key':product,'nav_cat':cat_data,"Error":"Already added in your faviourate list"})
            else:
                fav_model = faviourate_model()
                fav_model.userId = userId
                fav_model.productID = PID
                fav_model.pro_name = product_data.Product_name
                fav_model.pro_dec = product_data.Product_dec
                fav_model.pro_img = product_data.img
                fav_model.pro_price = product_data.Product_price
                fav_model.save()
                print("successsfull")
                return redirect ('faviourateurl')
        else:
            PID=request.POST['proId']
            Prodata=Productmodel.objects.get( pk = PID)
            cat_pd = Cartmodel.objects.all().filter(productID = PID) & Cartmodel.objects.filter (userID=userId) & Cartmodel.objects.filter(orderID = 0 )
            if len(cat_pd) == 0  :
                total =Prodata.Product_price * 2 
                proid=Prodata.pk
                name = Prodata.Product_name
                price = Prodata.Product_price
                img = Prodata.img

                cat = Cartmodel()
                cat.userID =userId
                cat.productID = proid
                cat.orderID = 0
                cat.productname =name
                cat.productprice = price
                cat.productimage = img
                cat.save()
                return redirect('Carturl')
            else:
                return redirect('proall')

    return render (request ,'Product.html',{'Product_key':product,'nav_cat':cat_data})

# ==============================================================================================================================

def proallview(request):
    product = Productmodel.objects.all()
    cat_data=commenPro_Cat_views(request)
    if request.method == 'POST':
        details = request.POST['type1']
        if details == "search" :
            request.session['search'] = request.POST['searchbutton']
            return redirect('searchurl')
        elif details ==  "details":
            PID=request.POST['proId']
            userId = request.session['sessionId']
        
            request.session['proId']= PID
            return redirect('prodetails')
        elif details == "fev":
            PID=request.POST['proId']
            print(PID)
            userID =request.session['sessionId']
            product_data = Productmodel.objects.get(pk = PID)
            check_prodata = faviourate_model.objects.filter(userId = userID) &  faviourate_model.objects.filter(productID = PID)
        
            if len(check_prodata) >0 :
                return render (request ,'proall.html',{'Proall_key':product,'nav_cat':cat_data,"Error":"Already added in your faviourate list"})
            else:
                fav_model = faviourate_model()
                fav_model.userId = userID
                fav_model.productID = PID
                fav_model.pro_name = product_data.Product_name
                fav_model.pro_dec = product_data.Product_dec
                fav_model.pro_img = product_data.img
                fav_model.pro_price = product_data.Product_price
                fav_model.save()
                print("successsfull")
                return redirect ('faviourateurl')

        else:
            PID=request.POST['proId']
            userId = request.session['sessionId']
        
            Prodata=Productmodel.objects.get( pk = PID) 
            catproduct_q =  Cartmodel.objects.all().filter(productID = PID)  & Cartmodel.objects.filter (userID=userId) & Cartmodel.objects.filter(orderID = 0 )
            if len(catproduct_q) == 0  :
                total =Prodata.Product_price * 2 
                proid=Prodata.pk
                name = Prodata.Product_name
                price = Prodata.Product_price
                img = Prodata.img

                cat=Cartmodel()
                cat.userID =userId
                cat.productID = proid
                cat.orderID = 0
                cat.productname =name
                cat.productprice = price
                cat.productimage = img
                cat.save()
                return redirect('Carturl')
            else:
                return redirect('proall')
    return render (request ,'proall.html',{'Proall_key':product,'nav_cat':cat_data})

# ==============================================================================================================================

def commenPro_Cat_views(request):
    if request.session.has_key('sessionId') :
        userdect={
            'userId' : request.session['sessionId'],
            'userName' : request.session['sessionName'],
            'userEmail' : request.session['sessionEmail'],
            'userContect' : request.session['sessioncontect'],
            'userpassword' : request.session['sessionPassword'],
            }
    else:
        userdect={}
    catogery=Catogerymodel.objects.all()
    main_array=[]
    for i in catogery:
        sub_cat = sub_catogerymodel.objects.all().filter(Catogery=i.pk)
        subcat_array=[]
        for j in sub_cat:
            proData = Productmodel.objects.all().filter(sub_catogery=j.pk)
            proArray = []
            for k in proData:
                proDict = {"proId":k.pk,"proName":k.Product_name}
                proArray.append(proDict)
            subcat_dict={'subcat_name':j.sub_Catogery_name,'subcat_img':j.sub_Catogery_img,'subcat_id':j.pk,'proArray':proArray}
            subcat_array.append(subcat_dict)
        cat_dict={'cat_id':i.pk,'cat_name':i.Catogery_name,'subcat_data':subcat_array} 
        main_array.append(cat_dict)

    maindict={'userdata':userdect,'catogery_array':main_array}
    return maindict

# ==============================================================================================================================

def prodetails(request):
    PId=request.session['proId']
    Promodel=Productmodel.objects.get(id=PId)
    cat_data=commenPro_Cat_views(request)
    if request.method == "POST":
        request.session['search'] = request.POST['searchbutton']
        return redirect('searchurl')
    return render(request,'pro_details.html',{'Prodetail':Promodel,'nav_cat':cat_data})

# ==============================================================================================================================

def Cartview(request):
    cat_data=commenPro_Cat_views(request)
    user = request.session['sessionId']
    cartdata = Cartmodel.objects.all().filter(userID=user) & Cartmodel.objects.filter(orderID = 0)
    data_pro = []
    Total_product= len(cartdata)
    Total_price=0
    for i in cartdata:
        Total_price+=i.Quantity * i.productprice
        dict_price = {'Product_Quty_price':i.Quantity * i.productprice , 'pro_id' : i.productID}
        data_pro.append(dict_price)
    request.session['total_product_price'] = Total_price

    if request.method=="POST":
        if request.POST['type1']=="search":
            request.session['search'] = request.POST['searchbutton']
            return redirect('searchurl')    

    return render (request ,'MyCart.html',{'tp':Total_product,'ttp':Total_price,'quantity_price_data':data_pro,'prodata':cartdata,'nav_cat':cat_data})

# ==============================================================================================================================

def shipingview(request):
    cat_data=commenPro_Cat_views(request)
    user = request.session['sessionId']
    # ship1 = Cartmodel.objects.all().filter(userID = user)
    Tprice = request.session['total_product_price']
    if request.method == 'POST':
        if request.POST['type1'] == "search":
            request.session['search'] = request.POST['searchbutton']
            return redirect('searchurl')
        else:
            ship =Shipingmodel()
            ship.userId =user
            ship.username = request.POST['name']
            ship.userEmail = request.POST['Email']
            ship.usercontect = request.POST['Contect']
            ship.Address = request.POST['Address']
            ship.Area = request.POST['Area']
            ship.City = request.POST['city']
            ship.Pincode = request.POST['Pincode']
            ship.Payment_Type = request.POST['Payment type']
            ship.save()
            print("test")
            orderId = ship.pk
            cartAllData = Cartmodel.objects.filter(userID = user) &   Cartmodel.objects.filter(orderID = 0)
            for i in cartAllData :
                cat=Cartmodel()
                cat.pk = i.pk
                cat.userID =i.userID
                cat.productID = i.productID
                cat.orderID = orderId
                cat.productname =i.productname
                cat.productprice = i.productprice
                cat.productimage = i.productimage
                cat.save()
            return redirect ('orderlisturl')

    return render (request , 'Shiping.html',{'ttp':Tprice,'nav_cat':cat_data})

# ==============================================================================================================================

def orderlistview(request):
    cat_data=commenPro_Cat_views(request)
    order_id = Shipingmodel.objects.filter(userId = request.session['sessionId'])
    order_data_array=[]
    for i in order_id:
        product_details = Cartmodel.objects.filter(orderID=i.pk)
        product_details_array=[]
        total_price=0
        for j in product_details:
            total_price+=j.productprice 
            product_dict = {'product_name':j.productname}
            product_details_array.append(product_dict)
        address_data = i.Area + i.City + '(' + str(i.Pincode) + ')'
        request.session['order_id'] = i.pk
        order_data_dict={'orderId':i.pk,'name':i.username,'contact':i.usercontect,'email':i.userEmail,'address':address_data,'payment':i.Payment_Type,'product_data':len(product_details_array),'total_price':total_price,'time':i.Date_time}
        order_data_array.append(order_data_dict)
    if request.method == 'POST':
        if request.POST['type1'] == "search":
            request.session['search'] = request.POST['searchbutton']
            return redirect('searchurl')
        else:
            id = request.POST['o_id']
            request.session['order_id_details'] = id
            return redirect('orderdetailurl')   
    return render(request,'OrderList.html',{'nav_cat':cat_data,'order_session':order_data_array})

# ==============================================================================================================================

def orderdetaisview(request):
    cat_data=commenPro_Cat_views(request)
    if request.method == "POST":
        if request.POST['type1']=="search":
            request.session['search'] = request.POST['searchbutton']
            return redirect('searchurl')
    else:
        pro_data = request.session['order_id_details']
        cat_pro_data = Cartmodel.objects.filter(orderID = pro_data)
        ship_order_data = Shipingmodel.objects.get(pk = pro_data)
        pro_data_array=[]
        address = ship_order_data.Address + ship_order_data.Area + ship_order_data.City + str(ship_order_data.Pincode)
        user_dict={'order_id':ship_order_data.pk,'name':ship_order_data.username,'contact':ship_order_data.usercontect,'email':ship_order_data.userEmail,'address':address,'payment_type':ship_order_data.Payment_Type , 'time':ship_order_data.Date_time}
        total_price = 0
        for i in cat_pro_data:
            total_price+=i.Quantity * i.productprice
            dict_pro_data={'pro_name':i.productname,'pro_price':i.productprice,'Product_Quty_price':i.Quantity * i.productprice ,'pro_image':i.productimage}
            pro_data_array.append(dict_pro_data)
        return render(request,'orders_details.html',{'nav_cat':cat_data,'product_data':pro_data_array,"NO_product" : len(pro_data_array) , 'user_data' : user_dict,'total_price':total_price})

# =========================================================================================================================================================

def searchview(request):
    cat_data=commenPro_Cat_views(request)
    value = request.session['search']
    print(value)
    if request.method == "POST":
        if request.POST['type1'] == "search":
            request.session['search'] = request.POST['searchbutton']
            return redirect('searchurl')
    if value !="":
        main=[]
        search_quary = Productmodel.objects.filter(Product_name__contains= value)    
        for i in search_quary:
            data = {'name':i.Product_name , 'price' :i.Product_price , 'img' : i.img}
            main.append(data)
        if main == []:
            return render ( request , 'serch.html', {'nav_cat':cat_data,"Error":"NO data found"})
        else:
            return render( request , 'serch.html', {"serch_data" : main,'nav_cat':cat_data})
    else:
        return render ( request , 'serch.html', {'nav_cat':cat_data,"Error":"NO data found"})

# =========================================================================================================================================================

def faviouratview(request):
    cat_data = commenPro_Cat_views(request)
    product_data = faviourate_model.objects.filter(userId = request.session['sessionId']) & faviourate_model.objects.all() 
    if request.method=='POST':
        selectedType = request.POST['type1']
        if selectedType == 'detail':
            PID=request.POST['proId']
            request.session['proId']= PID

            return redirect('prodetails')
        elif selectedType == 'search':
            request.session['search'] = request.POST['searchbutton']
            return redirect('searchurl')
        else:

            userId = request.session['sessionId']
            PID=request.POST['proId']
            
            Prodata=Productmodel.objects.get( pk = PID)
            cat_pd = Cartmodel.objects.all().filter(productID = PID) & Cartmodel.objects.filter (userID=userId) & Cartmodel.objects.filter(orderID = 0 )

            if len(cat_pd) == 0  :
                total =Prodata.Product_price * 2 
                proid=Prodata.pk
                name = Prodata.Product_name
                price = Prodata.Product_price
                img = Prodata.img

                cat = Cartmodel()
                cat.userID =userId
                cat.productID = proid
                cat.orderID = 0
                cat.productname =name
                cat.productprice = price
                cat.productimage = img
                cat.save()
                return redirect('Carturl')
            else:
                return render(request,'faviourate_list.html',{'nav_cat':cat_data,"fav_data":product_data,"Error":"Already added in cart"})

    return render (request,'faviourate_list.html',{'nav_cat':cat_data,"fav_data":product_data})

@csrf_exempt
def cartjsview(request):
    x=request.body.decode('utf-8')
    body = json.loads(x)
    proId = body['productId']
    proprice = body['productPrice']
    proqty = body['qty']
    type = body['type']

    if type == "Add" :
        Prodata=Productmodel.objects.get( pk = proId)
        cartCheck = Cartmodel.objects.all().filter(userID=request.session['sessionId']) & Cartmodel.objects.all().filter(orderID = 0) & Cartmodel.objects.all().filter(productID = proId)
        print(cartCheck)
        if len(cartCheck)>0:
            print("Product Already Added in Cart")
        else:
            cartModel = Cartmodel()
            cartModel.userID = request.session['sessionId']
            cartModel.orderID = 0
            cartModel.productID = proId
            cartModel.Quantity = proqty
            cartModel.productprice = proprice
            cartModel.productimage = Prodata.img
            cartModel.productname = Prodata.Product_name
            # cartModel.= int(qty) * proPrice
            cartModel.save()
            print("Add To Cart Successfully")

    return render (request,'faviourate_list.html')