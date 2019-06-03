import json

import os, base64

from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return render(request, 'hello.html')


def upload(request):
    data = request.POST.get("data")
    print(data)
    imgdata = base64.b64decode(data)
    file = open('d://1.jpg', 'wb')
    file.write(imgdata)
    file.close()

    result = {"flag": "success"}
    return HttpResponse(json.dumps(result), content_type="application/json")
