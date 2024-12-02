from django.db import models

class AnonMessage(models.Model):
    text = models.TextField(null=False)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:20]}... - {self.time}"

    @classmethod
    def get_last_messages(cls, count=10, reverse=False):
        """
        Fetch the last `count` messages with optional reversal.

        :param count: Number of messages to fetch.
        :param reverse: If True, return messages in ascending order (oldest to newest).
                        If False, return messages in descending order (newest to oldest).
        """
        queryset = cls.objects.order_by('-time')[:count]
        return queryset[::-1] if reverse else queryset
    
class TestMedia(models.Model):
   file = models.FileField()