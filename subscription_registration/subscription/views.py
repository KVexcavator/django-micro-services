# # subscription/views.py
from django.views import View
from subscription.mongo_models.address import Address
from django.http import HttpResponse, JsonResponse
from pydantic import ValidationError
import json
from subscription.utils.mixins import CSRFExemptMixin

class AsyncAddressListCreateView(CSRFExemptMixin, View):
    async def get(self, request):
        addresses = await Address.find_all().to_list()
        data = "[" + ",".join([a.model_dump_json() for a in addresses]) + "]"
        return HttpResponse(data, content_type="application/json")

    async def post(self, request):
        try:
            body = json.loads(request.body)
            address = Address(**body)
            await address.insert()
            return HttpResponse(address.model_dump_json(), content_type="application/json", status=201)
        except ValidationError as e:
            return JsonResponse({"errors": e.errors()}, status=422)
