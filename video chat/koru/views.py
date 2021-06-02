from django.shortcuts import render

from .models import currentchat









# Create your views here.

def index(request):
    return render(request,"koru/index.html")

def host(request):
    if request.method == "POST":
        if request.POST.get('name') and request.POST.get('uid'):
            post = currentchat()
            post.hostname = request.POST.get('name')
            post.meetingname = request.POST.get('uid')
            post.save()
            #return render(request, "koru/Chatroom with uid ie meeting id in database")
    return render(request, "koru/host.html")



def users(request):
    if request.method == "POST":
        if request.POST.get('name') and request.POST.get('uid'):
            name = request.POST.get('name')    # user's name
            uid = request.POST.get('uid')
            chats = currentchat.objects.values_list("meetingname",flat=True)
            if uid in chats:
                return render(request,"koru/host.html")     #edit
            else:
                return render(request,"koru/nochat.html",{'uid' : uid})
    return render(request,"koru/users.html")

