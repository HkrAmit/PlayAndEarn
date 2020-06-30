from django import forms
from django.utils.translation import gettext_lazy as _

class MatchRegFormDirect(forms.Form):
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={"class":"input100"}))
    re_password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={"class":"input100"}))

    def clean_re_password(self):
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")
        if password and re_password and password != re_password:
            raise forms.ValidationError("Password Not Matched")
        return re_password

class MatchRegFormBkash(forms.Form):
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={"class":"input100"}))
    re_password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={"class":"input100"}))
    txnid = forms.CharField(widget=forms.TextInput(attrs={"class":"input100"}))

    def clean_re_password(self):
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")
        if password and re_password and password != re_password:
            raise forms.ValidationError("Password Not Matched")
        return re_password