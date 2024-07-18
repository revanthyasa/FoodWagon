from . import views
from django.urls import path
urlpatterns = [
    path("",views.home,name="home"),
    path("home",views.home,name="home"),
    path("login",views.login,name="login"),
    path("signup",views.signup,name="signup"),
    path("cart",views.cart,name="cart"),
    path("restaurants",views.restaurants,name="restaurants"),
    path("place_order",views.place_order,name="place_order"),
    path("insert",views.insert,name="insert"),
    path('edit_item/<int:item_id>/', views.edit_item, name='edit_item'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
    path('add_to_cart/<int:item_id>', views.cart_item, name='cart_item'),
    path('delete_to_cart/<int:item_id>', views.delete_cartitem, name='delete_cartitem'),
]
