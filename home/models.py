from django.db import models

class AnonMessage(models.Model):
    text = models.TextField(null=False)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:20]}... - {self.time}"
