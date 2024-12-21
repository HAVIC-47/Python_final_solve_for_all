# python manage.py startapp products

# INSTALLED_APPS = [
#     ...,
#     'products',
# ]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.product_list, name='product_list'),
# ]



# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'


# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     description = models.TextField()
#     image = models.ImageField(upload_to='product_images/')  # Media field

#     def __str__(self):
#         return self.name


# python manage.py makemigrations
# python manage.py migrate


# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
