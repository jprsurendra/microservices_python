import json

import requests  # To call user_service

from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response

from orders.orders_data import OrdersData


class OrderView(APIView):
    def get(self, request, order_id):
        # Fake orders
        orders_db = OrdersData()
        order = orders_db.get_order(order_id)
        if not order:
            return Response({"error": "Order not found"}, status=404)

        try:
            _url = f"{settings.URL_MS_USERS}/{order['user_id']}"
            resp = requests.get(_url)
            # safer parse
            user_data = json.loads(resp.content.decode("utf-8"))
            # user_data = json.loads(resp.content.decode("utf-8"))  # bytes → string → dict
        except Exception as e:
            return Response({"error": f"User service failed: {str(e)}"}, status=500)

        result = {
            "order_id": order_id,
            "item": order["item"],
            "user": user_data
        }

        return Response(result, status=200)