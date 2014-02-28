#FILE: roster/views.py
# Create your views here.
from roster.models import Best, Athlete
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    context = {
        'athlete_count': Athlete.objects.count(),
        'best_count': Best.objects.count(),
    }
    return render(request, "roster/home.html", context)

def best(request, pk):
    #best = Best. objects.order_by('?')[0]
    best = get_object_or_404(Best, id=pk)
    return render(request, "roster/best.html", {'best': best})

def bestList(request):
    best_list = Best.objects.all()
    paginator = Paginator(best_list, 25)
    page = request.GET.get('page')
    try:
        bests= paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        bests = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        bests = paginator.page(paginator.num_pages)
        
    return render(request, 'roster/best_list.html', {"bests": bests})

def athlete(request, pk):
    #athlete = Athlete.objects.order_by('?')[0]
    athlete = get_object_or_404(Athlete, id=pk)
    return render(request, "roster/athlete.html", {'athlete': athlete})

def athleteList(request):
    #athlete = Athlete.objects.order_by('?')[0]
    athlete_list = Athlete.objects.all()
    
        
    return render(request, 'roster/athlete_list.html', {"athletes": athlete_list})
    