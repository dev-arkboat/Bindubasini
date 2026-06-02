from django.db import models


class NoticeCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = "Notice Categories"

    def __str__(self):
        return self.name


class Notice(models.Model):
    title = models.CharField(max_length=300)
    category = models.ForeignKey(NoticeCategory, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField(blank=True)
    file = models.FileField(upload_to='notices/', blank=True, null=True, help_text="Upload PDF or document")
    is_important = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    publish_date = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_important', '-publish_date']
        verbose_name_plural = "Notices"

    def __str__(self):
        return self.title
