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

def about(request):
    text = f'<h1>Имя: {name} <br /> Фамилия: {surname} <br /> Отчество: {fathername} <br /> Тел: {phone} <br /> email: {email}'
    return HttpResponse(text)
def item(request, number):
    print('Debug... number = ', number)
    for i in items:
        needed_item = i.get("id")
        if needed_item == number:
            print(f'Debug... number is in {i} dictionary')
            dict_index = (items.index(i))
            print('Debug... dict_index = ', dict_index)
            text = f'Товар: {items[dict_index]["name"]} <br /> Количество: {items[dict_index]["quantity"]} <br /> <a href=/items> Назад к списку товаров </a>'
            return HttpResponse(text)

    text = f'Товар с id={number} не найден'
    return HttpResponse(text)

def numeric_list(request):
    no_num_list = []
    num_list = []
    for i in items:
        dict_index = (items.index(i))
        id = items[dict_index]["id"]
        print('Debug... id = ', id)
        print('Debug ... dict_index = ', dict_index)
        text = f'<a href=item/{id}> {items[dict_index]["name"]} , количество: {items[dict_index]["quantity"]}</a>'
        print('Debug... text = ', text)
        no_num_list.append(text)
    print('Debug... no_num_list = ', no_num_list)

    for x, y in enumerate(no_num_list, start=1):
        print('Debug... x:y = ', f'{x}:{y}')
        a = f'{x}:{y}'
        num_list.append(a)
        print('Debug... num_list = ', num_list)
    temp_list = num_list[0:]
    print('Debug... temp_list = ', temp_list)
    final_string = "<br />".join(temp_list)
    print('Debug... final_list = ', final_string)

    return HttpResponse(final_string)


