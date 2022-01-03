from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Service, Certificate, Product, User, Client, Location, TestStandard, TestSequence, PerformanceData
from .serializer import ServiceSerializer, CertificateSerializer, ProductSerializer
from rest_framework.decorators import api_view

# @api_view(['GET'])
# def APIServiceViews(request):
# 	serviceURLS={
# 	'List': '/service-list/',
# 	'Detail View': '/service-detail/<int:id>',
# 	'Create': '/service-create/',
# 	'Update': '/service-update/<int:id>',
# 	'Delete': '/service-detail/<int:id>'
# 	}
# 	return Response(serviceURLS)

# @api_view(['GET'])
# def APICertificateViews(request):
# 	certificateURLS={
# 	'List': '/certificate-list/',
# 	'Detail View': '/certificate-detail/<int:id>',
# 	'Create': '/certificate-create/',
# 	'Update': '/certificate-update/<int:id>',
# 	'Delete': '/certificate-detail/<int:id>'
# 	}
# 	return Response(certificateURLS)

# @api_view(['GET'])
# def APIProductViews(request):
# 	productURLS={
# 	'List': '/product-list/',
# 	'Detail View': '/product-detail/<int:id>',
# 	'Create': '/product-create/',
# 	'Update': '/product-update/<int:id>',
# 	'Delete': '/product-detail/<int:id>'
# 	}
# 	return Response(productURLS)

# @api_view(['GET'])
# def APIUserViews(request):
# 	userURLS={
# 	'List': '/user-list/',
# 	'Detail View': '/user-detail/<int:id>',
# 	'Create': '/user-create/',
# 	'Update': '/user-update/<int:id>',
# 	'Delete': '/user-detail/<int:id>'
# 	}
# 	return Response(userURLS)

# @api_view(['GET'])
# def APIClientViews(request):
# 	clientURLS={
# 	'List': '/client-list/',
# 	'Detail View': '/client-detail/<int:id>',
# 	'Create': '/client-create/',
# 	'Update': '/client-update/<int:id>',
# 	'Delete': '/client-detail/<int:id>'
# 	}
# 	return Response(clientURLS)

# @api_view(['GET'])
# def APILocationViews(request):
# 	locationURLS={
# 	'List': '/location-list/',
# 	'Detail View': '/location-detail/<int:id>',
# 	'Create': '/location-create/',
# 	'Update': '/location-update/<int:id>',
# 	'Delete': '/location-detail/<int:id>'
# 	}
# 	return Response(locationURLS)	

# @api_view(['GET'])
# def APITestStandardViews(request):
# 	testStandardURLS={
# 	'List': '/testStandard-list/',
# 	'Detail View': '/testStandard-detail/<int:id>',
# 	'Create': '/testStandard-create/',
# 	'Update': '/testStandard-update/<int:id>',
# 	'Delete': '/testStandard-detail/<int:id>'
# 	}
# 	return Response(testStandardURLS)

# @api_view(['GET'])
# def APIPerformanceDataViews(request):
# 	performanceDataURLS={
# 	'List': '/performanceData-list/',
# 	'Detail View': '/performanceData-detail/<int:id>',
# 	'Create': '/performanceData-create/',
# 	'Update': '/performanceData-update/<int:id>',
# 	'Delete': '/performanceData-detail/<int:id>'
# 	}
# 	return Response(performanceDataURLS)

# @api_view(['GET'])
# def APITestSequenceViews(request):
# 	testSequenceURLS={
# 	'List': '/testSequence-list/',
# 	'Detail View': '/testSequence-detail/<int:id>',
# 	'Create': '/testSequence-create/',
# 	'Update': '/testSequence-update/<int:id>',
# 	'Delete': '/testSequence-detail/<int:id>'
# 	}
# 	return Response(testSequenceURLS)


@api_view(['GET'])
def ServiceDisplay(request):
	services = Service.objects.all() 
	serializer = ServiceSerializer(services, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def ProductDisplay(request):
	products = Product.objects.all() 
	serializer = ProductSerializer(products, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def CertificateDisplay(request):
	certificates = Certificate.objects.all() 
	serializer = CertificateSerializer(certificates, many=True)
	return Response(serializer.data)
