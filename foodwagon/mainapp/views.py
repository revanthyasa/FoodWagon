from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login, authenticate
from .models import R
from . import forms
from django.contrib import sessions
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your views here.
def home(request):
    return render(request,'index.html')

def loginn(request):
    form=forms.LoginForm()
    if request.method == 'POST':
        form=forms.LoginForm()
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html',{'form':form}) 

def signup(request):
    form = forms.UsersForm()
    alert_message = None
    if request.method == 'POST':
        form = forms.UsersForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                validate_email(email)
            except ValidationError:
                alert_message = 'Invalid email address!'
                return render(request, 'signup.html', {'form': form, 'alert_message': alert_message})
            form.save()
            return redirect('login')
    return render(request, 'signup.html', {'form': form, 'alert_message': alert_message})

def restaurants(request):
    res=R.objects.all()
    return render(request,'restaurants.html',{'res':res})

def insert(request):
    form=forms.RestaurantForm()
    if request.method=='POST':
        form=forms.RestaurantForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('restaurants')
        else:
            print(form.errors)
    return render(request,'insert.html',{'form':form})

def edit_item(request, item_id):
    item = R.objects.get(pk=item_id)
    if request.method == 'POST':
        new_price = request.POST.get('new_price')
        item.price = new_price
        item.save()
        return redirect('restaurants')

    return render(request, 'edit.html', {'item': item})

def delete_item(request, item_id):
    item = R.objects.get(id=item_id)
    item.delete()
    return redirect('restaurants')

from django.shortcuts import render, redirect

def restaurant_list(request):
    context = {
        'res': res,
    }
    return render(request, 'restaurant_list.html', context)

def delete_cartitem(request, item_id):
    cart = request.session.get('cart', [])
    updated_cart = [item for item in cart if item.get('id') != item_id]
    request.session['cart'] = updated_cart
    return redirect('cart')  

def cart_item(request, item_id):
    selected_item = get_object_or_404(R, id=item_id)
    item_data = {
        'id': selected_item.id,
        'itemname': selected_item.itemname,
        'price': float(selected_item.price),
    }
    cart = request.session.get('cart', [])
    cart.append(item_data)
    request.session['cart'] = cart
    return redirect('cart')  

def cart(request):
    cart_data = request.session.get('cart', [])
    cart = [R(**item_data) for item_data in cart_data]
    total_cost = sum(item.price for item in cart)
    data = {'cart': cart, 'total_cost': total_cost}
    return render(request, 'cart.html', data)

from .forms import OrderForm

def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():     
            order_placed = True
            request.session['cart'] = []
            return redirect('cart')
    else:
        form = OrderForm()

    return render(request, 'place_order.html', {'form': form})

def login(request):
    form=forms.LoginForm()
    if request.method == 'POST':
        form=forms.LoginForm()
        username = request.POST.get('username')
        password = request.POST.get('password')
        return redirect('home')
    return render(request, 'login.html',{'form':form})  
