from django.urls import path,include
from .views import sample1,search_flights,all_flights,tour_list,book_tour,booking_confirmation,room_list,make_reservation,aboutus,contact_us,contact_success

urlpatterns=[
path('',sample1,name="NR"),
path('aboutus/',aboutus,name="AU"),
path('search-flights/', search_flights, name='search_flights'),
path('all-flights/', all_flights, name='all_flights'),
path('tour/', tour_list, name='tour_list'),
path('<int:tour_id>/book', book_tour, name='book_tour'),
path('confirmation/<int:booking_id>', booking_confirmation, name='booking_confirmation'),
path('rooms/', room_list, name='room_list'),
path('rooms/<int:room_id>/reserve/', make_reservation, name='make_reservation'),
path('contact/', contact_us, name='contact_us'),
path('contact/success/', contact_success, name='contact_success'),
]