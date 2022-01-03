from django.urls import path, include
from . import views 


urlpatterns = [

    # path('', views.APIServiceViews, name='apiServiceView'),
    # path('', views.APICertificateViews, name='apiCertificateView'),
    # path('', views.APIProductViews, name='apiProductView'),
    # path('', views.APIUserViews, name='apiUserView'),
    # path('', views.APIClientViews, name='apiClientView'),
    # path('', views.APILocationViews, name='apiLocationView'),
    # path('', views.APITestStandardViews, name='apiTestStandardView'),
    # path('', views.APITestSequenceViews, name='apiTestSequenceView'),
    # path('', views.APIPerformanceDataViews, name='apiPerformanceDataView'),
    
    path('certificate-list/', views.CertificateDisplay),
    path('product-list/', views.ProductDisplay),
    path('service-list/', views.ServiceDisplay),

 ]