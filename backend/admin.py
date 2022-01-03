from django.contrib import admin
from .models import Service, Certificate, Product, User, Client, Location, TestStandard, TestSequence, PerformanceData

admin.site.register(Service)
admin.site.register(Certificate)
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Client)
admin.site.register(Location)
admin.site.register(TestStandard)
admin.site.register(TestSequence)
admin.site.register(PerformanceData)