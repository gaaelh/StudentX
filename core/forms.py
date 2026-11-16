
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StudentRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        help_texts = {
            'username': '',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password1'].help_text = (
            "Use at least 8 characters."
        )

        self.fields['password2'].help_text = ''
