from django import forms


class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'id': 'inputEmail', 'class': "form-control", 'placeholder': "Email address"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'inputPassword', 'class': "form-control",
                                                                 'placeholder': "Password"}))
    username = forms.CharField(widget=forms.Textarea)
