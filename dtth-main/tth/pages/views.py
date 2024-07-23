from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Flight,Tour, Booking, Customer,Room,Reservation,ContactUs
from .forms import ContactForm
# Create your views here.
def sample1(request):
	return render(request,"base.html")

def aboutus(request):
	return render(request,"aboutus.html")

def search_flights(request):
    if request.method == 'POST':
        origin = request.POST['origin']
        destination = request.POST['destination']
        date = request.POST['date']
        flights = Flight.objects.filter(origin=origin, destination=destination, date=date)
        return render(request, 'search_results.html', {'flights': flights})
    else:
        return render(request, 'search_form.html')

def all_flights(request):
    flights = Flight.objects.all()
    return render(request, 'all_flights.html',{'flights': flights})

def tour_list(request):
    tours = Tour.objects.filter(available=True)
    return render(request, 'tour_list.html', {'tours': tours})

def book_tour(request, tour_id):
    tour = Tour.objects.get(id=tour_id)
    if request.method == 'POST':
        customer_name = request.POST['name']
        customer_email = request.POST['email']
        customer_phone = request.POST['phone']
        booking_date = request.POST['date']
        num_people = request.POST['num_people']
        customer = Customer.objects.create(name=customer_name, email=customer_email, phone=customer_phone)
        booking = Booking.objects.create(tour=tour, customer=customer, date=booking_date, num_people=num_people)
        return HttpResponseRedirect(reverse('booking_confirmation', args=[booking.id]))
    return render(request, 'book_tour.html', {'tour': tour})

def booking_confirmation(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'booking_confirmation.html', {'booking': booking})

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})

def make_reservation(request, room_id):
    room = Room.objects.get(pk=room_id)
    if request.method == 'POST':
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        reservation = Reservation(room=room, start_date=start_date, end_date=end_date)
        reservation.save()
        return render(request, 'reservation_success.html', {'reservation': reservation})
    return render(request, 'make_reservation.html', {'room': room})

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact_us.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')


