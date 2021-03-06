from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Gebruikersnaam", max_length=100)
    password = forms.CharField(label="Wachtwoord", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    #username = forms.CharField(label="Gebruikersnaam", max_length=100)
    email = forms.EmailField(widget= forms.TextInput(attrs={'placeholder':'Email'}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={'placeholder':'Wachtwoord'}))
