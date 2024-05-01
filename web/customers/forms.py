from django import forms
from .models import Customers
import re


class CustomerSignUpForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ['first_name', 'last_name', 'email', 'phone', 'password']

    def clean_email(self):
        email = self.cleaned_data['email']
        if Customers.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        return password

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        if not re.match(r'^\+?1?\d{9,15}$', mobile):
            raise forms.ValidationError("Invalid mobile number format.")

        if Customers.objects.filter(profile__mobile=mobile).exists():
            raise forms.ValidationError("This mobile number is already registered.")

        return mobile
    # if in future added the confirm password in registration....
    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get("password")
    #     confirm_password = cleaned_data.get("confirm_password")
    #
    #     if password != confirm_password:
    #         raise forms.ValidationError("Passwords do not match.")
    #
    #     return cleaned_data

