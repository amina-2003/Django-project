from django.contrib import admin
from .models import Role, Region, Utilisateur, Categorie, Service, Profile, Portfolio

admin.site.register(Role)
admin.site.register(Region)
admin.site.register(Utilisateur)
admin.site.register(Categorie)
admin.site.register(Service)
admin.site.register(Profile)
admin.site.register(Portfolio)