from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm, TaskForm
from .models import Contact, Dish
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView

def index(request):
    template = 'index.html'
    context = Dish.objects.filter(is_published_main=True)
    return render(request, template, {'food': context})

def menu(request):
    template = 'menu.html'
    food = Dish.objects.filter(is_published=True)
    return render(request, template, {'food': food})

def menu_filter(request, type):
    template = 'menu.html'
    food = Dish.objects.filter(group=type) & Dish.objects.filter(is_published=True)
    return render(request, template, {'food': food})

class FoodDetailView(DetailView):
    model = Dish
    template_name = 'food_detail.html'
    context_object_name = 'food'

def about(request):
    template = 'about.html'
    context = {
        'me': {
            'name': 'Окулов Владимир Геннадьевич',
            'phone': '+79504774507',
            'email': 'vgokulov@edu.hse.ru',
            'photo': 'https://i.pinimg.com/736x/13/8d/52/138d52a8f429510e2c16bd67990dae3c.jpg',
            'status': 'student',
        },
        'program': {
            'name': 'Управление бизнесом',
            'discription': 'Программа «Управление бизнесом» — это идеальный вариант для тех, кто не хочет ограничивать '
                           'себя в выборе будущей профессии.',
            'head': {
                'name': 'Артемьев Дмитрий Геннадьевич',
                'email': 'dartemev@hse.ru',
                'photo': 'https://www.hse.ru/org/persons/cimage/452094',
                'status': 'Program Head',
            },
            'manager': {
                'name': 'Тутынина Ольша Владимировна',
                'email': 'oshibanova@hse.ru',
                'photo': 'https://www.hse.ru/org/persons/cimage/82021055',
                'status': 'Program Manager',
            },
        },
        'students': {
            'stud_1': {
                'name': 'Павлова Анна Владимировна',
                'phone': '+79994444555',
                'email': 'avpavlova_5@edu.hse.ru',
                'photo': 'https://en.neverlose.cc/static/avatars/Xomless.png?t=1677402670',
                'status': 'student',
            },
            'stud_2': {
                'name': 'Максимова Ирина Алексеевна',
                'phone': '+79093366888',
                'email': 'iamaksimova@edu.hse.ru',
                'photo': 'https://cdn.discordapp.com/icons/804435610920026124/7318645766371f24ad610ba30ef8fc02.jpg?size=256',
                'status': 'student',
            }
        }
    }
    return render(request, template, context)

def story(request):
    template = 'story.html'
    return render(request, template)

def contact(request):
    if request.method == 'POST':
        # contact = Contact()
        # form = ContactForm(instance=contact)
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return successSend(request)
    else:
        form = ContactForm()

    template = 'contact.html'
    return render(request, template, {'form1': form})


def successSend(request):
    template = 'success.html'
    return render(request, template)


def task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            s = form.cleaned_data["s"]
            r = form.cleaned_data["r"]
            k = form.cleaned_data["k"]
            return task_answer(request, s, r, k)
    else:
        form = TaskForm()
    template = 'contact.html'
    context = {'form2': form}
    return render(request, template, context)

def task_answer(request, s,r,k):
    taskq = f'Можно ли в квадратном зале площадью {s} поместить круглую сцену радиусом {r} так, чтобы от стены до сцены был проход не менее {k}?'
    if 2*r+2*k <= s**0.5:
        ans = 'Yes'
    else:
        ans = 'No'
    template = 'answer.html'
    context = {'ans': ans, 'taskq': taskq}
    return render(request, template, context)



