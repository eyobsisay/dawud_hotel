# admin.py
from django.contrib import admin
from .models import Attraction, ContactUs, Hotel,HeaderImage, HotelService, SliderImage, Amenity, Accommodation, Facility, AboutUs, Testimonial, GalleryImage, ContactInfo
from django.utils.html import format_html
from django_summernote.admin import SummernoteModelAdmin
@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number1', 'email', 'website')
    search_fields = ('name', 'address')

@admin.register(SliderImage)
class SliderImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(HotelService)
class HotelServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'icon')
    
@admin.register(Accommodation)
class AccommodationAdmin(SummernoteModelAdmin):
    list_display = ('room_type', 'description', 'price_per_night', 'capacity')
    search_fields = ('room_type', 'description')

@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'content')
    search_fields = ('name', 'position', 'content')

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'description','display_image')
    search_fields = ('title', 'description')
    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return '-'


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('hotel_name', 'address', 'phone_number', 'email')
    search_fields = ('hotel_name', 'address', 'phone_number', 'email')

@admin.register(HeaderImage)
class HeaderImageAdmin(admin.ModelAdmin):
    list_display = ('title' ,)
    
@admin.register(Attraction)
class AttractionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'display_image')
    search_fields = ('title', 'description')

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return '-'  
    
@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'subject', 'is_active']
         

