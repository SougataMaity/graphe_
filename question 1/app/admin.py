
from django.contrib import admin
from app.models import create_movie, casts_details

## admin components
admin.site.site_header  =  "Ok Movies" 
admin.site.site_title  =  "Ok Movies admin site"
admin.site.index_title  =  "Click and Create Movie"

# Model view
class CastAdmin(admin.ModelAdmin):
  list_display = ['movie_info','cast_name', 'cast_gender','cast_character','dialouge','start_time','end_time']
  fields = ['movie_info', 'cast_name', 'cast_gender','cast_character','dialouge','start_time','end_time']

  search_fields = ['cast_name', 'cast_gender', 'dialouge']

class ModelInline(admin.StackedInline):
    model = casts_details
    extra = 0

class MovieAdmin(admin.ModelAdmin):
    model = create_movie
    list_display = ['movie_name', 'movie_duration']
    inlines = [
        ModelInline,
    ]

admin.site.register(create_movie, MovieAdmin)
admin.site.register(casts_details, CastAdmin)


##




