from django.shortcuts import render
from .models import Sales
from .utils import get_plot

def visualize(request):
    sales = Sales.objects.all()
    x = [x.item for x in sales]
    y = [y.price for y in sales]
    
    graph = get_plot(x,y)

    return render(request, 'visualization/visualize.html', {'graph': graph})
