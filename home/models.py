from django.db import models

class AnonMessage(models.Model):
    message = models.TextField(null=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{str(self.room)} - {self.sender}"