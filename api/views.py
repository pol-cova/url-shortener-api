from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .utils.key import generate_key
from .models import Url
from .forms import UrlForm
from django.template.loader import render_to_string
# qr
import segno
from io import BytesIO
# rest framework
from rest_framework.decorators import throttle_classes, renderer_classes
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from .serializers import UrlSerializer
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.renderers import TemplateHTMLRenderer



# index
def index(request):
    context = {
        'form': UrlForm()
    }
    return render(request, 'index.html', context)

# url shortener
class UrlShortener(generics.ListCreateAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer

    def post(self, request):
        form = UrlForm(request.data)
        if form.is_valid():
            url = form.cleaned_data['url']
            key = generate_key()
            Url.objects.create(key=key, url=url)
            # Render the response
            # Construct the message with the generated URL
            return render(request, 'sucess.html', {'form': UrlForm(), 'message': f'http://127.0.0.1:8000/{key}'})
        return Response({'error': 'Invalid URL'}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'urls': serializer.data})

    def get_queryset(self):
        return Url.objects.all()

# url short redirect
@throttle_classes([AnonRateThrottle, UserRateThrottle])
class RedirectToUrl(APIView):
    def get(self, request, key):
        short_url = Url.objects.filter(key=key).first()
        if short_url:
            return redirect(str(short_url.url))
        else:
            context = {
                'error': 'URL not found',
                'code': 404
            }
            return Response(context, status=404)

# generate qr code
@throttle_classes([AnonRateThrottle, UserRateThrottle])
class GenerateQR(APIView):
    def get(self, request):
        qr_code = segno.make_qr("QR test")
        qr_img = BytesIO()
        qr_code.save(qr_img, scale=10, kind="png")

        response = HttpResponse(content_type="image/png")
        response.write(qr_img.getvalue())

        return response