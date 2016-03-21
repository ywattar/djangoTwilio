from django.http import HttpResponse
from django_twilio.decorators import twilio_view
from push_notifications.admin import DeviceAdmin
from twilio import twiml
from push_notifications.models import APNSDevice, GCMDevice
from twilio.twiml import Response

@twilio_view
def gather_digits(request):

    twilio_response = Response()

    with twilio_response.gather(action='/respond/', numDigits=1) as g:
        g.say('Press one to Notify Yaser, or  press two to notify Nazih')
        g.pause(length=1)
        g.say('Press one to notify  Yaser, or press two to notify Nazih')

    return twilio_response

@twilio_view
def handle_response(request):

    device = GCMDevice.objects.get(registration_id='eLO4byN9NXU:APA91bGhB5imqa5xPX3Nj-iGSLqbAHgVD9RQYGehjHXt68wphY-Jsm_oJyk9OGJwsO39zhieN7Cr-iuRxKja8IVbt4wwQ-193ZchLCQ2ICTF1h7K59vFBf_B5QtkHapdDD4_RM_kU4O0')


    digits = request.POST.get('Digits', '')

    twilio_response = Response()

    if digits == '1':
        twilio_response.say('A text message is on its way')
        device.send_message("You've got paged!",content_available=True)



    if digits == '2':
        twilio_response.say('A text message is on its way')
        twilio_response.sms('You got paged!',to='2266068196')

    return twilio_response


@twilio_view
def reply_to_sms_messages(request):
    r = twiml.Response()
    r.message('Thanks for the SMS message!')
    return r

@twilio_view
def delivered_receipt (request):
    print ("Hellllllllllllllooooooooooooo")
    if request.method == 'POST':
        msgId= request.POST["msgId"]
        print ('Message ID'+request.POST.get('msgId'))
        return HttpResponse("Message has delivered!")
    return HttpResponse("not delivered")
