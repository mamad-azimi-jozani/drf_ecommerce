from .models import *

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view()
def product_list(request):
    data = {
        "product": "niva",
        "quantity": 5
    }
    return Response(data)

@api_view()
def product_detail(request, id):
    data = {
        "product": "niva",
        "quantity": id
    }
    return Response(data)
