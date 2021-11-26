from datetime import datetime, timedelta
from datetime import date
from rest_framework import serializers
from .models import Invoice, InvoiceDetails, Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class InvoiceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetails
        fields = "__all__"

class InvoiceSerializer(serializers.ModelSerializer):
    cust_name = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    cust_no = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    addr = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    del_addr = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    tot_amt = serializers.IntegerField(required=False)
    pay_status = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    created_at = serializers.DateTimeField(format="%d %b %Y / %I:%M %p", required=False)
    updated_at = serializers.DateTimeField(format="%d %b %Y / %I:%M %p", required=False)
    inv_dtl = InvoiceDetailsSerializer(many=True, required=False)

    class Meta:
        model = Invoice
        fields = ('id', 'cust_name', 'cust_no', 'addr', 'del_addr', 'tot_amt', 'pay_status', 'inv_dtl',)
        read_only_fields = ('created_at', 'updated_at')

    def create(self, validated_data):
        inv_dtl_data = validated_data.pop('inv_dtl', None)
        invoice_obj = Invoice.objects.create(**validated_data)
        if inv_dtl_data is not None:
            for inv_data in inv_dtl_data:
                InvoiceDetails.objects.create(inv_dtl=invoice_obj, **inv_data)
        return invoice_obj

    # def update(self, instance, validated_data):
    #     tenant_new = tenant_from_request(self.context['request'])
    #     # tenant = self.context["request"].tenant_schema_name
    #     messageState = self.context["request"].data.get("messageState")
    #     business_name = self.context["request"].data.get("businessName")
    #     business_no = self.context["request"].data.get("businessPhoneNumber")
    #     customer_phone = validated_data["customerPhoneNo"]
    #         # cust_name = validated_data["cust_name"]
    #         # cust_no = validated_data["cust_no"]
    #         # addr = validated_data["cust_name"]
    #         # del_addr = validated_data["cust_no"]
    #         # tot_amt = validated_data["tot_amt"]
    #         # addr = validated_data["cust_name"]
    #         # pay_status = validated_data["pay_status"]
    #     instance.invoiceNo = validated_data.get('invoiceNo', instance.invoiceNo)
    #     instance.addedDate = validated_data.get('addedDate', instance.addedDate)
    #     instance.addedDateAndTime = validated_data.get('addedDateAndTime', instance.addedDateAndTime)
    #     instance.businessName = validated_data.get('businessName', instance.businessName)
    #     instance.businessAddress1 = validated_data.get('businessAddress1', instance.businessAddress1)
    #     instance.businessAddress2 = validated_data.get('businessAddress2', instance.businessAddress2)
    #     instance.businessEmail = validated_data.get('businessEmail', instance.businessEmail)
    #     instance.businessGSTIN = validated_data.get('businessGSTIN', instance.businessGSTIN)
    #     instance.businessPhoneNumber = validated_data.get('businessPhoneNumber', instance.businessPhoneNumber)
    #     instance.customerId = validated_data.get('customerId', instance.customerId)
    #     instance.customerName = validated_data.get('customerName', instance.customerName)
    #     instance.taxTyp = validated_data.get('taxTyp', instance.taxTyp)
    #     instance.customerPhoneNo = validated_data.get('customerPhoneNo', instance.customerPhoneNo)
    #     instance.customerEmail = validated_data.get('customerEmail', instance.customerEmail)
    #     instance.customerGSTIN = validated_data.get('customerGSTIN', instance.customerGSTIN)
    #     instance.customerBillingAddress = validated_data.get('customerBillingAddress', instance.customerBillingAddress)
    #     instance.customerBillingState = validated_data.get('customerBillingState', instance.customerBillingState)
    #     instance.customerShippingAddress = validated_data.get('customerShippingAddress',
    #                                                           instance.customerShippingAddress)
    #     instance.customerShippingState = validated_data.get('customerShippingState', instance.customerShippingState)
    #     instance.saleSubTotal = validated_data.get('saleSubTotal', instance.saleSubTotal)
    #     instance.saleGstAmount = validated_data.get('saleGstAmount', instance.saleGstAmount)
    #     instance.salePaidAmount = validated_data.get('salePaidAmount', instance.salePaidAmount)
    #     instance.saleBillAmount = validated_data.get('saleBillAmount', instance.saleBillAmount)
    #     instance.saleExcessAmount = validated_data.get('saleExcessAmount', instance.saleExcessAmount)
    #     instance.salePendingAmount = validated_data.get('salePendingAmount', instance.salePendingAmount)
    #     instance.salePaymentMode = validated_data.get('salePaymentMode', instance.salePaymentMode)
    #     instance.salePaymentType = validated_data.get('salePaymentType', instance.salePaymentType)
    #     instance.saleCreditPeriod = validated_data.get('saleCreditPeriod', instance.saleCreditPeriod)
    #     instance.saleCreditPeriodDate = validated_data.get('saleCreditPeriodDate', instance.saleCreditPeriodDate)
    #     instance.quoteNo = validated_data.get('quoteNo', instance.quoteNo)
    #     instance.discount = validated_data.get('discount', instance.discount)
    #     instance.itemTtl = validated_data.get('itemTtl', instance.itemTtl)
    #     instance.xtraCharg = validated_data.get('xtraCharg', instance.xtraCharg)
    #     instance.partPaymentFlag = validated_data.get('partPaymentFlag', instance.partPaymentFlag)
    #     instance.fullPaymentFlag = validated_data.get('fullPaymentFlag', instance.fullPaymentFlag)
    #     instance.cust_bal_adj = validated_data.get('cust_bal_adj', instance.cust_bal_adj)
    #     instance.cust_bal_adj_type = validated_data.get('cust_bal_adj_type', instance.cust_bal_adj_type)
    #     instance.adj_bal = validated_data.get('adj_bal', instance.adj_bal)
    #     instance.notes = validated_data.get('notes', instance.notes)
    #     instance.inclusiveOfGST = validated_data.get('inclusiveOfGST', instance.inclusiveOfGST)
    #     instance.adj_bal_type = validated_data.get('adj_bal_type', instance.adj_bal_type)
    #     instance.opening_bal = validated_data.get('opening_bal', instance.opening_bal)
    #     instance.opening_bal_type = validated_data.get('opening_bal_type', instance.opening_bal_type)
    #     instance.device = validated_data.get('device', instance.device)
    #     instance.is_deleted = validated_data.get('is_deleted', instance.is_deleted)
    #     instance.footer_notes = validated_data.get('footer_notes', instance.footer_notes)
    #     instance.print_bank_details = validated_data.get('print_bank_details', instance.print_bank_details)
    #     instance.print_auth_sign = validated_data.get('print_auth_sign', instance.print_auth_sign)
    #     instance.show_cust_sign = validated_data.get('show_cust_sign', instance.show_cust_sign)
    #     token = self.randomword(6)
    #     instance.file_token = token
    #     url = "https://{}.vasoolbooksandbox.in/invoice/{}".format(tenant_new.schema_name, token)
    #     customer_invoice = CustomerInvoice.objects.create(invoice=url, tenant_id=tenant_new.id)
    #     instance.is_updated = True
    #     instance.save(update_fields=['invoiceNo', 'addedDate', 'addedDateAndTime', 'businessName', 'businessAddress1',
    #                                  'businessAddress2', 'businessEmail', 'businessGSTIN', 'businessPhoneNumber',
    #                                  'customerId', 'customerName', 'taxTyp', 'customerPhoneNo', 'customerEmail',
    #                                  'customerGSTIN', 'customerBillingAddress', 'customerBillingState',
    #                                  'customerShippingAddress', 'customerShippingState', 'saleSubTotal',
    #                                  'saleGstAmount', 'salePaidAmount', 'saleBillAmount', 'salePendingAmount',
    #                                  'salePaymentMode', 'salePaymentType', 'saleCreditPeriod', 'saleCreditPeriodDate',
    #                                  'quoteNo', 'file_token', 'discount', 'itemTtl', 'xtraCharg', 'partPaymentFlag',
    #                                  'is_updated', 'fullPaymentFlag', 'device', 'file_token', 'cust_bal_adj',
    #                                  'cust_bal_adj_type', 'adj_bal', 'adj_bal_type', 'opening_bal', 'opening_bal_type',
    #                                  'inclusiveOfGST', 'notes', 'print_bank_details', 'print_auth_sign', 'show_cust_sign',
    #                                  'footer_notes'])
    #
    #     add_sale = validated_data.pop('addsale')
    #     ex_charge = validated_data.pop('extraChargeList')
    #     payment = self.context["request"].data.get("editPaymentData")
    #     delete_product = self.context["request"].data.get("deleteProductEdit")
    #     if delete_product is not None:
    #         for product in delete_product:
    #             get_product = Product.objects.get(productId=product['productId'], tenant_id=tenant_new.id)
    #             stkadj = float(get_product.stockAvailable) + float(product['productQty'])
    #             get_product.stockAvailable = stkadj
    #             get_product.save(update_fields=['stockAvailable'])
    #
    #     if payment["Status"] == "Update":
    #         try:
    #             get_adjust = InvoiceAdjustment.objects.get(payment_id=int(payment['sync_id']),
    #                                                        invoiceNo=payment["invoiceNo"], tenant_id=tenant_new.id)
    #             adjamt = float(get_adjust.adjustedAmount) - float(payment['amountReceived'])
    #             get_adjust.salePaidAmount = instance.salePaidAmount
    #             get_adjust.salePendingAmount = instance.salePendingAmount
    #             get_adjust.salePaymentType = instance.salePaymentType
    #             get_adjust.adjustedAmount = adjamt
    #             get_adjust.save()
    #             pay_obj = Payment.objects.get(ReceiptNo=payment["ReceiptNo"], invoiceNo=0, id=payment['sync_id'],
    #                                           tenant_id=tenant_new.id)
    #             try:
    #
    #                 if len(payment["delRecpt"]) > 0:
    #                     for i in payment["delRecpt"]:
    #                         get_adjust = InvoiceAdjustment.objects.get(payment_id=i, invoiceNo=payment["invoiceNo"],
    #                                                                    tenant_id=tenant_new.id)
    #                         get_adjust.is_deleted = True
    #                         amtrcvd = abs(float(payment["amountReceived"]) - float(get_adjust.adjustedAmount))
    #                         pay_obj.amountReceived = payment["amountReceived"]
    #                         pay_obj.balanceAmount = payment["balanceAmount"]
    #                         pay_obj.invoiceNo = instance.invoiceNo
    #                         pay_obj.invoiceAmount = instance.saleBillAmount
    #                         pay_obj.paymentMode = instance.salePaymentMode
    #                         pay_obj.amountReceived = amtrcvd
    #                         pay_obj.balanceAmount = instance.salePendingAmount
    #                         pay_obj.customerId = instance.customerId
    #                         pay_obj.customerName = instance.customerName
    #                         pay_obj.customerEmail = instance.customerEmail
    #                         pay_obj.customerPhoneNo = instance.customerPhoneNo
    #                         pay_obj.customerBillingAddress = instance.customerBillingAddress
    #                         pay_obj.customerBillingState = instance.customerBillingState
    #                         pay_obj.customerShippingAddress = instance.customerShippingAddress
    #                         pay_obj.customerShippingState = instance.customerShippingState
    #                         pay_obj.businessName = instance.businessName
    #                         pay_obj.businessPhoneNumber = instance.businessPhoneNumber
    #                         pay_obj.businessAddress1 = instance.businessAddress1
    #                         pay_obj.businessAddress2 = instance.businessAddress2
    #                         pay_obj.businessGSTIN = instance.businessGSTIN
    #                         pay_obj.businessEmail = instance.businessEmail
    #                         pay_obj.customerGSTIN = instance.customerGSTIN
    #                         pay_obj.cust_bal_adj = instance.cust_bal_adj
    #                         pay_obj.cust_bal_adj_type = instance.cust_bal_adj_type
    #                         pay_obj.adj_bal = instance.adj_bal
    #                         pay_obj.adj_bal_type = instance.adj_bal_type
    #                         pay_obj.opening_bal = instance.opening_bal
    #                         pay_obj.opening_bal_type = instance.opening_bal_type
    #                         pay_obj.device = instance.device
    #                         pay_obj.is_updated = True
    #                         pay_obj.save()
    #                 else:
    #                     pay_obj = Payment.objects.get(ReceiptNo=payment["ReceiptNo"], invoiceNo=payment['invoiceNo'],
    #                                                   tenant_id=tenant_new.id)
    #                     amtrcvd = abs(float(payment["amountReceived"]) - float(get_adjust.adjustedAmount))
    #                     pay_obj.amountReceived = payment["amountReceived"]
    #                     pay_obj.balanceAmount = payment["balanceAmount"]
    #                     pay_obj.invoiceNo = instance.invoiceNo
    #                     pay_obj.invoiceAmount = instance.saleBillAmount
    #                     pay_obj.paymentMode = instance.salePaymentMode
    #                     pay_obj.amountReceived = amtrcvd
    #                     pay_obj.balanceAmount = instance.salePendingAmount
    #                     pay_obj.customerId = instance.customerId
    #                     pay_obj.customerName = instance.customerName
    #                     pay_obj.customerEmail = instance.customerEmail
    #                     pay_obj.customerPhoneNo = instance.customerPhoneNo
    #                     pay_obj.customerBillingAddress = instance.customerBillingAddress
    #                     pay_obj.customerBillingState = instance.customerBillingState
    #                     pay_obj.customerShippingAddress = instance.customerShippingAddress
    #                     pay_obj.customerShippingState = instance.customerShippingState
    #                     pay_obj.businessName = instance.businessName
    #                     pay_obj.businessPhoneNumber = instance.businessPhoneNumber
    #                     pay_obj.businessAddress1 = instance.businessAddress1
    #                     pay_obj.businessAddress2 = instance.businessAddress2
    #                     pay_obj.businessGSTIN = instance.businessGSTIN
    #                     pay_obj.businessEmail = instance.businessEmail
    #                     pay_obj.customerGSTIN = instance.customerGSTIN
    #                     pay_obj.cust_bal_adj = instance.cust_bal_adj
    #                     pay_obj.cust_bal_adj_type = instance.cust_bal_adj_type
    #                     pay_obj.adj_bal = instance.adj_bal
    #                     pay_obj.adj_bal_type = instance.adj_bal_type
    #                     pay_obj.opening_bal = instance.opening_bal
    #                     pay_obj.opening_bal_type = instance.opening_bal_type
    #                     pay_obj.device = instance.device
    #                     pay_obj.is_updated = True
    #                     pay_obj.save()
    #             except:
    #                 pay_obj = Payment.objects.get(ReceiptNo=payment["ReceiptNo"], invoiceNo="0",
    #                                               tenant_id=tenant_new.id)
    #                 amtrcvd = abs(float(payment["amountReceived"]) - float(get_adjust.adjustedAmount))
    #                 pay_obj.amountReceived = payment["amountReceived"]
    #                 pay_obj.balanceAmount = payment["balanceAmount"]
    #                 pay_obj.invoiceNo = instance.invoiceNo
    #                 pay_obj.invoiceAmount = instance.saleBillAmount
    #                 pay_obj.paymentMode = instance.salePaymentMode
    #                 pay_obj.amountReceived = amtrcvd
    #                 pay_obj.balanceAmount = instance.salePendingAmount
    #                 pay_obj.customerId = instance.customerId
    #                 pay_obj.customerName = instance.customerName
    #                 pay_obj.customerEmail = instance.customerEmail
    #                 pay_obj.customerPhoneNo = instance.customerPhoneNo
    #                 pay_obj.customerBillingAddress = instance.customerBillingAddress
    #                 pay_obj.customerBillingState = instance.customerBillingState
    #                 pay_obj.customerShippingAddress = instance.customerShippingAddress
    #                 pay_obj.customerShippingState = instance.customerShippingState
    #                 pay_obj.businessName = instance.businessName
    #                 pay_obj.businessPhoneNumber = instance.businessPhoneNumber
    #                 pay_obj.businessAddress1 = instance.businessAddress1
    #                 pay_obj.businessAddress2 = instance.businessAddress2
    #                 pay_obj.businessGSTIN = instance.businessGSTIN
    #                 pay_obj.businessEmail = instance.businessEmail
    #                 pay_obj.customerGSTIN = instance.customerGSTIN
    #                 pay_obj.cust_bal_adj = instance.cust_bal_adj
    #                 pay_obj.cust_bal_adj_type = instance.cust_bal_adj_type
    #                 pay_obj.adj_bal = instance.adj_bal
    #                 pay_obj.adj_bal_type = instance.adj_bal_type
    #                 pay_obj.opening_bal = instance.opening_bal
    #                 pay_obj.opening_bal_type = instance.opening_bal_type
    #                 pay_obj.device = instance.device
    #                 pay_obj.is_updated = True
    #                 pay_obj.save()
    #
    #
    #         except:
    #             pay_obj = Payment.objects.get(ReceiptNo=payment["ReceiptNo"], invoiceNo=payment["invoiceNo"],
    #                                           tenant_id=tenant_new.id)
    #             pay_obj.amountReceived = payment["amountReceived"]
    #             pay_obj.balanceAmount = payment["balanceAmount"]
    #             pay_obj.invoiceNo = instance.invoiceNo
    #             pay_obj.invoiceAmount = instance.saleBillAmount
    #             pay_obj.paymentMode = instance.salePaymentMode
    #             pay_obj.amountReceived = instance.salePaidAmount
    #             pay_obj.balanceAmount = instance.salePendingAmount
    #             pay_obj.customerId = instance.customerId
    #             pay_obj.customerName = instance.customerName
    #             pay_obj.customerEmail = instance.customerEmail
    #             pay_obj.customerPhoneNo = instance.customerPhoneNo
    #             pay_obj.customerBillingAddress = instance.customerBillingAddress
    #             pay_obj.customerBillingState = instance.customerBillingState
    #             pay_obj.customerShippingAddress = instance.customerShippingAddress
    #             pay_obj.customerShippingState = instance.customerShippingState
    #             pay_obj.businessName = instance.businessName
    #             pay_obj.businessPhoneNumber = instance.businessPhoneNumber
    #             pay_obj.businessAddress1 = instance.businessAddress1
    #             pay_obj.businessAddress2 = instance.businessAddress2
    #             pay_obj.businessGSTIN = instance.businessGSTIN
    #             pay_obj.businessEmail = instance.businessEmail
    #             pay_obj.customerGSTIN = instance.customerGSTIN
    #             pay_obj.cust_bal_adj = instance.cust_bal_adj
    #             pay_obj.cust_bal_adj_type = instance.cust_bal_adj_type
    #             pay_obj.adj_bal = instance.adj_bal
    #             pay_obj.adj_bal_type = instance.adj_bal_type
    #             pay_obj.opening_bal = instance.opening_bal
    #             pay_obj.opening_bal_type = instance.opening_bal_type
    #             pay_obj.device = instance.device
    #             pay_obj.is_updated = True
    #             pay_obj.save()
    #             if len(payment["delRecpt"]) > 0:
    #                 for i in payment["delRecpt"]:
    #                     del_recpt = Payment.objects.get(ReceiptNo=i, tenant_id=tenant_new.id)
    #                     del_recpt.is_deleted = True
    #                     del_recpt.save(update_fields=['is_deleted'])
    #
    #     elif payment["Status"] == "Delete":
    #         try:
    #             pay_obj = Payment.objects.get(ReceiptNo=payment["ReceiptNo"], invoiceNo=0, tenant_id=tenant_new.id)
    #             pay_obj.is_deleted = True
    #             pay_obj.save()
    #             get_adjust = InvoiceAdjustment.objects.get(payment_id=int(payment['sync_id']),
    #                                                        invoiceNo=payment["invoiceNo"], tenant_id=tenant_new.id)
    #             get_adjust.is_deleted = True
    #             get_adjust.save()
    #             if len(payment["delRecpt"]) > 0:
    #                 for i in payment["delRecpt"]:
    #                     get_adjust = InvoiceAdjustment.objects.get(payment_id=i, invoiceNo=payment["invoiceNo"],
    #                                                                tenant_id=tenant_new.id)
    #                     get_adjust.is_deleted = True
    #                     get_recpt = Payment.objects.get(ReceiptNo=i, invoiceNo=payment["invoiceNo"],
    #                                                     tenant_id=tenant_new.id)
    #                     amtrcvd = abs(float(get_recpt.amountReceived) - float(get_adjust.adjustedAmount))
    #                     get_recpt.amountReceived = amtrcvd
    #                     get_recpt.save()
    #         except:
    #             pay_obj = Payment.objects.get(ReceiptNo=payment["ReceiptNo"], invoiceNo=payment["invoiceNo"],
    #                                           tenant_id=tenant_new.id)
    #             pay_obj.is_deleted = True
    #             pay_obj.save()
    #             if len(payment["delRecpt"]) > 0:
    #                 for i in payment["delRecpt"]:
    #                     del_recpt = Payment.objects.get(ReceiptNo=i, tenant_id=tenant_new.id)
    #                     del_recpt.is_deleted = True
    #                     del_recpt.save(update_fields=['is_deleted'])
    #
    #     elif payment["Status"] == "Insert":
    #         if instance.partPaymentFlag:
    #             id_max = Payment.objects.filter(tenant_id=tenant_new.id).aggregate(Max('ReceiptNo'))['ReceiptNo__max']
    #             id_next = id_max + 1 if id_max else 1
    #             Payment.objects.create(
    #                 invoiceNo=instance.invoiceNo, invoiceAmount=instance.saleBillAmount,
    #                 paymentMode=instance.salePaymentMode,
    #                 amountReceived=instance.salePaidAmount, ReceiptNo=id_next,
    #                 balanceAmount=instance.salePendingAmount, customerId=instance.customerId,
    #                 customerName=instance.customerName, customerEmail=instance.customerEmail,
    #                 customerPhoneNo=instance.customerPhoneNo,
    #                 customerBillingAddress=instance.customerBillingAddress,
    #                 customerBillingState=instance.customerBillingState,
    #                 customerShippingAddress=instance.customerShippingAddress,
    #                 customerShippingState=instance.customerShippingState, businessName=instance.businessName,
    #                 businessPhoneNumber=instance.businessPhoneNumber, businessAddress1=instance.businessAddress1,
    #                 businessAddress2=instance.businessAddress2, businessGSTIN=instance.businessGSTIN,
    #                 businessEmail=instance.businessEmail,
    #                 customerGSTIN=instance.customerGSTIN,
    #                 device=instance.device, tenant_id=tenant_new.id,
    #                 cust_bal=instance.cust_bal_adj,
    #                 cust_bal_type=instance.cust_bal_adj_type,
    #                 adj_bal=instance.adj_bal,
    #                 adj_bal_type=instance.adj_bal_type,
    #                 opening_bal=instance.opening_bal,
    #                 opening_bal_type=instance.opening_bal_type,
    #             )
    #         elif instance.fullPaymentFlag:
    #             id_max = Payment.objects.filter(tenant_id=tenant_new.id).aggregate(Max('ReceiptNo'))['ReceiptNo__max']
    #             id_next = id_max + 1 if id_max else 1
    #             Payment.objects.create(
    #                 invoiceNo=instance.invoiceNo, invoiceAmount=instance.saleBillAmount,
    #                 paymentMode=instance.salePaymentMode,
    #                 amountReceived=instance.salePaidAmount, ReceiptNo=id_next,
    #                 balanceAmount=instance.salePendingAmount, customerId=instance.customerId,
    #                 customerName=instance.customerName, customerEmail=instance.customerEmail,
    #                 customerPhoneNo=instance.customerPhoneNo,
    #                 customerBillingAddress=instance.customerBillingAddress,
    #                 customerBillingState=instance.customerBillingState,
    #                 customerShippingAddress=instance.customerShippingAddress,
    #                 customerShippingState=instance.customerShippingState, businessName=instance.businessName,
    #                 businessPhoneNumber=instance.businessPhoneNumber, businessAddress1=instance.businessAddress1,
    #                 businessAddress2=instance.businessAddress2, businessGSTIN=instance.businessGSTIN,
    #                 businessEmail=instance.businessEmail,
    #                 customerGSTIN=instance.customerGSTIN, device=instance.device, tenant_id=tenant_new.id,
    #                 cust_bal=instance.cust_bal_adj,
    #                 cust_bal_type=instance.cust_bal_adj_type,
    #                 adj_bal=instance.adj_bal,
    #                 adj_bal_type=instance.adj_bal_type,
    #                 opening_bal=instance.opening_bal,
    #                 opening_bal_type=instance.opening_bal_type,
    #             )
    #         elif instance.salePaymentType == "No Item":
    #             id_max = Payment.objects.filter(tenant_id=tenant_new.id).aggregate(Max('ReceiptNo'))['ReceiptNo__max']
    #             id_next = id_max + 1 if id_max else 1
    #             Payment.objects.create(
    #                 invoiceNo=instance.invoiceNo, invoiceAmount=instance.saleBillAmount,
    #                 paymentMode=instance.salePaymentMode,
    #                 amountReceived=instance.salePaidAmount, ReceiptNo=id_next,
    #                 balanceAmount=instance.salePendingAmount, customerId=instance.customerId,
    #                 customerName=instance.customerName, customerEmail=instance.customerEmail,
    #                 customerPhoneNo=instance.customerPhoneNo,
    #                 customerBillingAddress=instance.customerBillingAddress,
    #                 customerBillingState=instance.customerBillingState,
    #                 customerShippingAddress=instance.customerShippingAddress,
    #                 customerShippingState=instance.customerShippingState, businessName=instance.businessName,
    #                 businessPhoneNumber=instance.businessPhoneNumber, businessAddress1=instance.businessAddress1,
    #                 businessAddress2=instance.businessAddress2, businessGSTIN=instance.businessGSTIN,
    #                 businessEmail=instance.businessEmail,
    #                 customerGSTIN=instance.customerGSTIN, device=instance.device, tenant_id=tenant_new.id,
    #                 cust_bal=instance.cust_bal_adj,
    #                 cust_bal_type=instance.cust_bal_adj_type,
    #                 adj_bal=instance.adj_bal,
    #                 adj_bal_type=instance.adj_bal_type,
    #                 opening_bal=instance.opening_bal,
    #                 opening_bal_type=instance.opening_bal_type,
    #             )
    #
    #         if len(payment["delRecpt"]) > 0:
    #             for i in payment["delRecpt"]:
    #                 del_recpt = Payment.objects.get(ReceiptNo=i, tenant_id=tenant_new.id)
    #                 del_recpt.is_deleted = True
    #                 del_recpt.save(update_fields=['is_deleted'])
    #             # except:
    #             #     pass
    #     saleproduct_id = []
    #     for sale in add_sale:
    #         synch_id = sale.get('synch_id')
    #         print("syncid", synch_id)
    #         if synch_id is not None:
    #             sale_obj = SaleProduct.objects.get(id=int(synch_id), sale_id=instance.id, tenant_id=tenant_new.id)
    #             product = Product.objects.get(productId=sale_obj.productId, tenant_id=tenant_new.id)
    #             print(product.stockAvailable)
    #             old_qty = sale_obj.productQuantity
    #             new_qty = sale.get('productQuantity')
    #             print(new_qty)
    #             print(old_qty)
    #             saleproduct_id.append(int(synch_id))
    #             if new_qty > old_qty:
    #                 diff = abs(float(new_qty) - float(old_qty))
    #                 stkadj = float(product.stockAvailable) - float(diff)
    #                 if stkadj <= 0.0:
    #                     stkadj = 0.0
    #                 product.stockAvailable = stkadj
    #                 product.save(update_fields=['stockAvailable'])
    #             elif new_qty < old_qty:
    #                 diff = abs(float(new_qty) - float(old_qty))
    #                 stkadj = float(product.stockAvailable) + float(diff)
    #                 product.stockAvailable = stkadj
    #                 product.save(update_fields=['stockAvailable'])
    #             print(product.stockAvailable)
    #             sale_obj.productCode = sale.get('productCode', sale_obj.productCode)
    #             sale_obj.productHsnSacCode = sale.get('productHsnSacCode', sale_obj.productHsnSacCode)
    #             sale_obj.productName = sale.get('productName', sale_obj.productName)
    #             sale_obj.productUnit = sale.get('productUnit', sale_obj.productUnit)
    #             sale_obj.costPrice = sale.get('costPrice', sale_obj.costPrice)
    #             sale_obj.unitSalePrice = sale.get('unitSalePrice', sale_obj.unitSalePrice)
    #             sale_obj.stockAvailable = sale.get('stockAvailable', sale_obj.stockAvailable)
    #             sale_obj.gstPercent = sale.get('gstPercent', sale_obj.gstPercent)
    #             sale_obj.productQuantity = sale.get('productQuantity', sale_obj.productQuantity)
    #             sale_obj.gstAmount = sale.get('gstAmount', sale_obj.gstAmount)
    #             sale_obj.sellingPrice = sale.get('sellingPrice', sale_obj.sellingPrice)
    #             sale_obj.inclusiveOfGSTBoolean = sale.get('inclusiveOfGSTBoolean', sale_obj.inclusiveOfGSTBoolean)
    #             sale_obj.productServiceType = sale.get('productServiceType', sale_obj.productServiceType)
    #             sale_obj.subTotal = sale.get('subTotal', sale_obj.subTotal)
    #             sale_obj.totalSalePrice = sale.get('totalSalePrice', sale_obj.totalSalePrice)
    #             sale_obj.file_token = sale_obj.file_token
    #             sale_obj.messageState = sale.get('messageState', sale_obj.messageState)
    #
    #             sale_obj.save(
    #                 update_fields=['productCode', 'productHsnSacCode', 'productName', 'productUnit', 'costPrice',
    #                                'unitSalePrice', 'stockAvailable', 'gstPercent', 'productQuantity', 'gstAmount',
    #                                'sellingPrice', 'inclusiveOfGSTBoolean', 'productServiceType', 'subTotal',
    #                                'totalSalePrice', 'file_token', 'messageState'])
    #
    #         else:
    #             new_product = SaleProduct.objects.create(**sale, sale_id=instance.id, tenant_id=tenant_new.id)
    #             new_product.save()
    #             saleproduct_id.append(new_product.id)
    #
    #     print("saleproduct:", saleproduct_id)
    #     for sale in instance.addsale.all():
    #         if sale.id not in saleproduct_id:
    #             print(sale.id)
    #             sale.is_deleted = True
    #             sale.save()
    #
    #     exchrg_id = []
    #     for charge in ex_charge:
    #         synch_id = charge.get('synch_id')
    #         if synch_id is not None:
    #             charge_obj = ExtraCharges.objects.get(id=synch_id, tenant_id=tenant_new.id)
    #             charge_obj.invoiceNo = charge.get('invoiceNo', charge_obj.invoiceNo)
    #             charge_obj.xtraAmnt = charge.get('xtraAmnt', charge_obj.xtraAmnt)
    #             charge_obj.xtraNam = charge.get('xtraNam', charge_obj.xtraNam)
    #             charge_obj.save(update_fields=['invoiceNo', 'xtraAmnt', 'xtraNam'])
    #             exchrg_id.append(synch_id)
    #         else:
    #             new_charge = ExtraCharges.objects.create(**charge, extraChargeList_id=instance.id,
    #                                                      tenant_id=tenant_new.id)
    #             new_charge.save()
    #             exchrg_id.append(new_charge.id)
    #
    #     for charge in instance.extraChargeList.all():
    #         if charge.id not in exchrg_id:
    #             charge.is_deleted = True
    #             charge.save()
    #     print(messageState)
    #     if messageState == "TRUE":
    #         sale = Sale.objects.get(id=instance.id, tenant_id=tenant_new.id)
    #         url = "https://{}.vasoolbooksandbox.in/invoice/{}".format(tenant_new.schema_name, sale.file_token)
    #         res = send_editsale(invoice=url, mobile=customer_phone, type="Invoice",
    #                             businessname=business_name, businessno=business_no)
    #
    #     return instance
