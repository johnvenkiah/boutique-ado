from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe Webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Handle a generic or unknown/unexpected webhook event"""
        return HttpResponse(
            context=f'Webhook received: {event["type"]}', status=200
        )
