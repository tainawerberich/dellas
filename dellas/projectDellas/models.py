from django.db import models
from projectDellas.models import ferias

def my_view(request):
    objects = ferias.objects.all()

# Create your models here.
