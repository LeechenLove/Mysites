from django.db import models

# Create your models here.

#Event.objects.create(name="IPhone11发布会",limit=2000,status=True,address="广州",start_time="2019-12-25 14:00:00")
#Guest.objects.create(realname="张三",phone="18819414657",email='test@qq.com',sign=False,event_id=2)
class Event(models.Model):
    """
    发布会表
    """
    name = models.CharField(max_length=100)            # 发布会标题
    limit = models.IntegerField()                      # 限制人数
    status = models.BooleanField()                     # 状态
    address = models.CharField(max_length=200)         # 地址
    start_time = models.DateTimeField('events time')   # 发布会时间
    create_time = models.DateTimeField(auto_now=True)  # 创建时间（自动获取当前时间）

    def __str__(self):
        return self.name



class Guest(models.Model):
    """
    嘉宾表
    """
    event = models.ForeignKey(Event, on_delete=models.CASCADE)  # 关联发布会id
    realname = models.CharField(max_length=64)  # 姓名
    phone = models.CharField(max_length=16)     # 手机号
    email = models.EmailField()                 # 邮箱
    sign = models.BooleanField()                # 签到状态
    create_time = models.DateTimeField(auto_now=True)  # 创建时间（自动获取当前时间）

    # class Meta:
    #     unique_together = ('phone', 'event')
    #     ordering = ['-id']

    # def __str__(self):
    #     return self.realname