from mainapp.models import Users
from django import forms
from .models import R
class UsersForm(forms.ModelForm):
    class Meta:
        model=Users
        fields="__all__"

class LoginForm(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(max_length=20)

class RestaurantForm(forms.ModelForm):
    class Meta:
        model=R
        fields="__all__"


class OrderForm(forms.Form):
    full_name = forms.CharField(max_length=100, label='Full Name')
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'custom-email-field'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 30}),label='Address')
    phone_number = forms.CharField(max_length=10, min_length=10, label='Phone Number')
    payment_method = forms.ChoiceField(choices=[('cod', 'Cash on Delivery'), ('online', 'Online Payment')],widget=forms.RadioSelect, label='Payment Method')



