# -*- coding: utf-8 -*-
from __future__ import unicode_literals


#polskie znaki
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#polskie znaki





from django.contrib import admin

from apka.models import Topic, Entry, Newsletter

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Newsletter)

# Register your models here.
