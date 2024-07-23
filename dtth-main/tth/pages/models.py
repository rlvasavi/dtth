from django.db import models

class Flight(models.Model):
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    date = models.DateField()
    airline = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.airline} {self.origin} to {self.destination} on {self.date}"

class Tour(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Booking(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    num_people = models.IntegerField()

    def __str__(self):
        return f"{self.customer} - {self.tour} ({self.date})"

class Room(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Reservation for {self.room} from {self.start_date} to {self.end_date}"

class ContactUs(models.Model):
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email