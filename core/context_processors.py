from products.models import Category, Product, Brand

def categories(request):
    return{
        "categoriesContext" : Category.objects.all()
    }
    
def products(request):
    return{
        "productsContext" : Product.objects.all()
    }
def brands(request):
    return{
        "brandsContext" : Brand.objects.all()
    }