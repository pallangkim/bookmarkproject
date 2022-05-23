from django.contrib import admin
from .models import Bookmark

# Register your models here.
# 아래 문구를 활용하여 관리자 페이지에서 해당 모델 관리
admin.site.register(Bookmark)