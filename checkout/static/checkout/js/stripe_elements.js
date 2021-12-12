/*
Core logic/payment flow for this comes from here:
https://stripe.com/docs/payments/accept-a-payment
CSS from here:
https://stripe.com/docs/stripe-js
I
*/

let stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
let client_secret = $('#id_client_secret').text().slice(1, -1);
let stripe = Stripe(stripe_public_key);
let elements = stripe.elements();
let card = elements.create('card');
card.mount('#card-element');