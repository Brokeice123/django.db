from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Student
from .models import Products


def index_page(request):
    data = Student.objects.all()
    context = {'data': data}
    return render(request, "index2.html", context)


def login_page(request):
    return render(request, "login.html")


def signup_page(request):
    return render(request, "signup.html")


def edit_page(request):
    return render(request, "edit.html")


def insertdata(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        country = request.POST.get('city')

        query = Student(name=name, email=email, age=age, gender=gender, phone=phone, city=city, country=country)
        query.save()
        return redirect("/")

    return render(request, "/")


def deleteData(request, id):
    d = Student.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, "index2.html")


# slash means that it is retuning to the root page


def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        country = request.POST.get('country')

        update_info = Student.objects.get(id=id)
        update_info.name = name
        update_info.email = email
        update_info.age = age
        update_info.gender = gender
        update_info.phone = phone
        update_info.city = city
        update_info.country = country

        update_info.save()
        return redirect("/")

    d = Student.objects.get(id=id)
    context = {"d": d}
    return render(request, "edit.html", context)


def insertproducts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        quantity = request.POST.get('quantity')

        query = Products(name=name, price=price, description=description, quantity=quantity)
        query.save()

    return render(request, "products.html")
