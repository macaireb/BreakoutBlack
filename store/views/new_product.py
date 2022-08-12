import os

from django.conf import settings
from django.shortcuts import render
from django.views.generic import View

from store.form.product import UploadProductForm, NewCategory
from store.models.image import Image, ImageAlbum
from store.models.product import Category


def new_product_view(request):
    print("USE S3: " + os.getenv("USE_S3") + "USE LOCAL: " + os.getenv("LOCAL_DEVELOPMENT"))
    try:
        if request.method == "GET":
            form = UploadProductForm()
            context = {
                'form': form
            }
            print("Sent form: " + str(type(form.description)))
            return render(request, 'upload_product.html', context)
        if request.method == "POST":
            album = ImageAlbum.objects.create()
            album.save()
            image_file = request.FILES["item_image"]
            print(settings.USE_S3)
            if settings.USE_S3:
                image = Image.objects.create(file=image_file, album=album)
                image.save()
                product_form = UploadProductForm(request.POST)
                if product_form.is_valid():
                    print("Form is valid")
                    product = product_form.save()
                    product.image_url = image.file.url
                    product.album = album
                    product.save()
                if image:
                    print("Successfully uploaded image, it's location is: " + str(image))
                    context = {
                        'image': image,
                    }
                    return render(request, 'upload_product.html', context)
                if product:
                    print("Successfully uploaded image, it's location is: " + str(product))
                    context = {
                        'product': product,
                    }
                    return render(request, 'upload_product.html', context)
        form = UploadProductForm()
    except Exception as e:
        print(e, flush=True)
        form = UploadProductForm()
    context = {
        'form': form,
    }
    return render(request, 'upload_product.html', context)


class AddCategory(View):
    def get(self, *args, **kwargs):
        categories = Category.objects.all()
        form = NewCategory()
        context = {
            'form': form,
        }
        if categories:
            context.update({'categories': categories})
        return render(self.request, 'new category.html', context)
