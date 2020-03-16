from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


class mysqlImage(models.Model):
    mid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    letters = models.CharField(max_length=100)
    isdelete = models.IntegerField(default=0)
    addtime = models.DateTimeField(auto_now_add=True)
    modifytime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_ocr_letters'  # 数据表名称
