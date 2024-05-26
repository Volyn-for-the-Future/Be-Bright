from django.db import models

# Create your models here.

class Themes(models.Model):
    id = models.IntegerField(primary_key=True)
    theme = models.CharField(max_length=100)

class Materials(models.Model):
    id = models.IntegerField(primary_key=True)
    material_text = models.TextField(null=True, blank=True)
    material_links = models.TextField(null=True, blank=True)
    theme = models.ForeignKey(Themes, on_delete=models.SET_NULL, null=True, blank=True, related_name='theme')

class MaterialsFiles(models.Model):
    file = models.FileField(upload_to="files/%Y/%m/%d")
    material = models.ForeignKey(Materials, on_delete=models.CASCADE, related_name='files')

class Teachers(models.Model):
    id = models.IntegerField(primary_key=True)
    surname = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    second_name = models.CharField(max_length=40, null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    # password = models.OneToOneField('TeachersLogin', on_delete=models.CASCADE)
    date_of_birth = models.DateField(auto_now=False,auto_now_add=False)
    date_of_creation = models.DateField(auto_now=False,auto_now_add=True)
    address = models.CharField(max_length=200)
    # Achivment
