from django.contrib import admin

from api.models import Company
from api.models import Vacancy

admin.site.register(Company)
admin.site.register(Vacancy)
