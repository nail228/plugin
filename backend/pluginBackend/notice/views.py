from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from .models import Deadlines
import datetime

@api_view(['GET','POST','DELETE','PUT'])
def getDocs(request):
    print(Deadlines.objects.all().values())
    return Response(Deadlines.objects.all().values())
def getDay(request):
    if request.method=="GET":

        start=datetime.datetime()

