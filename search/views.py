

from django.db.models import Q
from django.views.generic import TemplateView, ListView

from shop.models import Product




class SearchResultsView(ListView):
    model = Product
    template_name = 'search/search_results.html'
    
    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(name__icontains=query) | Q(slug__icontains=query)
        )
        return object_list

