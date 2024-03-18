from django.shortcuts import render
from django.core.mail import send_mail
from website.models import *
from django.conf import settings
# Create your views here.

def data_for_all():
    hotels = Hotel.objects.last()
    contact_info = ContactInfo.objects.last()
    about_us = AboutUs.objects.last()
    header_image = HeaderImage.objects.last()
    
   
    
    context={
             'contact_info':contact_info,
             'about_us':about_us,
             'header_image':header_image,
             'hotels':hotels}
    return context

def index(request):
    hotels = Hotel.objects.last()
    slider_images = SliderImage.objects.all()
    amenities = Amenity.objects.all()
    accommodations = Accommodation.objects.all()
    facilities = Facility.objects.all()
    about_us = AboutUs.objects.last()
    testimonials = Testimonial.objects.all()
    gallery_images = GalleryImage.objects.all()
    contact_info = ContactInfo.objects.last()  # Assuming there's only one contact info object
    hotel_service = HotelService.objects.all()
    
    context = {'hotels': hotels,
        'slider_images': slider_images,
        'amenities': amenities,
        'accommodations': accommodations,
        'facilities': facilities,
        'about_us': about_us,
        'testimonials': testimonials,
        'gallery_images': gallery_images,
        'hotel_service':hotel_service,
        'contact_info': contact_info,}
    return render(request, 'index.html',context )

def accommodation(request):
    
    accommodations = Accommodation.objects.all()
    context = {'accommodations':accommodations}
    context.update(data_for_all())
    
    return render(request,'accommodations.html',context)
def accommodation_details(request,room_id):
    accommodations_details = Accommodation.objects.get(id=room_id)
    context = {'accommodations_details':accommodations_details}
    context.update(data_for_all())
    
    return render(request,'accommodations_detail.html',context)
    
def gallery(request):
    gallery_images = GalleryImage.objects.filter()
    context = {'gallery_images':gallery_images}
    context.update(data_for_all())
    
    return render(request,'gallery.html',context)


def attraction(request):
    attraction = Attraction.objects.filter()
    context = {'attraction':attraction}
    context.update(data_for_all())
    
    return render(request,'attraction.html',context)

def about_us(request):
    about_us = AboutUs.objects.last()
    testimonials = Testimonial.objects.all()
    context = {'about_us':about_us,
               'testimonials':testimonials}
    context.update(data_for_all())
    
    return render(request,'about_us.html',context)

# def contact_us(request):
#     about_us = AboutUs.objects.last()
#     testimonials = Testimonial.objects.all()
#     context = {'about_us':about_us,
#                'testimonials':testimonials}
#     context.update(data_for_all())
    
#     return render(request,'contact_us.html',context)

def contact_us(request): 
    templet_name='contact_us.html'
    context={}
    data=data_for_all()
    context.update(data)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Send email
        send_mail(
            'Contact Form Submission',
            f'Name: {name}\nEmail: {email}\nMessage: {message}',
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )

        # Optionally, you can redirect the user to a success page
        return render(request, 'sucess.html',context)
    return render(request, templet_name,context)
def book(request): 
    
    templet_name='book.html'
    accommodations = Accommodation.objects.all()
    
    context={'accommodations':accommodations}
    data=data_for_all()
    context.update(data)
    if request.method == 'POST':
        # Process the form data here
        arrival_date = request.POST.get('arrival_date')
        departure_date = request.POST.get('departure_date')
        full_name = request.POST.get('fullname')
        phone_number = request.POST.get('phonenumber')
        adult_count = request.POST.get('adult_count')
        room_type = request.POST.get('room_type')
        num_of_rooms = request.POST.get('num_of_rooms')
        send_mail(
            'Contact Form Submission',
            f'Name: {full_name}\nPhone number: {phone_number}\narrival date: {arrival_date}\ndeparture date: {departure_date}\nadult_count: {adult_count}\nroom type: {room_type}\nnum of rooms: {num_of_rooms}',
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )

        # Perform any additional processing or validation as needed

        # Redirect to a success page or do something else
        return render(request, 'sucess.html',context)

    return render(request, templet_name,context)



    
    
    
    

