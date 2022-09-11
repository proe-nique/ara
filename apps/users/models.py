
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    """Model definition for Profile."""

    # TODO: Define fields here
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='members/team.png', upload_to='members/')
    role = models.CharField(default='', max_length=50)
    mobile = models.IntegerField(default='+263 000 000 000' )
    whatsapp = models.IntegerField(default='+263 000 000 000')


    slug = models.SlugField(blank=True, unique=True)

    class Meta:
        """Meta definition for Profile."""

        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        """Unicode representation of Profile."""
        return self.user.username

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('users:profile_detail', kwargs={'slug': self.slug})    

    def save(self):
        if not self.slug:
            self.slug = slugify(self.user.username)
        return super().save()

