import json
from django.http    import JsonResponse
from django.views   import View
from product.models import Product


class ProductView(View):

    def post(self, request):
        print(request.body)
        data =json.loads(request.body)
        print(data)

        Product.objects.create(
            name        = data["name"],
            price       = data["price"],
            description = data["description"],
            image_url   = data["image_url"]
        )
        return JsonResponse({"message":"SUCESS"}, status=201)

    def get(self, request, product_id):
        product = Product.objects.get(id=product_id)
        result = {
                "name"          : product.name,
                "price"         : product.price,
                "description"   : product.description,
                "image_url"     : product.image_url
        }
        return JsonResponse({'result':result}, status=200)





   

