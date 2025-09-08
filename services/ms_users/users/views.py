from rest_framework.views import APIView
from rest_framework.response import Response

from users.users_data import UsersData

class UserView(APIView):
    def get(self, request, user_id):
        users_db = UsersData()

        result = {
                    "user_id": user_id,
                    "name": users_db.get_user(user_id)
                  }
        return Response(result)

