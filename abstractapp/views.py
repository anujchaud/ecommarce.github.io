from django.shortcuts import render,redirect
from .form_validations import check_name,check_mobile,check_email
from django.core.paginator import Paginator
from django.views import View
from django.contrib import messages
import datetime
from django.contrib.auth import authenticate
from django.contrib.auth import login as loginuser
from django.http import HttpResponse
from .models import User,Product,Order
# Create your views here.
def form(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            sname = request.POST.get("sname")
            email = request.POST.get("email")
            mobile = request.POST.get("mobile")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            if sname and email and mobile and password1 and password2:
                if password1 == password2:
                    if check_mobile(mobile):
                        if check_email(email):
                            if check_name(sname):
                                check_usnique_mail = User.objects.filter(email=email)
                                if not check_usnique_mail:
                                    User.objects.create_user(email, password1, sname, mobile)
                                    messages.error(request, "Accounts has been created!")
                                else:
                                    messages.error(request, "Ragister with another email id!")

                            else:
                                messages.error(request, "name should be alphabatical form!")
                        else:
                            messages.error(request, "enter a vailed Email Id!")
                    else:
                        messages.error(request, "Mobile number should be 10 digit and digit form!")
                else:
                    messages.error(request, "password does not matched!")
            else:
                messages.error(request, "fill required field!")
        return render(request, 'index.html')
    else:
        return redirect("/home")


def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            email = request.POST.get('email')
            password = request.POST.get('pass')
            print(email,password,"<this is user name and password")
            if email and password:
                if check_email(email):
                    authenticated_user = authenticate(email=email, password=password)
                    if authenticated_user:
                        loginuser(request, authenticated_user)
                        return redirect("/home")
                    else:
                        messages.error(request, 'invailed creadientials!')
                else:
                    messages.error(request, "enter a valiled email!")
            else:
                messages.error(request, "fill required all fields!")
        return render(request, 'login.html')
    else:
        return redirect("/home")



class Home(View):
    category_data=Product.objects.filter(cat="/Pies")

    print(category_data,"<--category_data")
    data = Product.objects.all()
    category_data = Product.objects.raw('SELECT * FROM abstractapp_product group by "cat"') ## Its Filter all ctegory from products

    def get(self, request):
        if request.user.is_authenticated:

            """its use for showing data in home page!"""
            cart_item = request.session.get('cart')
            category = request.GET.get('category')
            print(category,"<- this is category ")
            if category:
                category_wise = Product.objects.filter(cat=category)
                for i in self.category_data:
                    print(i.cat)
                return render(request, "home.html",
                              {'cart': cart_item, 'category_data': self.category_data, 'data': category_wise})
            else:
                return render(request, "home.html",
                              {'cart': cart_item, 'category_data': self.category_data, 'data': self.data})
        else:
            return HttpResponse(f'''<center style="color:red"><h1>You'r not authinticated..<br><h4><a href="/login">Login First!''')

    def post(self,request):
        """Its use for handling session!"""
        cart = request.session.get("cart")
        if request.method == "POST":
            product_id = request.POST.get('pid')
            print(product_id, "<--this profuct_id")
            if cart is not None:
                if product_id in cart:
                    product_value = cart[product_id]

                    print(product_value, "<--product value")
                    cart[product_id] = product_value + 1
                    print(cart[product_id], product_id, '<-after update {productvalue:product_id}')
                    print(cart,"<--this is cart")
                else:
                    """if cart dictonary/object hai but item new hai in cart"""
                    print("<--cart hai")
                    cart[product_id] = 1
                    print(cart)
            else:
                print("<--cart nahi hai")
                cart = {}     # if cart me first time value a rahi hai then create cart dictonary
                cart[product_id] = 1      #by default pahli bar 1 quantity insert hogi with product_id

        request.session['cart'] = cart       #initilizing cart object in session which key name "cart"
        print(request,"<---this is request in post method")
        return self.get(request)


def logout(request):
    request.session.clear()
    return redirect('/login')



def cart(request):
    if request.user.is_authenticated:
        error = False
        try:
            data = request.session.get('cart')
            data = (data.keys())
            list(data)
            data = Product.objects.filter(id__in=data).order_by("-id")
            print(data)
        except:
            error=("You Have Not any item in cart!")
        # for i in data:
        #     print(i)
        # print((data))
        return render(request, 'cart.html', {'data': data,"error":error})
    else:
        return HttpResponse(
                    f'''<center style="color:red"><h1>You'r not authinticated..<br><h4><a href="/login">Login First!''')


def order(request, pid):
    if request.user.is_authenticated:
        user_data = User.objects.filter(email=request.user)
        data = Product.objects.filter(id=pid)
        cat_data = Product.objects.filter(cat=data[0].cat)
        cat_data=Paginator(cat_data,2)
        page_number=request.GET.get('page')
        page_obj=cat_data.get_page(page_number)

        print(request.POST.get('update'))
        if request.method == "POST" and request.POST.get("update")=="Update Address":
            cuntry = request.POST.get("cuntry")
            state = request.POST.get("state")
            city = request.POST.get("city")
            landmark = request.POST.get("landmark")
            road = request.POST.get("road")
            place = request.POST.get("place")
            pin = request.POST.get("pin")
            # print(cuntry,state,city,landmark,road,place,pin,"<----address data")
            if User.objects.filter(email=request.user).update(cuntry=cuntry, state=state,city=city,
                                                landmark=landmark,road=road, place=place, pin=pin):
                print('update succrssfuly....')
        elif request.method=="POST" and request.POST.get("confirm")=="Confirm Order":
            ord_address=request.POST.get("order_add")
            print(ord_address,'<--this is order address')
            quantity=request.POST.get('quantity')
            product_obj=Product.objects.get(id=pid)
            print(product_obj,"<---product object")
            date=datetime.date.today()
            try:
                if int(quantity)>=1 and data[0].aval >= int(quantity):
                    try:
                        Product.objects.filter(id=pid).update(aval=data[0].aval - int(quantity))

                        total_prize = int(data[0].prize) * int(quantity)
                        print(total_prize,'<-Total prize')
                        a=Order.objects.create(user=request.user, product=product_obj,
                                                 quantity=quantity, prize=data[0].prize,
                                                 total_prize=total_prize,order_address=ord_address)
                        if a:
                            get_cart_value = request.session.get('cart')
                            try:
                                del(get_cart_value[str(pid)])
                                # print(get_cart_value, "<- before this is order cart")

                                request.session['cart']=get_cart_value
                                # print(get_cart_value,"<-after this is order cart")
                                messages.error(request,'Order successful!')
                            except:
                                messages.error(request, 'Order successful!')
                    except:
                        print("Somthing went wrong during Order!")


                else:
                    messages.error(request, "Product not available as your quantity!")
            except:
                messages.error(request,"Add product quantity as you want to order!")
        return render(request, 'all_order.html', {'data': data,"user_data":user_data,'page_obj':page_obj})
    else:
        return HttpResponse(
                    f'''<center style="color:red"><h1>You'r not authinticated..<br><h4><a href="/login">Login First!''')
def myorder(request):
    if request.user.is_authenticated:
        user=request.user
        try:
            user_order=Order.objects.select_related('product').filter(user=user).order_by('-id')
            print(user_order)
        except Exception as e:
            print(e)
            raise("Something went wrong!")
        return render(request,"myorder.html",{'user_order':user_order})
    else:


        return HttpResponse(
            f'''<center style="color:red"><h1>You'r not authinticated..<br><h4><a href="/login">Login First!''')

def sendMail(request):
    from django.core.mail import EmailMessage
    msg="<h1 style='color:red'>Hello Devlopers!<h1>"
    a=EmailMessage('Mail Testing By Vinay...',msg,"vinaykushwaha587@gmail.com",['surendrakush002@gmail.com','vinaykushwaha588@gmail.com','abhishekvishal8121997@gmail.com'])
    a=a.send()
    if a:
        print("send")
    else:
        print("fail")
    return HttpResponse(msg)
def delete_cart(request,pid):
    if pid is not None:
        cart=request.session.get("cart")
        print(cart,"<before")
        del cart[str(pid)]
        print(cart,"<after")
        request.session['cart']=cart
        print("removed")
        print(cart,"this is cart for remove")
    return redirect('/cart')