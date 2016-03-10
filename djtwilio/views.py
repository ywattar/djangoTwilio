from django_twilio.decorators import twilio_view
from twilio import twiml


from twilio.twiml import Response

@twilio_view
def gather_digits(request):

    twilio_response = Response()

    with twilio_response.gather(action='/respond/', numDigits=1) as g:
        g.say('Press one to hear a song, two to receive an SMS')
        g.pause(length=1)
        g.say('Press one to hear a song, two to receive an SMS')

    return twilio_response

@twilio_view
def handle_response(request):

    digits = request.POST.get('Digits', '')

    twilio_response = Response()

    if digits == '1':
        twilio_response.play('http://bit.ly/phaltsw')

    if digits == '2':
        number = request.POST.get('From', '')
        twilio_response.say('A text message is on its way')
        twilio_response.sms('You looking lovely today!', to=number)

    return twilio_response


@twilio_view
def reply_to_sms_messages(request):
    r = twiml.Response()
    r.message('Thanks for the SMS message!')
    return r