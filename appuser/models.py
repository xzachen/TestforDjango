from django.db import models


# Create your models here.

# 创建模型的管理类
class UserManager(models.Manager):
    def create(self, username, password, QQnumber, QQname):
        user = User()
        user.username = username
        user.password = password
        user.QQnumber = QQnumber
        user.QQname = QQname
        user.isbinding = 1
        return user

# 创建自己的模型类。
class User(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=40)
    QQnumber = models.CharField(max_length=20, unique=True)
    QQname = models.CharField(max_length=20)
    isbinding = models.IntegerField(default=0)

    # 创建元数据
    class Meta:
        ordering = ['userid']
        # 设置表名字
        db_table = 'user'

    maneger = UserManager()

class CourseManager(models.Manager):
    def create(self, cname, schoolYear,term, credit,intstartSection,endSection,startWeek,endWeek,dayOfWeek,classroom,teacher):
        course = Course()
        course.cname = cname
        course.schoolYear = schoolYear
        course.term = term
        course.credit = credit
        course.intstartSection = intstartSection
        course.endSection = endSection
        course.startWeek = startWeek
        course.endWeek = endWeek
        course.dayOfWeek = dayOfWeek
        course.classroom = classroom
        course.teacher = teacher
        return course

# 创建课程类的model
class Course(models.Model):
    uid = models.ForeignKey('User',on_delete=models.CASCADE,)
    cid = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=20)
    schoolYear = models.CharField(max_length=20)
    term = models.CharField(max_length=20)
    credit = models.FloatField()
    intstartSection = models.IntegerField()
    endSection = models.IntegerField()
    startWeek = models.IntegerField()
    endWeek = models.IntegerField()
    dayOfWeek = models.IntegerField()
    classroom = models.CharField(max_length=20)
    teacher = models.CharField(max_length=20)

    class Meta:
        ordering = ['cid']
        # 设置表名字
        db_table = 'course'
    # 创建管理类。
    manager=CourseManager()
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'files/user%s/%s'%(instance.uid, filename)
class Note(models.Model):
    nid=models.AutoField(primary_key=True)
    uid = models.ForeignKey('User', on_delete=models.CASCADE, )
    content=models.FileField(upload_to=user_directory_path)#设置上传的文件路径名字

    class Meta:
        ordering = ['nid']
        # 设置表名字
        db_table = 'note'
