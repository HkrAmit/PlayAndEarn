from django import forms
from django.utils.translation import gettext_lazy as _
from .models import players

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"input100"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"input100"}))

class UserVerifyForm(forms.Form):
    otp = forms.CharField(max_length=6, widget=forms.TextInput(attrs={"class":"input100"}))

class UserRegForm(forms.ModelForm):
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={"class":"input100"}))
    re_password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={"class":"input100"}))

    class Meta:
        model = players
        fields = ('name', 'pubg_name', 'pubg_id', 'mobile', 'email', 'password', 're_password')

        error_messages = {
            'name': {
                # 'max_length': _("Name is too long."),
                'required': _("Please enter your name."),
            },
            'pubg_name': {
                'invalid': _("Please provide a valid name."),
                'required': _("Please enter your PUBG name."),
            },
            'pubg_id': {
                'invalid': _("Please provide a valid ID."),
                'required': _("Please enter your PUBG ID."),
            },
            'mobile': {
                'invalid': _("Please provide a valid mobile number."),
                # 'unique': _("User already registered."),
                'required': _("Please enter your mobile number."),
            },
            'email': {
                'invalid': _("Please provide a valid email."),
                'required': _("Please enter your email address."),
            },

        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'input100'}),
            'pubg_name': forms.TextInput(attrs={'class': 'input100'}),
            'pubg_id': forms.TextInput(attrs={'class': 'input100'}),
            'mobile': forms.TextInput(attrs={'class': 'input100'}),
            'email': forms.EmailInput(attrs={'class': 'input100'}),
        }

    def clean_mobile(self):
        data = self.cleaned_data['mobile']

        if len(data)==11 and data[:2]=="01":
            return data
        elif len(data)==14 and data[:5]=="+8801":
            return data[-11:]
        else:
            raise forms.ValidationError("Invalid Number.")

    def clean_re_password(self):
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")
        if password and re_password and password != re_password:
            raise forms.ValidationError("Password Not Matched")
        return re_password
