from django.shortcuts import render
from django.http import HttpResponse

name = 'Иван'
surname = 'Иванов'
fathername = 'Петрович'
phone = '8-923-600-01-02'
email = 'vasya@mail.ru'

items = [
{"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
{"id": 2, "name": "Куртка кожаная" ,"quantity":2},
{"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
{"id": 7, "name": "Картофель фри" ,"quantity":0},
{"id": 8, "name": "Кепка" ,"quantity":124},
]

def home(request):
    text = """<h1>"Learning django"</h1>
    <strong>Автор</strong>: <i>Иванов И.П.</i>
    """
    return HttpResponse(text)

def item1(request, number):
    for i in items:
        needed_item = i.get("id")
        if needed_item == number:
            dict_index = (items.index(i))
            data = items[dict_index]
            return render(request, "item.html", context=data)

    text = f'Товар с id={number} не найден'
    return HttpResponse(text)

def numeric_list(request):
    item_list = items
    print('data = ', item_list)
    data = {"data": item_list}
    return render(request, "items.html", {'data': data})

def index(request):
    return render(request, 'index.html')


