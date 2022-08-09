from django.shortcuts import render
from django.conf import settings
from store.models.image import Image, ImageAlbum
from store.form.product import UploadProductForm
import os


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
                if image:
                    print("Successfully uploaded image, it's location is: " + str(image))
                    context = {
                        'image': image,
                    }
                    return render(request, 'upload_product.html', context)
        form = UploadProductForm()
    except Exception as e:
        print(e, flush=True)
    context = {
                'form': form,
    }
    return render(request, 'upload_product.html', context)
