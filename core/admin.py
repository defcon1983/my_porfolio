from django.contrib import admin
from .models import Welcome, Project, Skill, Contact, Social_network, My_data

# Register your models here.

admin.site.register(Welcome)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Contact)
admin.site.register(Social_network)
admin.site.register(My_data)

