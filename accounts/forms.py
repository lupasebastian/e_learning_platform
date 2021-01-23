from django.contrib.auth.forms import UserCreationForm
from django.db.transaction import atomic

from .models import UserProfile


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'last_name', 'email']

    @atomic
    def save(self, commit=True):
        self.instance.is_active = False
        result = super().save(commit)
        user_profile = UserProfile(user=result)
        if commit:
            user_profile.save()
        return result
