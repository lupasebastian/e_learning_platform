from django.contrib.auth.models import User
from django.db.models import CharField, EmailField, DateTimeField, OneToOneField, \
    ForeignKey, DO_NOTHING, CASCADE, Model


class UserProfile(Model):
    user = OneToOneField(User, on_delete=CASCADE, related_name='profile_user')
    role = ForeignKey('viewer.Role', default=None, on_delete=DO_NOTHING, related_name='user_role')
    group_id = ForeignKey('viewer.Group', default=None, on_delete=DO_NOTHING, related_name='user_group')

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
