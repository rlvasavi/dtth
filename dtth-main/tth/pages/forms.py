from django import forms
from .models import Flight,ContactUs

class FlightSearchForm(forms.Form):
    origin = forms.CharField(max_length=50)
    destination = forms.CharField(max_length=50)
    date = forms.DateField()

    def search(self):
        cleaned_data = super().clean()
        flights = Flight.objects.filter(origin=cleaned_data['origin'],
                                        destination=cleaned_data['destination'],
                                        date=cleaned_data['date'])
        return flights


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['email', 'message']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your message'}),
        }