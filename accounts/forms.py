from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'  # 等于 ['customer, product, date_created, status']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password']
