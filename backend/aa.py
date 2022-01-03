from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser
class Client(models.Model):
	
	clientName = models.CharField(max_length=50, null = True)
	clientType = models.CharField(max_length =20, null = True)


class User(models.Model):
	firstName = models.CharField(max_length=20, null=True)
	lastName = models.CharField(max_length=50, null = True)
	middleName = models.CharField(max_length=20, null = True)
	jobTitle = models.CharField(max_length=10, null = True)
	email = models.EmailField(max_length=255, unique=True, null = True)
	officePhone = models.CharField(max_length=10, null = True)
	cellPhone = models.CharField(max_length=10, null = True)
	prefix = models.IntegerField(null = True)
	clientID = models.ForeignKey(Client, on_delete = models.CASCADE, null=True)

class Location(models.Model):
	address1 = models.CharField(max_length=255,null=True)
	address2 =models.CharField(max_length=20,null=True)
	city =models.CharField(max_length=20,null=True)
	state =models.CharField(max_length=20,null=True)
	country =models.CharField(max_length=20,null=True)
	phone =models.CharField(max_length=12,null=True)
	fax =models.CharField(max_length=10,null=True)
	clientID = models.ForeignKey(Client, on_delete = models.CASCADE, null=True)

class TestStandard(models.Model):
	
	standardName=models.CharField(max_length=30,null=True) 
	description =models.CharField(max_length=255,null=True)
	publishedDate = models.DateField(null=True)


class TestSequence(models.Model):
	sequenceName =models.IntegerField(int,null=True)


class Service(models.Model):

	serviceName =models.CharField(max_length=50,null=True)
	description =models.CharField(max_length=255,null=True)
	isF1Required =models.CharField(max_length=3,null=True)
	F1Frequency =models.FloatField(max_length=255,null=True)
	standardID = models.ForeignKey(TestStandard, on_delete = models.CASCADE, null=True)

class Product(models.Model):
	modelNumber =models.CharField(max_length=10,unique = True, primary_key=True)
	productName =models.CharField(max_length=50,null=True)
	cellTechnology =models.CharField(max_length=50,null=True)
	cellManufacturer =models.CharField(max_length=50,null=True)
	numberofCells =models.IntegerField(int,null=True)
	numberofCellsinSeries =models.IntegerField(int,null=True)
	numberofSeriesStrings =models.IntegerField(int, null=True)
	numberofDiode =models.IntegerField(int,null=True)
	productLength =models.FloatField(float,null=True)
	productWidth =models.FloatField(float,null=True)
	productWeight =models.FloatField(float,null=True)
	superStateType =models.CharField(max_length=50,null=True)
	superStateManufacturer =models.CharField(max_length=50,null=True)
	substrateType =models.CharField(max_length=50,null=True)
	substrateManufacturer =models.CharField(max_length=50,null=True)
	frameType =models.CharField(max_length=50,null=True)
	frameAdhesive =models.CharField(max_length=50,null=True)
	encapsulateType =models.CharField(max_length=50,null=True)
	encapsulantManufacturer =models.CharField(max_length=50,null=True)
	junctionBoxType =models.CharField(max_length=50,null=True)
	junctionBoxManufacturer =models.CharField(max_length=50,null=True)


class PerformanceData(models.Model):

	maxSystemVoltage =models.FloatField(float,null=True)
	voc =models.FloatField(max_length=50,null=True)
	isc =models.FloatField(max_length=50,null=True)
	vmp =models.FloatField(max_length=50,null=True)
	imp =models.FloatField(max_length=50,null=True)
	pmp =models.FloatField(max_length=50,null=True)
	ff =models.FloatField(max_length=50,null=True)
	modelNum = models.ForeignKey(Product, on_delete = models.CASCADE, null=True)
	sequenceId = models.ForeignKey(TestSequence, on_delete = models.CASCADE, null=True)


class Certificate(models.Model):
	certNumber= models.IntegerField(int, unique=True, primary_key = True)
	certID =models.IntegerField(int,null=True)
	reportNumber=models.IntegerField(int,null=True)
	issueDate =models.DateField(null=True)


	userId = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
	standardID = models.ForeignKey(TestStandard, on_delete = models.CASCADE, null=True)
	locationID = models.ForeignKey(Location, on_delete = models.CASCADE, null=True)

	modelNum = models.ForeignKey(Product, on_delete = models.CASCADE, null=True)
