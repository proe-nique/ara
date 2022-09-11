from django.db import models
from django.utils.text import slugify
from django.utils import timezone as time

# Create your models here.
class Service(models.Model):
    """Model definition for Service."""

    # TODO: Define fields here
    
    name = models.CharField(default='', max_length=50)
    about = models.TextField()
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        """Meta definition for Service."""

        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        """Unicode representation of Service."""
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('home:service_detail', kwargs={'slug': self.slug})

    def save(self):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save()

# PRODUCT MODEL
class Product(models.Model):
    """Model definition for Product."""

    # TODO: Define fields here
    
    name = models.CharField(default='', max_length=50)
    weight = models.CharField(max_length=100, default='')
    network = models.CharField(max_length=100, default='')
    loc_tech = models.CharField(max_length=100, default='')
    accuracy_range = models.CharField(max_length=10, default='')
    features = models.ManyToManyField(Service, related_name='products')
    published_date = models.DateTimeField(default=time.now)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        """Unicode representation of Product."""
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('home:product_detail', kwargs={'slug': self.slug})    

    def save(self):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save()
