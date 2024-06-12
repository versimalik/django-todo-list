from django.db import models

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=100)
    due_date = models.DateField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.text