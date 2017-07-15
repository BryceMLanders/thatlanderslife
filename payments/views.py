from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from payments.forms import MakePaymentForm
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.template.context_processors import csrf
from django.conf import settings
from donate.models import Donation
import stripe

stripe.api_key = settings.STRIPE_SECRET


@login_required(login_url="/accounts/login")
def donate_now(request, id):
    if request.method == 'POST':
        form = MakePaymentForm(request.POST)
        if form.is_valid():
            try:
                donation = get_object_or_404(Donation, pk=id)
                charge = stripe.Charge.create(
                    amount= int(donation.price * 100),
                    currency="EUR",
                    description=donation.name,
                    card=form.cleaned_data['stripe_id'],
                )
            except (stripe.error.CardError, e):
                messages.error(request, "Your card was declined!")

            if charge.paid:
                messages.success(request, "You have successfully paid")
                return redirect(reverse('wanted_donation'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            messages.error(request, "We were unable to take a payment with that card!")

    else:
        form = MakePaymentForm()
        donation = get_object_or_404(Donation, pk=id)

    args = {'form': form, 'publishable': settings.STRIPE_PUBLISHABLE, 'donation': donation}
    args.update(csrf(request))

    return render(request, 'pay.html', args)