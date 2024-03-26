from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class CustomUser(AbstractUser):
    user_type_data= ((1,"HOD"), (2,"Staff"), (3, "Student"))
    user_type= models.CharField(default=1, choices=user_type_data, max_length=10)
    
class AdminHOD(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager


class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser,on_delete = models.CASCADE)
    address = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    
class Grade(models.Model):
    id = models.AutoField(primary_key=True)
    grade_name= models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class Cname(models.Model):
    id = models.AutoField(primary_key=True)
    class_name= models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=255)
    grade_id = models.ForeignKey(Grade, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(Staff,on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class Students(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    gender = models.CharField(max_length=255)
    profile_pic = models.FileField()
    address = models.CharField(max_length=255)
    grade_id = models.ForeignKey(Grade, on_delete= models.DO_NOTHING)
    class_id = models.ForeignKey(Cname, on_delete= models.DO_NOTHING)
   # session_start_year = models.DateField()
   # session_end_year = models.DateField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    name= models.CharField(max_length=255)
    kha_reg_date= models.DateField()
    student_id= models.CharField(max_length=250)
    school_attended= models.CharField(max_length=255)
    grade_attended= models.CharField(max_length=255)
    year_attended= models.DateField()
    dob=models.DateField()
    pob=models.CharField(max_length=255)
    nrc=models.CharField(max_length=255)
    nationality= models.CharField(max_length=255)
    religion= models.CharField(max_length=255)
    academic_year= models.DateField()
    father_name= models.CharField(max_length=255)
    f_nrc=models.CharField(max_length=255)
    f_qulification=models.CharField(max_length=255)
    f_job=models.CharField(max_length=255)
    f_phone=models.IntegerField()
    f_address=models.CharField(max_length=255)
    f_aorp=models.CharField(max_length=255)
    mother_name= models.CharField(max_length=255)
    m_nrc=models.CharField(max_length=255)
    m_qulification=models.CharField(max_length=255)
    m_job=models.CharField(max_length=255)
    m_phone=models.IntegerField()
    m_address=models.CharField(max_length=255)
    m_aorp=models.CharField(max_length=255)
    guradian_name= models.CharField(max_length=255)
    g_nrc=models.CharField(max_length=255)
    g_qulification=models.CharField(max_length=255)
    g_job=models.CharField(max_length=255)
    g_phone=models.IntegerField()
    g_address=models.CharField(max_length=255)
    st_comment=models.CharField(max_length=255)



    objects = models.Manager()
    
    
class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    subject_id = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    attendance_date = models.DateTimeField(auto_now_add=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class AttendanceReport(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.DO_NOTHING)
    attendance_id = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class LeaveReportStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students,on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=255)
    leave_message = models.TextField( max_length=255)
    leave_status = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    



class LeaveReportStaff(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staff,on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=255)
    leave_message = models.TextField( max_length=255)
    leave_status = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class FeedBackStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students,on_delete=models.CASCADE)
    feedback = models.CharField(max_length=255)
    feedback_reply = models.TextField()
    leave_status = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class FeedBackStaff(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staff,on_delete=models.CASCADE)
    feedback = models.CharField(max_length=255)
    feedback_reply = models.TextField()
    leave_status = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
   

class NotificationStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students,on_delete=models.CASCADE)
    message = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    

class NotificationStaff(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staff,on_delete=models.CASCADE)
    message = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()



@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created,**kwargs):
    if created:
        if instance.user_type==1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type==2:
            Staff.objects.create(admin=instance,address="")
        if instance.user_type==3:
            Students.objects.create(admin=instance)


@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.adminhod.save() 
    if instance.user_type==2:
        instance.staff.save()       
    if instance.user_type==3:
        instance.students.save()