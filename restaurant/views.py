from django.shortcuts import render
from .forms import AddTable
from .models import Orders, Table

from datetime import datetime

def restaurant_tables(request):
    orders = Orders.objects.all()
    tables = Table.objects.all() 
    form = AddTable()

    if request.method == 'POST':
        strNowDate = request.POST.get("date")
        nowDate = datetime.strptime(strNowDate, "%Y-%m-%d").date()
        if request.POST.get("name"):
            form = AddTable(request.POST)
            form.save()
            return render(request, 'thanks.html')
    else: 
        nowDate = datetime.now().date()
        strNowDate = nowDate.strftime("%Y-%m-%d")
        
    return render(request, 'index.html', {'orders': orders,'tables': tables, 'nowDate': nowDate, 'strNowDate': strNowDate, 'form': form })
 
