from django.http import HttpResponse
from django.shortcuts import redirect, render
import random
from . import models

def gen_random_link():
    letters = "qwertyuioplkjhgfdsazxcvbnm"
    for i in range(26*26*10*10):
        chars = [str(random.randint(0,9)), str(random.randint(0,9)), random.choice(letters), random.choice(letters)]
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
    main = request.POST["main_link"]
    L = models.link(short=short, main=main)
    L.save()
    print(short, main)
