from.models import Invoice, Project
from .serializers import InvoiceSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)

def hello_world(request):
    return render(request, 'invoice.html', {})
# create a function

def jinja_view(request):
	# create a dictionary to pass
	# data to the template
	context ={
		"data":"sample",
		"list":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	}
	# return response with template and context
	return render(request, "details.html", context)


def index(request):
   template = loader.get_template('index.html') # getting our template
   return HttpResponse(template.render())       # rendering the template in HttpResponse























class InvoiceView(viewsets.ModelViewSet):
    queryset = Invoice.objects.all().order_by('-id')
    serializer_class = InvoiceSerializer
    lookup_field = 'id'
    # filterset_class = SaleFilter
    # pagination_class = SalePagination

    def get_queryset(self):
        queryset = super().get_queryset().filter(id=id)
        if queryset is None:
            return []
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"success": "Invoice created successfully",
                             "data": {"id": serializer.data["id"],
                                      "customer name": serializer.data['cust_name'],
                                      "customer no": serializer.data['cust_no'],
                                      "customer address": serializer.data['addr'],
                                      "delivery address": serializer.data['del_addr'],
                                      "Total amount": serializer.data['tot_amt'],
                                      "pay status": serializer.data['pay_status'],
                                      "Invoice Details": serializer.data["inv_dtl"]}
                             },
                            status=status.HTTP_201_CREATED,
                            headers=headers)
    def perform_create(self, serializer):
        serializer.save()

    # def get_success_headers(self, data):
    #     try:
    #         return {'Location': str(data[api_settings.URL_FIELD_NAME])}
    #     except (TypeError, KeyError):
    #         return {}

    # def update(self, request, *args, **kwargs):
    #     stock = []
    #     extra_charge = []
    #     product = []
    #     tenant = tenant_from_request(self.request)
    #     payment = request.data.get('editPaymentData', None)
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     customer = ShopCustomer.objects.get(customerId=serializer.data['customerId'], is_deleted=False,
    #                                         tenant_id=tenant.id)
    #     customer.cust_bal = serializer.data['cust_bal_adj']
    #     customer.cust_bal_type = serializer.data['cust_bal_adj_type']
    #     customer.save(update_fields=['cust_bal', 'cust_bal_type'])
    #     if getattr(instance, '_prefetched_objects_cache', None):
    #         # If 'prefetch_related' has been applied to a queryset, we need to
    #         # forcibly invalidate the prefetch cache on the instance.
    #         instance._prefetched_objects_cache = {}
    #     for i in serializer.data["addsale"]:
    #         productid = i['productId']
    #         id = i['id']
    #         pro = dict(productId=productid, id=id)
    #         product.append(pro)
    #         if i["stockadjustment"]:
    #             stock.append(i["stockadjustment"])
    #         else:
    #             pass
    #
    #     try:
    #         receipt = serializer.data["payments"][0]['ReceiptNo']
    #         get_payment = Payment.objects.get(ReceiptNo=receipt, tenant_id=tenant.id)
    #         return Response({"success": "Sale updated successfully",
    #                          "data": {"id": serializer.data["id"],
    #                                   "ReceiptNo": receipt,
    #                                   "paymentId": get_payment.id,
    #                                   "addedDate": serializer.data["addedDate"],
    #                                   "addedDateAndTime": serializer.data["addedDateAndTime"],
    #                                   "sale_date": serializer.data['sale_date'],
    #                                   "product": product,
    #                                   "stockadjustment": stock,
    #                                   "extraChargeList": serializer.data["extraChargeList"],
    #                                   "auth_sign_url": serializer.data["auth_sign_url"],
    #                                   "banksale": serializer.data["banksale"]
    #                                   },
    #                          'cust_bal': customer.cust_bal,
    #                          'cust_bal_type': customer.cust_bal_type
    #                          },
    #                         status=status.HTTP_201_CREATED)
    #     except:
    #         return Response({"success": "Sale updated successfully",
    #                          "data": {"id": serializer.data["id"],
    #                                   "paymentId": "",
    #                                   "ReceiptNo": "",
    #                                   "product": product,
    #                                   "addedDate": serializer.data["addedDate"],
    #                                   "addedDateAndTime": serializer.data["addedDateAndTime"],
    #                                   "sale_date": serializer.data['sale_date'],
    #                                   "stockadjustment": stock,
    #                                   "extraChargeList": serializer.data["extraChargeList"],
    #                                   "auth_sign_url": serializer.data["auth_sign_url"],
    #                                   "banksale": serializer.data["banksale"]
    #                                   },
    #                          'cust_bal': customer.cust_bal,
    #                          'cust_bal_type': customer.cust_bal_type
    #                          },
    #                         status=status.HTTP_201_CREATED)
    #
    # def perform_update(self, serializer):
    #     super().perform_update(serializer)
    #
    # def partial_update(self, request, *args, **kwargs):
    #     return super().partial_update(request, *args, **kwargs)
    #
    # def retrieve(self, request, *args, **kwargs):
    #     return super().retrieve(request, *args, **kwargs)

    # def list(self, request, *args, **kwargs):
    #     tenant = tenant_from_request(self.request)
    #     sync_time = request.query_params.get('created_at')
    #     if sync_time is not None and sync_time != "":
    #         if Sync.objects.filter(tenant_id=tenant.id).exists():
    #             sync = Sync.objects.get(tenant_id=tenant.id)
    #             context = sync.last_sync
    #         else:
    #             context = None
    #         queryset = Sale.objects.filter(
    #             Q(created_at__gte=str(sync_time)) | Q(modified_at__gte=str(sync_time))).order_by('-id')
    #         qs = queryset.filter(tenant=tenant)
    #         serializer = self.get_serializer(qs, many=True)
    #         return Response({"sync_time": context, "next": None, "data": serializer.data})
    #     else:
    #         if Sync.objects.filter(tenant_id=tenant.id).exists():
    #             sync = Sync.objects.get(tenant_id=tenant.id)
    #             context = sync.last_sync
    #         else:
    #             context = None
    #         queryset = self.filter_queryset(self.get_queryset())
    #
    #         page = self.paginate_queryset(queryset)
    #         if page is not None:
    #             serializer = self.get_serializer(page, many=True)
    #             return self.get_paginated_response(serializer.data)
    #
    #         serializer = self.get_serializer(queryset, many=True)
    #         return Response({"sync_time": context, "next": None, "data": serializer.data})

    # def destroy(self, request, *args, **kwargs):
    #     stock = []
    #     extra_charge = []
    #     product_val = []
    #     tenant = tenant_from_request(self.request)
    #     instance = self.get_object()
    #     try:
    #         payment = Payment.objects.get(invoiceNo=instance.invoiceNo, tenant_id=tenant.id)
    #         if payment:
    #             payment.is_deleted = True
    #             payment.save()
    #     except Payment.DoesNotExist:
    #         payment = None
    #     for prod in instance.addsale.all():
    #         product = Product.objects.get(productId=prod.productId, tenant_id=instance.tenant_id)
    #         if not float(product.stockAvailable) == 0.0 and not float(product.stockAvailable) < 0.0:
    #             stkadj = float(product.stockAvailable) + float(prod.productQuantity)
    #             if stkadj <= 0.0:
    #                 product.stockAvailable = 0.0
    #                 product.save(update_fields=['stockAvailable'])
    #             else:
    #                 product.stockAvailable = abs(stkadj)
    #                 product.save(update_fields=['stockAvailable'])
    #         else:
    #             stkadj = float(product.stockAvailable) + float(prod.productQuantity)
    #             if stkadj <= 0.0:
    #                 product.stockAvailable = 0.0
    #                 product.save(update_fields=['stockAvailable'])
    #             else:
    #                 product.stockAvailable = abs(stkadj)
    #                 product.save(update_fields=['stockAvailable'])
    #         pro = dict(productId=prod.productId, id=prod.id, new_stock=product.stockAvailable)
    #         stock.append(pro)
    #     self.perform_destroy(instance)
    #     if payment:
    #         return Response({"success": "Sale deleted successfully", "id": instance.id, "invoiceNo": instance.invoiceNo,
    #                          "ReceiptNo": payment.ReceiptNo, "stockadjustment": stock},
    #                         status=status.HTTP_200_OK)
    #     else:
    #         return Response(
    #             {"success": "Sale deleted successfully", "id": instance.id, "invoiceNo": instance.invoiceNo,
    #              "stockadjustment": stock},
    #             status=status.HTTP_200_OK)
    #
    # def perform_destroy(self, instance):
    #     instance.is_deleted = True
    #     instance.save()

