from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Film)
admin.site.register(Hall)

admin.site.register(Seance)
