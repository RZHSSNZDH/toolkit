from django.http import HttpResponse
from django.shortcuts import redirect, render, reverse
import random, re
from . import models

def gen_random_link():
    letters = "qwertyuioplkjhgfdsazxcvbnm"
    res = 0
    for i in range(26*26*26*26):
        chars = [random.choice(letters), random.choice(letters), random.choice(letters), random.choice(letters)]
        temp_res = ''.join(chars)
        if not models.link.objects.filter(short=temp_res):
            res = temp_res
            break
    return res

def index(request):
    return render(request, "link/index.html")

def create_short(request):
    short = gen_random_link()
    main = request.POST["main_link"]
    url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
    if not short:
        return HttpResponse("We reached to the limits of short urls that we can make!")
    else:
        if re.match(url_pattern, main):
            L = models.link(short=short, main=main)
            L.save()
            return HttpResponse("127.0.0.1:8000" + reverse("link:index") + str(short))
        else:
            return HttpResponse("Your link is not valid. Maybe you should add http.")

def go_to_main(request, short):
    main = str(models.link.objects.get(short=short))
    return redirect(main)
