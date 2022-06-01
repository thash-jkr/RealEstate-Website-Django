from multiprocessing import context
from django.shortcuts import redirect, render
from .models import Listing
from .forms import ListingForm

# Create your views here.
def home(request):
    return redirect("/listings")

def listing_list(request):
    listings = Listing.objects.all()
    context = {
        "listings": listings
    }
    return render(request, "listings.html", context)

def listing_detail(request, pk):
    listing = Listing.objects.get(id=pk)
    context = {
        "listing": listing
    }
    return render(request, "listing.html", context)

def listing_create(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("/listings")
    context = {
        "form": form
    }
    return render(request, "listing_create.html", context)
