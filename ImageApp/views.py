from django.shortcuts import render,redirect
from.models import *
from .forms import *

# Create your views here.
def home(request):
    data = Profile.objects.all()#get all profiles stored in database
    return render(request,'ImageApp/home.html',{'data':data})


def BookCreate(request):
    if request.method == 'POST':
        form = BookCreateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()#saved to database
            return redirect('home')
    else:
        form = BookCreateForm()        
    return render(request,'ImageApp/book-create.html',{'form':form})    


def BookListView(request):
    books = Book.objects.all()
    return render(request,'ImageApp/book-list.html', {'books':books})


def BookDetailView(request,pk):
    book = Book.objects.get(id = pk)
    return render(request,'ImageApp/book_detail.html',{'book':book})    


def BookUpdateView(request,pk):
    book = Book.objects.get(id = pk)
    if request.method == "POST":
        form = BookCreateForm(instance = book,data=request.POST,files = request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book-detail', book.id)
    else:
        form = BookCreateForm(instance= book) 

    return render(request,'ImageApp/book_update.html',{'book':book,'form':form})     


def BookDeleteView(request,pk):
    book = Book.objects.get(id = pk)
    if request.method == 'POST':
        form = ConfirmForm(request.POST)
        if form.is_valid():
            book.delete()
            return redirect('book-list')
    else:
        form = ConfirmForm()
        return render(request, 'ImageApp/book_confirm_delete.html',{'book':book, 'form':form})                      