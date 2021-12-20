from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=255)
    post_body = RichTextUploadingField(blank=True, null=True)
    created_at = models.DateField(default=timezone.now())
