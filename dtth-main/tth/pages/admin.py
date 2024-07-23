# Register your models here.
from django.contrib import admin
from .models import Flight,Tour,Customer,Booking,Room,Reservation,ContactUs

admin.site.register(Flight)
admin.site.register(Tour)
admin.site.register(Customer)
admin.site.register(Booking)
admin.site.register(ContactUs)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('room', 'start_date', 'end_date')