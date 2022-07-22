from django.db import models


class ImageAlbum(models.Model):
    def default(self):
        return self.images.filter(default=True).first()

    def thumbnails(self):
        return self.images.filter(width__lt=100, length_lt=100)

    def __str__(self):
        if self.images.all():
            return self.images.all()[0].name + " Album"
        else:
            return "Empty Image Album"


class Image(models.Model):
    image_url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=255)
    album = models.ForeignKey(ImageAlbum, related_name='images', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

