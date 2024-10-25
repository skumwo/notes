from django.db import models


class Note(models.Model):
    title = models.CharField('Name', max_length=100)
    content = models.TextField('Content')
    created_at = models.DateTimeField('Date', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Things-to-do'
        verbose_name_plural = 'Notes'
