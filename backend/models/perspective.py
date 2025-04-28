from django.db import models

class Perspective(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        app_label = "core"

    def __str__(self):
        return self.name