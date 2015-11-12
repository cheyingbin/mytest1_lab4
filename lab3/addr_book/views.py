# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import Context
from django.shortcuts import render_to_response
from addr_book.models import  Author, Book
from django.http import HttpResponseRedirect
# Create your views here.

    
def lib_home(request):
    return render_to_response("lib_home2.html")
    
def add_author(request):
    right = ""
    if request.POST:       
        author_name = request.POST["author_name"]  
        author_age = request.POST["author_age"]
        author_country = request.POST["author_country"]
        length = Author.objects.filter(Name = author_name).count()
        if length == 0:
            authorID = length + 1
            Author.objects.create(AuthorID = authorID, Name = author_name, Age = author_age, Country = author_country)
            return HttpResponseRedirect("/add_author_ok/")
        else:
            right = "该作者已经存在."
            return render_to_response("add_author.html",{"right":right})
    return render_to_response('add_author.html')
def add_book(request):
    word = ""
    if request.POST:
        post = request.POST
        isbn = post["isbn"]
        title = post["title"]
        author_ = post["author_name"]
        publisher = post["publisher"]
        publishdate = post["publishdate"]
        price = post["price"]
        le = Book.objects.filter(ISBN = isbn).count()
        if le == 0:
            try:
                author = Author.objects.get(Name = author_)
                new_book = Book(
                                ISBN = isbn,
                                Title = title,
                                Author = author,
                                Publisher = publisher,
                                PublishDate = publishdate,
                                Price = price
                                )
                new_book.save()
                return HttpResponseRedirect("/add_book_ok/")
            except:
                return HttpResponseRedirect("/author_not_exist/")
            else:
                word = "本书已经存在，请检查书号"
    return render_to_response('add_book.html',{"word":word})

def add_book2(request):
    word = ""
    name = request.GET["authorname"]
    if request.POST:
        post = request.POST
        post = request.POST
        isbn = post["isbn"]
        title = post["title"]
        publisher = post["publisher"]
        publishdate = post["publishdate"]
        price = post["price"]
        le = Book.objects.filter(ISBN = isbn).count()
        if le == 0:
            try:
                author = Author.objects.get(Name = name)
                new_book = Book(
                        ISBN = isbn,
                        Title = title,
                        Author = author,
                        Publisher = publisher,
                        PublishDate = publishdate,
                        Price = price
                        )
                new_book.save()
                return HttpResponseRedirect("/add_book_ok/")
            except:
                return HttpResponseRedirect("/author_not_exist/")
        else:
            word = "this book has already existed, please check the ISBN code"
    return render_to_response('add_book2.html',{"name":name, "word":word})

def delete_book(request):
    id = request.GET["id"]
    book_select = Book.objects.get(id = int(id))
    book_select.delete()
    return render_to_response("delete_book.html",id)


def update_book(request):
    id = request.GET["id"]
    abook = Book.objects.get(id = int(id))
    if request.POST:
        post = request.POST
        try:
            author = Author.objects.get(Name = post["author_name"])
            new_ps = post["publisher"]
            new_psd = post["publishdate"]
            new_price = post["price"]
            abook.Author = author
            abook.Publisher = new_ps
            abook.PublishDate = new_psd
            abook.Price = new_price
            abook.save()
            return HttpResponseRedirect("/update_book_ok/")
        except:
            return HttpResponseRedirect("/author_not_exist/")
    return render_to_response("update_book.html",Context({"book": abook, "id": id}))
def update_book_ok(request):
    return render_to_response('update_book_ok.html')


def search_book(request):
    author = Author.objects.get(Name = request.GET["authorname"])
    books = author.book_set.all()
    word = "You can also add books of this author by clicking the Add button below"
    if len(books) == 0:
        word = "The works of this author maynot be include in our database, you can add one by clicking Add below"
    c = Context({"books":books, "author":author, "word":word})
    return render_to_response('index.html',c)
    
def author_not_exist(request):
    return render_to_response('author_not_exist.html')
    
def add_author_ok(request):
    return render_to_response('add_author_ok.html')

def add_book_ok(request):
    return render_to_response('add_book_ok.html')
