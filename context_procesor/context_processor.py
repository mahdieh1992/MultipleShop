from  product.models import Categories


def category_Show(request):
    categoryProduct=Categories.objects.all()
    return {'categoryProduct':categoryProduct}