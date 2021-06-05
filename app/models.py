from django.db import models
from django.utils.timezone import datetime
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User


class Contact(models.Model):
    gender = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=150)
    info = models.CharField(max_length=150)
    gender = models.CharField(max_length=150, choices=gender)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    # date_added = models.DateTimeField( auto_now_add=True)
    # date_update = models.DateTimeField(auto_now=True)
    date_added = models.DateTimeField(default=datetime.now)
    date_update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, null=True)

    # creating slug in database by overriding the save method
    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Contact, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})

    # def get_absolute_url(self):
    #     return reverse("detail", kwargs={"id": self.id})

    class Meta:
        ordering = ['-id']
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.name
