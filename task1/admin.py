# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Language
from .models import Application
from .models import Website
from .models import Product
from .models import Contact
from .models import Profession
# Register your models here.


admin.site.register(Language)
admin.site.register(Application)
admin.site.register(Website)
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Profession)
