from django.shortcuts import render, redirect
from django.http import JsonResponse
from .utils.key import generate_key
from .models import Url
from .forms import UrlForm


# index
def index(request):
    context = {
        'form': UrlForm()
    }
    return render(request, 'index.html', context)

# url shortener
def url_shortener(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        if url:
            key = generate_key()
            Url.objects.create(key=key, url=url)
            return JsonResponse({'key': key})
        return JsonResponse({'error': 'Invalid URL'}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)


# url short redirect
def redirect_to_url(request, key):
    short_url= Url.objects.filter(key=key).first()
    if short_url:
        return redirect(str(short_url.url))
    context = {
        'error': 'URL not found',
        'code': 404
    }
    return JsonResponse(context, status=404)

