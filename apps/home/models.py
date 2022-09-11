from django.db import models
from django.utils.text import slugify
from django.utils import timezone as time
# Create your models here.

class Review(models.Model):
    """Model definition for Review."""

    # TODO: Define fields here
    image = models.ImageField(default='/testimonials/team.png', upload_to='testimonials/')
    name = models.CharField(default='', max_length=50)
    job_description = models.CharField(default='', max_length=50)
    review = models.TextField()
    published_date = models.DateTimeField(default=time.now)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        """Meta definition for Review."""

        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        """Unicode representation of Review."""
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('home:service_detail', kwargs={'slug': self.slug})

    def save(self):
        if not self.slug:
            self.slug = slugify(self.name + self.job_description)
        return super().save()
