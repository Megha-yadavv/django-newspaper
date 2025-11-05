from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser


class CustomCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'phone_number')

class CustomChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields= ('username', 'email', 'phone_number')
