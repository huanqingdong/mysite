import json, string

import os, base64

from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return render(request, 'hello.html')


def camera(request):
    return render(request, 'camera.html')


def upload(request):
    data = request.POST.get("data")
    tryTimes = request.POST.get("tryTimes")
    tryTimes = int(tryTimes)
    tryTimes = tryTimes + 1
    print(data)
    imgdata = base64.b64decode(data)
    file = open('d://1.jpg', 'wb')
    file.write(imgdata)
    file.close()
    if tryTimes == 100:
        result = {"flag": "success", "tryTimes": tryTimes, "user": "郇庆东"}
    else:
        result = {"flag": "failed", "tryTimes": tryTimes}

    return HttpResponse(json.dumps(result), content_type="application/json")
