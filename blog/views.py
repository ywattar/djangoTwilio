from django.shortcuts   import render

def home (request):
    print ("views")
    title="Yaser Alwattar :) %s" % (request.user)
    print(request.user)
    context={
        "title" : title
    }
    return render(request,"home.html",context)