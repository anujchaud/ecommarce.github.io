from django.db import models
import datetime
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomerUserManager
# Create your models here.\
CAT_CHOISES=(("Electronics",'Electronics'),("Vegitables",'Vegitables'),("Womens Clothes","Womans Clothes"),('Mens Clothes',"Mens Clothes"),('Taddy',"Taddy"))
CAT_TYPE_CHOISES=(("/Piece",'/Piece'),("/Kg",'/Kg'),("/Packet",'/Packet'))
class User(AbstractBaseUser,PermissionsMixin):
    name=models.CharField(max_length=100)
    email=models.EmailField(_('email address'),unique=True)
    phone=models.CharField(max_length=10)
    status=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_active =models.BooleanField(default=True)
    cuntry = models.CharField(max_length=20, null=True, blank=True)
    state=models.CharField(default= None,max_length=20,null=True, blank=True)
    city=models.CharField(max_length=20,default=None,null=True, blank=True)
    landmark = models.CharField(max_length=30, null=True, default=None, blank=True)
    road = models.CharField(max_length=50, null=True, default=None, blank=True)
    place=models.CharField(max_length=50, blank=True,null=True,default=None)
    pin=models.IntegerField(max_length=6,null=True,default=None, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','phone']
    objects=CustomerUserManager()
class Product(models.Model):
    pname=models.CharField(max_length=250)
    ptitle=models.TextField(max_length=300)
    cat=models.CharField(choices=CAT_CHOISES,max_length=20)
    quantity_type=models.CharField(choices=CAT_TYPE_CHOISES,max_length=20)
    prize=models.BigIntegerField(max_length=5)
    offer=models.IntegerField(max_length=3)
    image=models.ImageField(upload_to="images",max_length=500)
    total=models.IntegerField(max_length=5)
    aval=models.IntegerField(max_length=5)
    def __str__(self):
        return self.pname
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(max_length=5)
    prize=models.IntegerField(max_length=5)
    total_prize=models.FloatField(max_length=10)
    order_data=models.DateField(default=datetime.date.today())
    order_time=models.TimeField(default=datetime.datetime.now())
    status=models.BooleanField(default=False)
    order_address=models.TextField(max_length=100)
    def __str__(self):
        a=str(self.user)+" | "+str(self.product)
        return a


