from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MemberProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    status = models.CharField(max_length=100)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username