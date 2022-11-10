from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.form),
    path('login/',views.login),
    path('home/',views.Home.as_view()),
    path('logout/',views.logout),
    path('cart/',views.cart),
    path('order/<int:pid>/', views.order),
    path('myorder/',views.myorder),
    path('mail/',views.sendMail),
    path('delete_cart/<int:pid>',views.delete_cart),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

