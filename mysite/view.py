import json, string

import base64
import matplotlib

from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return render(request, 'hello.html')


def camera(request):
    return render(request, 'camera.html')


def plot(request):
    return render(request, 'plot.html')


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


def get_plot(request):
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from io import BytesIO

    y = [3, 10, 7, 5, 3, 4.5, 6, 8.1]
    N = len(y)
    x = range(N)
    width = 1 / 1.5
    plt.bar(x, y, width, color="blue")
    sio = BytesIO()

    plt.savefig(sio, format='png')
    plt.xticks(rotation=70)
    image_tag = base64.encodebytes(sio.getvalue()).decode()
    # image_tag = '<img src="data:image/png;base64,%s"/>' % base64.encodebytes(sio.getvalue()).decode()
    result = {"flag": "failed", "image_tag": image_tag}
    return HttpResponse(json.dumps(result), content_type="application/json")
