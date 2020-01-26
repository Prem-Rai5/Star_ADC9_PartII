from django.shortcuts import render, redirect
from . models import Book
from . forms import BookCreate
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):
    shelf = Book.objects.all()
    return render(request, 'book/library.html', {'shelf': shelf})

def upload(request):
    upload = BookCreate()
    if request.method == 'POST':
        upload = BookCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
            
    else:
     return render(request, 'book/upload_form.html', {'upload_form':upload})

def update_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_form = BookCreate(request.POST or None, instance = book_sel)
    if book_form.is_valid():
       book_form.save()
       return redirect('index')
    return render(request, 'book/upload_form.html', {'upload_form':book_form})
def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_sel.delete()
    return redirect('index')

    #Search
def search(request):
    return render(request, 'book/searchforms.html')

def searchdata(request):
    book_multiples = Book.objects.filter(name = request.GET['name'])
    print(book_multiples)
    return render(request, 'book/library.html',{'shelf':book_multiples}) 

    #signup

def signup_part(request):
  if request.method == 'GET':
    return render(request, 'book/signUp.html')
  else:
         print(request.POST)
         user = User.objects.create_user(username=request.POST['input_Username'], password=request.POST['input_Password'], email=request.POST['input_Email'])
         print(user)
         user.save()
         return HttpResponse("Signup Successful")

    #Login
def login_part(request):
    if request.method == 'GET':
        return render(request, 'book/login.html')

    else:
        print(request.POST)
        user = authenticate(username = request.POST['input_Username'], password = request.POST['input_Password'])
        print(user)
        if user is not None:
            login(request, user)
            return HttpResponse('login successful')

        else:
            return HttpResponse('invalid crenditals')

def logout(request):
    return render(request,"book/login.html")

def danger(request):
    if request.method == "GET":
        return render(request, "book/admin.html")