# from utilities.mixins import ResponseViewMixin
from rest_framework.views import APIView
from django.http import HttpResponse
import datetime

class ListSongsView(APIView):
    """
    Provides a get method handler.
    """
    def get(self, request):
        # now = datetime.datetime.now()

        print("--------------------------------------------")
        html = "<html><body>-------------------------------------</body></html>"
        return HttpResponse(html)
