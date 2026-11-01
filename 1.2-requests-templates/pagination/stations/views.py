from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    from .services import work_with_csv
    from django.core.paginator import Paginator
    data_list = work_with_csv()
    paginator = Paginator(data_list,10)
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    context = {
         'bus_stations': page_obj,
         'page': page_obj,
    }
    return render(request, 'stations/index.html', context)
