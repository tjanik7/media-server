from rest_framework.response import Response
from rest_framework.views import APIView

class FirstView(APIView):
    def get(self, request):
        return Response("hi there; that worked")

