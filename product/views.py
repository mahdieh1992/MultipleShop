from django.shortcuts import render
from .models import product,Size,Color
from django.views.generic import ListView,DetailView,View
from django.db.models import Q
from django.core.paginator import Paginator


class ProductView(ListView):
    paginate_by = 3
    template_name = 'product/Shop.html'

    def get_queryset(self):
        request = self.request
        pricemin = request.GET.get('pricemin')
        pricemax = request.GET.get('pricemax')
        color = request.GET.getlist('color')
        size = request.GET.getlist('size')
        q = request.GET.get('q')
        if q is not None:
            queryset = product.objects.filter(title__icontains=q)
            return queryset
        elif (pricemin and pricemax) or color or size:
            queryset = product.objects.all()
            queryset = queryset.filter(Q(price__gte=pricemin, price__lte=pricemax) | Q(size__title__in=size) | Q(
                color__title__in=color)).distinct()
            return queryset
        else:
            queryset = product.objects.all()
            return queryset
    def get_context_data(self,**kwargs):

        context=super().get_context_data(**kwargs)
        context['color']=Color.objects.all()
        context['size']=Size.objects.all()
        context['object'] = Size.objects.all()
        context['pricemin'] =self.request.GET.get('pricemin')
        context['pricemax'] = self.request.GET.get('pricemax')
        for color in self.request.GET.getlist('color'):
            context['color1'] =color
        for size in self.request.GET.getlist('size'):
            context['size1'] =size
        return context


class ProductDetail(DetailView):
    model = product
    template_name = 'product/detail.html'
    context_object_name = 'ProductDetail'




# Create your views here.
