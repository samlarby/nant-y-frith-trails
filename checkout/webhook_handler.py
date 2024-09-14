from django.http import HttpResponse

class StripeWh_handler:
    # handle stripe webhooks

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        # handle a generic/unknown/unexpected webhook event 

        return HttpResponse(
            content=f'Webhook receieved: {event["type"]}',
            status=200)   