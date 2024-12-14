
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Comment
from .forms import CommentForm
from django.db.models import Q
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

def filter(request):
    category_id = request.GET.get('category',None)
    brand_ids = request.GET.getlist('brand', None)
    on_sale = request.GET.get('on_sale', False)
    min_price = request.GET.get('min_price', 0)
    max_price = request.GET.get('max_price', None)
    
    filters = Q()
    
    if category_id:
        filters &= Q(category_id=category_id)
    if brand_ids:
        filters &= Q(brand_id__in=brand_ids)
    if on_sale:
        filters &= Q(on_sale=True)
    if min_price:
        filters &= Q(price__gte=min_price) 
    if max_price:
        filters &= Q(price__lte=max_price) 
    
    products = Product.objects.filter(filters)
    count = products.count
    context = {
        'products': products,
        'count': count,
    }
    return render(request, 'products/store.html',context)