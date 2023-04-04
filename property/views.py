from .models import Property
from django.views.generic import ListView, DetailView

class PropertyListView(ListView):
    model = Property
    template_name = 'property_list.html'
    context_object_name = 'property_list'
    paginate_by = 10


class PropertyDetailView(DetailView):
    model = Property
    template_name = 'property_detail.html'
    context_object_name = 'property_detail'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the blogs
        context['latest_posts'] = Property.objects.all()[:5]
        return context


class SellPropertyListView(ListView):
    model = Property
    template_name = 'sell_property_list.html'
    context_object_name = 'sell_property_list'
    paginate_by = 10


class SellPropertyDetailView(DetailView):
    model = Property
    template_name = 'sell_property_detail.html'
    context_object_name = 'sell_property_detail'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the blogs
        context['latest_posts'] = Property.objects.all()[:5]

        return context
