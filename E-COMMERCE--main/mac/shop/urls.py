from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index, name="ShopHome"),
    path('about/',views.about, name="AboutUS"),
    path('contact/',views.contact, name="ContactUs"),
    path('tracker/',views.tracker, name="TrackinStatus"),
    path('search/',views.search, name="Search"),
    path('productview/<int:myid>',views.productview, name="ProductView"),
    path('checkout/',views.checkout, name="CheckOut"),
    # path('handlerequest/',views.handlerequest, name="CheckOut"),
]