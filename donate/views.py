from django.contrib import messages, auth
from django.shortcuts import render, HttpResponse
from .forms import MakeDonationForm
from django.template.context_processors import csrf
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.conf import settings
import stripe
from .models import Donation

stripe.api_key = settings.STRIPE_SECRET


def show_wanted_donations(request):
    donations = Donation.objects.all()
    return render(request, 'donate.html', {'donations': donations})


# Create your views here.
def all_donations(request):
    if request.method == 'POST':
        print (request.POST)
        form = MakeDonationForm(request.POST)
        if form.is_valid():
            try:
                customer = stripe.Charge.create(
                    amount= 10000,
                    currency="EUR",
                    description="donation",
                    card=form.cleaned_data['stripe_id'],
                )
            except (stripe.error.CardError, e):
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.success(request, "You have successfully paid")
                return redirect(reverse('donate'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            messages.error(request, "We were unable to take a payment with that card!")

    else:
        form = MakeDonationForm()

    return render(request, "donate.html", {"form": form, 'publishable': settings.STRIPE_PUBLISHABLE})


def make_donation(request, amount):
    print(amount)
    return HttpResponse(amount)


