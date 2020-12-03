from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):

    def get(self, request, format=None):
        an_apiview = [
            'Uses HTTP methods as function(get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you most contorl over application logic,',
            'Is maped '
        ]

        return Response({'message' : 'Heloo', 'an_apiview': an_apiview})