from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect, render,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import Bookform, SignUpForm
from . import forms, models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

#for index/landing page
def landingpage(request):
    return render(request,"landingpage.html")

#code for add books
@login_required(login_url = '/admin_login')
def add_book(request):
    if(request.method=="POST"):
        fm=Bookform(request.POST)
        Book.objects.create(
            name = request.POST['name'],
            author = request.POST['author'],
            isbn = request.POST['isbn'],
            category = request.POST['category'],
            admin = request.user
        )
        return HttpResponseRedirect('/view_books')
    else:
        fm=Bookform  
        
    return render(request,'add_book.html',{'form':fm})

#code for view books added by admin user
@login_required(login_url ='/admin_login')
def view_books(request):
    books = Book.objects.filter(admin_id = request.user.id)
    print(request.user.email)
    return render(request, "view_books.html", {'books':books})

#code for show all books to student
def view_students(request):
    books = Book.objects.all()
    return render(request, "view_students.html", {'books':books})
#code for delete books

#delete book added by admin
def delete_book(request, id):
    print(id)
    books = Book.objects.get(id=id)
    books.delete()
    return redirect("/view_books")

#edit book added by admin
def edit_book(request,id):
    if(request.method=="POST"):
        Book.objects.filter(id=id).update(
            name = request.POST['name'],
            author = request.POST['author'],
            isbn = request.POST['isbn'],
            category = request.POST['category'],
        )
        return HttpResponseRedirect('/view_books')
    else: 
        book = Book.objects.get(id=id)
    
    return render(request,'edit_book.html',{'form':book})

#for admin login page
def admin_login(request):
    if request.method == "POST":
        userinfo = User.objects.get(email=request.POST['email'])
        username = userinfo.username
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/add_book")
            # else:
            #     return HttpResponse("You are not an admin.")
        else:
            alert = True
            return render(request, "admin_login.html", {'alert':alert})
    return render(request, "admin_login.html")

#Register admin
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        try: 
            if not User.objects.get(email=request.POST['email']):
                return HttpResponse('This email id already registered')
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('admin_login')
        except:
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('admin_login')
            
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

#code for logout
def Logout(request):
    logout(request)
    return redirect ("/view_students")