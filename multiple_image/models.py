from django.db import models
from django.contrib.auth import get_user_model
from .utils import images_directory_path

User = get_user_model()


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)

    def save(self, *args, **kwargs):
        super(Task, self).save(*args, **kwargs)


class TaskImage(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=images_directory_path)
