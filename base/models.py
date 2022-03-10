from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=250, null=True, blank=True)

    class Meta:
        ordering = ['user', 'body']
        constraints = [
            models.UniqueConstraint(fields=['user', 'body'], name="unique note"),
        ]
        verbose_name = "Note"
        verbose_name_plural = "Notes"
    
    def __str__(self) -> str:
        return self.body[:50]