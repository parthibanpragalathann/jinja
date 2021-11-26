from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from .views import InvoiceView, index, jinja_view, project_index, project_detail
invoice_router = routers.DefaultRouter()

invoice_router.register('invoice', InvoiceView, basename="Invoice")

urlpatterns = [
    url('', include(invoice_router.urls)),
    path('index/', index),
    path('demo/', jinja_view),
    path("project/", project_index, name="project"),
    path("project/<int:pk>/", project_detail, name="project_detail"),
    ]