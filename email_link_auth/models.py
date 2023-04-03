from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.timezone import now
import uuid

class EmailVerification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    email = models.EmailField(unique=False)
    token = models.CharField(max_length=36, default=uuid.uuid4, editable=False, unique=False)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.email} | {self.token}"

    class Meta:
        # db_table = 'email verification db'
        ordering = ['-created_at']
        verbose_name = 'Link Email Verification'
