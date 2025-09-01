
from rest_framework.views import APIView
from rest_framework.response import Response


class UserView(APIView):
    def get(self, request, user_id):
        users = {"1": "Alice", "2": "Bob", "3": "Charlie"}

        return Response({"user_id": user_id, "name": users.get(user_id, "Unknown")})
