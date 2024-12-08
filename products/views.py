
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Comment
from .forms import CommentForm
from django.contrib import messages
# Create your views here.
def product_detail (request, pk):
    categories = Category.objects.all()
    product = get_object_or_404 (Product, pk=pk)
        
    # related_products = Product.objects.filter(category = product.category). exclude (pk=pk)
    comments = product.comments.all()
    if request.method == "POST":  
        form = CommentForm(request.POST)  
        if form.is_valid():  
            comment = form.save(commit=False)  
            comment.product = product  
            comment.user = request.user  
            comment.save()  
            return redirect('product_detail', product.id)  
    else:  
        form = CommentForm()
    context = {
        'product' : product,
        'categories' : categories,
        'comments' : comments,
        'form':form,
    }
    return render (request, 'products/product_detail.html', context)

def product_category (request, pk): 
    categories = Category.objects.all()
    category = get_object_or_404(Category, pk =pk)
    products = Product.objects.filter(category = category)
    context = {
            'products': products,
            'categories' : categories,
    }
    return render (request, 'products/store.html', context)

def store(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    count = products. count
    context = {
    'products': products,
    'categories': categories,
    'count': count
    }
    return render(request, 'products/store.html', context)
def search(request):  
    categories = Category.objects.all()  
    query = request.GET.get('q')  
    if query:  
        products = Product.objects.filter(name__icontains=query)  
        if products is not None:  
            count = products.count  
            context = {  
            'products': products,  
            'categories': categories,  
            'count': count ,
            'query' : query
            }  
            return render(request, 'products/store.html', context)  
        else:  
            messages.error(request, "No products found")  
    else:  
        products = Product.objects.all()  
    count = products.count
    
    return render(request, 'products/store.html', context)