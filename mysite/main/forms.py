from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class OrderForm(forms.Form):
    name = forms.CharField(label='ФИО', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Зубенко Михаил Михайлович', 'style': 'width: 180px;'}))
    credit_card_number = forms.CharField(label='Номер кредитной карты', max_length=16, widget=forms.TextInput(attrs={'placeholder': '1245 2256 8945 3654'}))
    cvv = forms.CharField(label='CVV', max_length=3, widget=forms.TextInput(attrs={'placeholder': '652'}))
    card_expiry = forms.CharField(label='Срок действия карты', widget=forms.TextInput(attrs={'placeholder': '6/28'}))