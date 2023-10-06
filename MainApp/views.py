from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

def item1(request, number):
    data = Item.objects.all()
    for i in data:
        obj = Item.objects.get(id=number)
        return render(request, "item.html", {'data': obj})

    text = f'Товар с id={number} не найден'
    return HttpResponse(text)

def items(request):
    data = Item.objects.all()
    print('data = ', data)
    return render(request, "db.html", {'data': data})

