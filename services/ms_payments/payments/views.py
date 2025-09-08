import json
import requests

from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response

from payments.payments_data import PaymentsData


class PaymentView(APIView):
    def get(self, request, payment_id):
        payments_db = PaymentsData()

        payment = payments_db.get_payment(payment_id)
        if not payment:
            return Response({"error": "Payment not found"}, status=404)

        # Call Order Service
        try:
            _url = f"{settings.URL_MS_ORDERS}/{payment['order_id']}"
            resp = requests.get(_url)
            # safer parse
            order_data = json.loads(resp.content.decode("utf-8"))   # bytes → string → dict
        except Exception as e:
            print("Error: ", str(e))
            return Response({"error": f"Order service failed: {str(e)}"}, status=500)

        return Response({
            "payment_id": payment_id,
            "amount": payment["amount"],
            "order": order_data
        })

