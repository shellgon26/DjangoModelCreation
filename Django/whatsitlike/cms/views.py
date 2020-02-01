from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework import viewsets # React API functionality
from .serializers import CustomerSerializer, ContentSerializer, BundleSerializer, ContentViewerSerializer,ContentBundleLinkSerializer, ProgressSerializer, ViewerBundleLinkSerializer  # deliver data in JSON format
from .models import Customer, Content, Bundle, ContentViewer, ContentBundleLink, Progress, ViewerBundleLink

def index(request):
    return HttpResponse("Welcome, you're at the CMS index page.")

# return a set of customer data to the front end - the viewset is the default CRUD implementation 
class CustomerView(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
class ContentView(viewsets.ModelViewSet):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
class BundleView(viewsets.ModelViewSet):
	serializer_class = BundleSerializer
	queryset = Bundle.objects.all
class ContentViewerView(viewsets.ModelViewSet):
	serializer_class = ContentViewerSerializer
	queryset = ContentViewer.objects.all
class ContentBundleLinkView(viewsets.ModelViewSet):
	serializer_class = ContentBundleLinkSerializer
	queryset = ContentBundleLink.objects.all
class ProgressView(viewsets.ModelViewSet):
	serializer_class = ProgressSerializer
	queryset = Progress.objects.all
class ViewerBundleLinkView(viewsets.ModelViewSet):
	serializer_class = ViewerBundleLinkSerializer
	queryset = ViewerBundleLink.objects.all