from django.db import models
from django.utils.html import format_html
class Hotel(models.Model):
    name = models.CharField(max_length=255, verbose_name='Hotel Name')
    address = models.TextField(verbose_name='Address')
    phone_number1 = models.CharField(max_length=15, verbose_name='Phone Number 1')
    phone_number2 = models.CharField(max_length=15, verbose_name='Phone Number 2', blank=True, null=True)
    email = models.EmailField(verbose_name='Email')
    website = models.URLField(verbose_name='Website', blank=True, null=True)
    description = models.TextField(verbose_name='Description')
    logo = models.ImageField(upload_to='hotel_logos/', verbose_name='Hotel Logo', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'


class SliderImage(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='slider_images/', verbose_name='Image')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Slider Image'
        verbose_name_plural = 'Slider Images'

class Amenity(models.Model):
    name = models.CharField(max_length=255, verbose_name='Amenity Name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Amenity'
        verbose_name_plural = 'Amenities'


class HotelService(models.Model):
    name = models.CharField(max_length=255, verbose_name='Service Name')
    description = models.TextField(verbose_name='Service Description')
    icon = models.CharField(max_length=50, verbose_name='Service Icon Class', blank=True, null=True)
    image = models.ImageField(upload_to='service_images/', verbose_name='Image')
    

    def __str__(self):
        return self.name
    
            
class Accommodation(models.Model):
    room_type = models.CharField(max_length=255, verbose_name='Room Type')
    description = models.TextField(verbose_name='Description')
    description_detail = models.TextField(null=True,blank=True)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price per Night')
    capacity = models.IntegerField(verbose_name='Capacity')
    amenities = models.ManyToManyField('Amenity', blank=True, verbose_name='Amenities')
    image = models.ImageField(upload_to='accommodation_images/', verbose_name='Image')
    image1 = models.ImageField(upload_to='accommodation_images/', verbose_name='Image' ,null=True,blank=True)
    image2 = models.ImageField(upload_to='accommodation_images/', verbose_name='Image' ,null=True,blank=True)
    image3 = models.ImageField(upload_to='accommodation_images/', verbose_name='Image' ,null=True,blank=True)

    def __str__(self):
        return f"{self.room_type} - {self.price_per_night}"

    class Meta:
        verbose_name = 'Accommodation'
        verbose_name_plural = 'Accommodations'
        
        
class Facility(models.Model):
    name = models.CharField(max_length=255, verbose_name='Facility Name')
    description = models.TextField(verbose_name='Description')
    icon = models.ImageField(upload_to='facility_icons/', verbose_name='Icon')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Facility'
        verbose_name_plural = 'Facilities'
        
class AboutUs(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    image = models.ImageField(upload_to='about_us_images/', verbose_name='Image', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'


class Testimonial(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    position = models.CharField(max_length=255, verbose_name='Position', blank=True, null=True)
    content = models.TextField(verbose_name='Testimonial Content')
    image = models.ImageField(upload_to='testimonial_images/', verbose_name='Image', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'


class GalleryImage(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    description = models.TextField(verbose_name='Description', blank=True, null=True)
    image = models.ImageField(upload_to='gallery_images/', verbose_name='Image')
    
    

    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Gallery Image'
        verbose_name_plural = 'Gallery Images'
        
class ContactInfo(models.Model):
    hotel_name = models.CharField(max_length=255, verbose_name='Hotel Name')
    address = models.TextField(verbose_name='Address')
    phone_number = models.CharField(max_length=15, verbose_name='Phone Number')
    email = models.EmailField(verbose_name='Email')
    facebook = models.URLField(verbose_name='Facebook URL', blank=True, null=True)
    twitter = models.URLField(verbose_name='Twitter URL', blank=True, null=True)
    instagram = models.URLField(verbose_name='Instagram URL', blank=True, null=True)
    linkedin = models.URLField(verbose_name='LinkedIn URL', blank=True, null=True)
    youtube = models.URLField(verbose_name='Youtube URL', blank=True, null=True)
    map_embed_code = models.TextField(verbose_name='Map Embed Code', blank=True, null=True)

    def __str__(self):
        return self.hotel_name

    class Meta:
        verbose_name = 'Contact Information'
        verbose_name_plural = 'Contact Information'  
        

class Attraction(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='attraction_images/', verbose_name='Image')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Attraction'
        verbose_name_plural = 'Attractions'    
        
class ContactUs(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)    
    
class HeaderImage(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    header_image = models.ImageField(upload_to='header_images/', verbose_name='Image')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Header Image'
        verbose_name_plural = 'Header Image'    
            