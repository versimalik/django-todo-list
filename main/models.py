from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=100)
    due_date = models.DateField()
    status = models.BooleanField(default=False)
    user = models.ForeignKey(
        to = User,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.text