from django.db import models

class Record(models.Model):
    """
    A generic Record model — customise fields to match your use case.
    Each Record is stored as a row in the MySQL `myapp_record` table.
    """
    name        = models.CharField(max_length=200)
    email       = models.EmailField(max_length=254, unique=True)
    category    = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} ({self.email})'
