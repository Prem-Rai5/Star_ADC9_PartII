from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from book.models import Book
import json

@csrf_exempt
def view_get_post_book(request):
    print("What's the request => ",request.method)
    if request.method == "GET":
        book = Book.objects.all()
        print("QuerySet objects => ",book)
        list_of_book = list(book.values("name","email"))
        print("List of Book objects => ",list_of_book)
        dictionary_name = {
        "Book":list_of_book
    }
        return JsonResponse(dictionary_name)
    elif request.method == "POST":
        print("Request body content =>", request.body)
        print("Request body type =>", type(request.body))
        python_dictionary_object = json.loads(request.body)
        print("Python dictionary contents=>",python_dictionary_object)
        print("Python dictionary type=>",type(python_dictionary_object))
        print(python_dictionary_object['name'])
        print(python_dictionary_object['email'])
        Book.objects.create(name=python_dictionary_object['name'],email=python_dictionary_object['email'])
        return JsonResponse({
            "message":"Successfully posted!!"
        })
    else:
        return HttpResponse("Other HTTP verbs testing")

@csrf_exempt
def view_getByID_updateByID_deleteByID(request,ID):
    print("What's the request =>", request.method)
    if request.method == "GET":
        book = Book.objects.get(id = ID)
        print(type(book.name))
        return JsonResponse({
            "id":Book.id,
            "name":Book.name,
            "email":Book.email
        })
    else:
        return JsonResponse({
        "message":" Other htpp verbs Testing"
        })

@csrf_exempt
def api_delete_data(request,ID):
 print("What's the request =>", request.method)
 book= Book.name.get(id=ID)   
 print(type(book.name))
 if request.method=="DELETE":
     book.delete()
     return JsonResponse({"Message":"Delete Completed"})

 else:
         return JsonResponse({"id":book.id,
         "name":book.name,
         "email":book.email,
         
         })

@csrf_exempt
def api_update_data(request,ID):
    book = Book.name.get(id = ID)
    if request.method =="PUT":
        decoded_data = request.body.decode('utf.8')
        book_data = json.loads(decoded_data)
        book.name=book_data['name']

        book.save()  
        return JsonResponse ({"Message": "Update is Done"})
    else:
        return JsonResponse({"id":Book.id,
        "name":Book.name,
        "email":Book.email
        })
@csrf_exempt
def api_book_pagination(request,PAGENO):
    SIZE =3
    skip =SIZE * (PAGENO-1)
    book=Book.name.all() [skip:PAGENO*SIZE]
    dict={
        "book":list(book.values("name","email"))
    }
    return JsonResponse(dict)
