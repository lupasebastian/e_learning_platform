from django.contrib.auth.models import User
from django.db.models import Model, OneToOneField, ForeignKey, TextField, DO_NOTHING, CASCADE


class UserProfile(Model):
    user = OneToOneField(User, on_delete=CASCADE, related_name='profile_user', default=None, blank=True)
    group_id = ForeignKey('viewer.Group', default=None, blank=True, null=True, on_delete=DO_NOTHING, related_name='user_group')
    bio = TextField(null=True, blank=True, default='Kim jesteś, mój książę?')

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
