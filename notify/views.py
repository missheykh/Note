from typing import Text
from django.shortcuts import render
from notify.models import UsersNote
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User


@csrf_exempt
def send_note(request,r,c):#create user Then create note
    if request.method == "POST":
        data =json.loads(request.body)
        if "user" not in data or "title" not in data or "text" not in data:
            return JsonResponse({"status": "error", "msg": "Enter username ,title and text:"}, status=403)
        _user=data.get("user","")
        _title= data.get("title", "")
        _text= data.get("text", "")
        b=UsersNote.objects.get(id=r)
        u=b.user
        rec1=User.objects.get(username=u)

        f=UsersNote.objects.get(id=c)
        g=f.user
        rec2=User.objects.get(username=g)
        if not (UsersNote.objects.filter(shared_users__username=_user).exists()):
            user2 = User.objects.create_user(_user, 'test@yahoo.com', 'johnpassword')
        else:
            user2=User.objects.get(username=_user)

        a=UsersNote.objects.create(user=user2,title=_title,text=_text)
        a.shared_users.add(rec1,rec2)

        
        return JsonResponse({"status": "successful", "msg": "Note created successfully."}, status=201)  
    else:
        return JsonResponse({"status": "error", "msg": "method bayad POST bashe"}, status=403)




