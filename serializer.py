from rest_framework import serializers
from .models import Service, Certificate, Product, User, Client, Location, TestStandard, TestSequence, PerformanceData

class ServiceSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = Service
		fields = ('id', 'serviceName', 'description', 'isF1Required', 'F1Frequency')

class CertificateSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = Certificate
		fields= '__all__'
		#fields = ('certNumber', 'certID', 'reportNumber', 'issueDate', 'userId', 'standardID', 'locationID', 'modelNum')

class ProductSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = Product
		fields = '__all__'