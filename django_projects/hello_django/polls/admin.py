from django.contrib import admin
from polls.models import Question, Choice

# Register your models here.
admin.site.register(Question) # Registrando um CRUD para Question
admin.site.register(Choice)
