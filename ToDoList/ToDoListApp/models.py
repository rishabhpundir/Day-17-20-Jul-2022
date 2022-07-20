from django.db import models

# Create your models here.

class AddTask(models.Model):
    taskTitle = models.CharField(max_length=30)
    taskDesc = models.TextField()
    Time = models.DateTimeField(auto_now_add=True)
    taskImg = models.FileField()

    def __str__(self):
        return self.taskTitle