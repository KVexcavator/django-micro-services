from django.views import View
from subscription.mongo_models.address import Address
from django.http import JsonResponse, HttpResponseNotFound, HttpResponse
from pydantic import ValidationError
from beanie import PydanticObjectId, WriteRules
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
            await address.insert(link_rule=WriteRules.WRITE)
            return HttpResponse(address.model_dump_json(), content_type="application/json", status=201)
        except ValidationError as e:
            return JsonResponse({"errors": e.errors()}, status=422)
        
class AsyncAddressDetailView(CSRFExemptMixin, View):
    async def get(self, request, address_id):
        try:
            obj_id = PydanticObjectId(address_id)
            address = await Address.get(obj_id)

            if not address:
                return HttpResponseNotFound("Address not found")
            
            response_data = address.model_dump()
            response_data["id"] = str(address.id)
            return JsonResponse(response_data, safe=False)
        except Exception as e:
            return HttpResponseNotFound("Invalid ID or address not found")

    async def put(self, request, address_id):
        try:
            obj_id = PydanticObjectId(address_id)
            address = await Address.get(obj_id)
            if not address:
                return HttpResponseNotFound("Address not found")
            
            data = json.loads(request.body)
            updated_fields = {
                k: v for k, v in data.items() if v is not None
            }

            await address.update({"$set": updated_fields})  

            response_data = address.model_dump()
            response_data["id"] = str(address.id)
            return JsonResponse(response_data, safe=False)
        except ValidationError as e:
            return JsonResponse({"errors": e.errors()}, status=422)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    async def delete(self, request, address_id):
        try:
            obj_id = PydanticObjectId(address_id)
            address = await Address.get(obj_id)
            if not address:
                return HttpResponseNotFound("Address not found")
            await address.delete()
            return JsonResponse({"message": "Address deleted successfully"}, status=200)
        except Exception as e:
            return JsonResponse({"error": "Invalid ID or address not found"}, status=404)
