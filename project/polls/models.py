from django.db import models

# Create your models here.

class Deskripsi(models.Model):
    keterangan = models.CharField(max_length=200)

    def __str__(self):
        return self.keterangan

class Barang(models.Model):
    nama = models.CharField(max_length=200)
    harga = models.IntegerField(default=0)
    deskripsi = models.ForeignKey(Deskripsi, on_delete=models.CASCADE)
    foto = models.CharField(max_length=200)

    def __str__(self):
        return self.nama
