from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email',)
    
    username = forms.CharField(
        label='회원이름',
        widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : '아이디',
        }
        )
    )

    email = forms.EmailField(
        label='이메일',
        widget=forms.EmailInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : '이메일',
        }
        )
    )



class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'password')



class CustomAuthenticationForm(AuthenticationForm):
    class Meta(AuthenticationForm):
        model = get_user_model()
        fields = ('username', 'password',)

    username = forms.CharField(
        label='회원이름',
        widget=forms.TextInput(
        attrs={
            'placeholder' : '아이디',
        }
        )
    )
    

