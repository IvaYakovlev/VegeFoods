from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import EmailField


def validate_email(value):
    if User.objects.filter(email=value).exists():
        raise ValidationError('Email Already Exists')
    return value


class CustomUserCreationForm(UserCreationForm):
    email = EmailField(validators=[validate_email])

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValueError('Email Already Exists')
        return email

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2' ]
        field_classes = {"username": UsernameField}