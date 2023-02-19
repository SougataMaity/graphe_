
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class create_movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length=200)
    movie_duration = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "New Movie"


gen_choice = (
    (0, "Male"),
    (1, "Female")
)

# from datetime import timedelta
time = "00:00:00"

class casts_details(models.Model):
    
    # cast_id = models.AutoField(primary_key=True)
    movie_info = models.ForeignKey(create_movie, on_delete=models.CASCADE)
    cast_name = models.CharField(max_length=300)
    cast_gender = models.BooleanField(choices=gen_choice)
    cast_character = models.CharField(max_length=500)
    dialouge = models.CharField(max_length=100)
    start_time = models.DurationField(default=time)
    end_time = models.DurationField(default=time)

    class Meta:
        verbose_name_plural = "Cast and Dialouge"
    

