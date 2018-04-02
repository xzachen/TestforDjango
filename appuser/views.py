#coding=utf-8
from django.http import HttpResponse,JsonResponse,StreamingHttpResponse,FileResponse
from appuser.models import User,Course,Note
from appuser.Serializer import UserSerializer,CourseSerializer
from rest_framework.renderers import JSONRenderer
from django.core import serializers
from django.db.models import Q
import json,os
import ast


# from django.forms.models import model_to_dict
# 路由的处理方法在这里。
def index(request):
    return HttpResponse('Test..user')


# 登录注册都是POST方法来处理的。
# 400代表空，200代表oK,500代表重复。
# 用户登录的事件处理/测试成功
def login(request):
    # 考虑到出错的可能性，一开始就设置为
    context = {'status': 400, 'content': 'null'}
    if request.method == "POST":
        username = request.POST.get('username', )
        password = request.POST.get('password')
        try:
            user = User.maneger.get(username=username, password=password)
            context['status'] = 200
        except:
            context['status'] == 400
        if context['status'] == 200:
            serializer = UserSerializer(user)
            context['content'] = serializer.data
        else:
            context['content'] = "null"
        content = JSONRenderer().render(context)
        return HttpResponse(content)
    return HttpResponse(JSONRenderer().render(context))


# 用户注册的事件处理
# 用户注册和登录
# 用户名字或者QQ号码被绑定的话返回500.这里采用了Q对象
# 测试成功
def register(request):
    context = {'status': 400}
    if request.method == "POST":
        # 获取到对象，之后序列化
        username = request.POST.get('username')
        password = request.POST.get('password')
        QQnumber = request.POST.get('QQnumber')
        QQname = request.POST.get('QQname')
        try:
            testuser = User.maneger.filter(Q(username=username) | Q(QQnumber=QQnumber))
            if testuser:
                context['status'] = 500
            else:
                user = User.maneger.create(username, password, QQnumber, QQname)
                user.save()
                context['status'] = 200
        except Exception:
            context['status'] == 400
        return HttpResponse(JSONRenderer().render(context))
    return HttpResponse(JSONRenderer().render(context))


def RetrievePassword(request):
    pass


# 这个方法目前还有问题校留着、未测试
# 用户可能第一次就使用了QQ登录而没有注册 所以应该判断一下
def registerOrNot(request,QQnumber):
    context={'status':400}
    if request.method == "GET":
        try:
           user=User.maneger.get(QQnumber=QQnumber)
           if user.isbinding==1:
               context['status']=500
           # 未绑定QQ号码
           elif user.isbinding==0:
               context['status']=200
        except Exception:
            context['status']=400
        return HttpResponse(JSONRenderer().render(context))
    return HttpResponse(JSONRenderer().render(context))


# 以下是课程的增删改查
#查询用户的所有课程信息
def querycourseinfo(request,uid):
    context = {'status': 400,'content':"null"}
    if request.method == "GET":
        try:
            course = Course.manager.filter(uid=uid)
            #查询集为空时候
            if course.count()== 0:
                print('yes')
            else:
                context['status'] = 200
                serialize= serializers.serialize("json",course)
                # 这里先将json对象转化为列表进行存储缺少这一步的话将无法解析。
                context['content'] = json.loads(serialize)
        except Exception:
            context['status'] = 400
        return HttpResponse(JSONRenderer().render(context))
    return HttpResponse(JSONRenderer().render(context))

# 更新通过id得到课程信息并进行更新。状态码200表示成功/测试成功
def updatecourseInfo(request):
    context = {'status': 400}
    if request.method == "POST":
        # 获取到对象，之后序列化
        cid = request.POST.get('cid')
        cname =request.POST.get('cname')
        schoolYear = request.POST.get('schoolYear')
        term = request.POST.get('term')
        credit = request.POST.get('credit')
        intstartSection =request.POST.get('credit')
        endSection = request.POST.get('endSection')
        startWeek = request.POST.get('startWeek')
        endWeek = request.POST.get('endWeek')
        dayOfWeek = request.POST.get('dayOfWeek')
        classroom = request.POST.get('classroom')
        teacher = request.POST.get('teacher')
        try:
            course =Course.manager.get(cid=cid)
            course.cname = cname
            course.schoolYear = schoolYear
            course.term = term
            # 注意类型的转化
            data= ast.literal_eval(credit)
            course.credit =data
            course.intstartSection = intstartSection
            course.endSection = endSection
            course.startWeek = startWeek
            course.endWeek = endWeek
            course.dayOfWeek = dayOfWeek
            course.classroom = classroom
            course.teacher = teacher
            course.save()
            context['status']=200
        except Exception as e:
            print(e)
            context['status'] == 400
        return HttpResponse(JSONRenderer().render(context))
    return HttpResponse(JSONRenderer().render(context))

