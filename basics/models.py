from django.db import models
from tinymce import models as tinymce_models
# from home.models import CreationDate


class Category(models.Model):
    
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Article(models.Model):
    category = models.ManyToManyField('Category')
    name = models.CharField(max_length=254)
    summary = models.CharField(max_length=500)
    description = tinymce_models.HTMLField()
    jsconsole_title = models.CharField(max_length=254, default=None, null=True, blank=True)
    jsconsole_permalink = models.URLField(max_length=2000, default=None, null=True, blank=True)
    gist_title = models.CharField(max_length=254, null=True, blank=True)
    gist = models.CharField(max_length=2000, null=True, blank=True)
    codepen_title = models.CharField(max_length=254, null=True, blank=True)
    codepen_data_slug_hash = models.CharField(max_length=254, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    # new_date_added = models.OneToOneField(CreationDate, on_delete=models.SET_NULL,
    #                                       related_name='added_date', null=True)

    def __str__(self):
        return self.name
