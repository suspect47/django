from django.shortcuts import render
from django.http import HttpResponse

name = 'Иван'
surname = 'Иванов'
fathername = 'Петрович'
phone = '8-923-600-01-02'
email = 'vasya@mail.ru'

def home(request):
    text = """<h1>"Learning django"</h1>
    <strong>Автор</strong>: <i>Иванов И.П.</i>
    """
    return HttpResponse(text)

def about(request):
    text = f'(<h1>Имя: {name} <br /> Фамилия: {surname} <br /> Отчество: {fathername} <br /> Тел: {phone} <br /> email: {email})'
    return HttpResponse(text)