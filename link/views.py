from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
import random
from . import models

def gen_random_link():
    letters = "qwertyuioplkjhgfdsazxcvbnm"
    for i in range(26*26*26*26):
        chars = [random.choice(letters), random.choice(letters), random.choice(letters), random.choice(letters)]
        temp_res = ''.join(chars)
        if not models.link.objects.filter(short=temp_res):
            res = temp_res
            break
    try: # TODO: Repair try/except part
        return res
    except:
        print("We reach the limit of links!")

def index(request):
    return render(request, "link/index.html")

def create_short(request):
    short = gen_random_link()
    print(short)
    main = request.POST["main_link"] # TODO: Add https if there is no
    L = models.link(short=short, main=main)
    L.save()
    return HttpResponse("127.0.0.1:8000/link/" + str(short))

def go_to_main(request, short):
    main = str(models.link.objects.get(short=short))
    return redirect(main)
