from django.http import HttpResponse
from django.shortcuts   import render


def home (request):
    print ("views")
    title="Yaser Alwattar :) %s" % (request.user)
    print(request.user)
    context={
        "title" : title
    }
    return render(request,"home.html",context)

def delivered_receipt (request):
    print ("Hellllllllllllllooooooooooooo")
    if request.method == 'POST':
        from rdflib.plugins.sparql.operators import string
        msgId= string (request.POST['phone_number'])
        print ('Message ID'+msgId)
        return HttpResponse("Message has delivered!")
    return HttpResponse("not delivered")