from products.models import Category, Product 

def categories(request):
    return{
        "categoriesContext" : Category.objects.all()
    }
    
def products(request):
    return{
        "productsContext" : Product.objects.all()
    }