#创建课程的信息/测试成功
def createCourse(request):
    context = {'status': 400}
    if request.method == "POST":
        # 获取到对象，之后序列化
        uid = request.POST.get('uid')
        cname = request.POST.get('cname')
        schoolYear = request.POST.get('schoolYear')
        term = request.POST.get('term')
        credit = request.POST.get('credit')
        intstartSection = request.POST.get('credit')
        endSection = request.POST.get('endSection')
        startWeek = request.POST.get('startWeek')
        endWeek = request.POST.get('endWeek')
        dayOfWeek = request.POST.get('dayOfWeek')
        classroom = request.POST.get('classroom')
        teacher = request.POST.get('teacher')
        try:
            user = User.maneger.get(userid=uid)
            if user:
                course=Course.manager.create(cname,schoolYear,term,credit,intstartSection,endSection,startWeek,endWeek,dayOfWeek,classroom,teacher)
                course.uid_id=user.userid
                course.save()
                context['status'] = 200
            else:
                context['status']=400
        except Exception as e:
            print(e)
            context['status'] == 400
        return HttpResponse(JSONRenderer().render(context))
    return HttpResponse(JSONRenderer().render(context))

# 删除课程信息/测试成功
def deleteCourse(request,cid):
    context = {'status': 400}
    if request.method == "GET":
        try:
            course = Course.manager.get(cid=cid)
            # 查询集为空时候
            if course:
                course.delete()
                context['status'] = 200
            else:
                context['status'] = 400
        except Exception:
            context['status'] = 400
        return HttpResponse(JSONRenderer().render(context))
    return HttpResponse(JSONRenderer().render(context))

# 上传用户的文件/测试成功
def uploadfile(request):
    context = {'status': 400}
    if request.method == "POST":
        try:
            uid = request.POST.get('uid')
            user = User.maneger.get(userid=uid)
            instance = Note(content=request.FILES['filename'])  # 保存文件到FileField域
            instance.uid_id=user.userid
            instance.save()
            context['status'] = 200
        except Exception as e:
            print(e)
            context['status'] = 400
        return HttpResponse(JSONRenderer().render(context))
    return HttpResponse(JSONRenderer().render(context))


# 实现文件的下载
# def download(request):
#     uid = request.POST.get('uid')
#     resource = Note.objects.filter(uid=uid)
#     print(resource)
#     # print(type(resource.content))
#     # print(str(resource.content))
#     # # 从当前文件路径中获取文件名
#     # the_file_name=os.path.basename(os.path.realpath(str(resource.content)))
#     # print(the_file_name)
#
#     def file_iterator(filename, chunk_size=512):
#         with open(filename,'w') as f:
#             while True:
#                 c = f.read(chunk_size)
#                 if c:
#                     yield c
#                 else:
#                     break
#
#     # response = StreamingHttpResponse(file_iterator(the_file_name))
#     # response['Content-Type'] = 'application/octet-stream'
#     # response['Content-Disposition'] = 'attachment; filename=' + the_file_name.encode('utf-8') # 设定传输给客户端的文件名称
#     # response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(escape_uri_path(the_file_name))
#     return HttpResponse('hello ')
#
#
# def download(request):
#     uid = request.POST.get('nid')
#     resource = Note.objects.get(nid=uid)
#     file = open(str(resource.content), 'rb')
#     response = FileResponse(file)
#     response['Content-Type'] = 'application/octet-stream'
#     response['Content-Disposition'] = 'attachment;filename="example.tar.gz"'
#     return response

def download(request):
    def file_iterator(file_name, chunk_size=512):#用于形成二进制数据
        with open(file_name,'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    the_file_name ='files\\user_User object (2)\\app.png'#要下载的文件路径
    response =StreamingHttpResponse(file_iterator(the_file_name))#这里创建返回
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="example.tar.gz"'
    # response['Content-Type'] = 'application/octet-stream'#注意格式
    # response['Content-Disposition'] = 'attachment;filename=%s'%the_file_name
    #注意filename 这个是下载后的名字
    return response