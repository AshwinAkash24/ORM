from django.db import models
from django.contrib import admin
class Book_DB(models.Model):
    slno=models.IntegerField(primary_key="slno");
    bname=models.CharField(max_length=50);
    author=models.CharField(max_length=20);
    published_date=models.DateField();
    prize=models.IntegerField();
class Book_DBAdmin(admin.ModelAdmin):
	list_display=("slno", "bname", "author", "published_date", "prize");
