from django.db import models


class ToDoList(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    which_day = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
