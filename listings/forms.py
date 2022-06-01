from django.forms import ModelForm
from .models import Listing

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = [
            "title",
            "price",
            "bedroom",
            "bathroom",
            "square_feet",
            "address",
            "image",
        ]