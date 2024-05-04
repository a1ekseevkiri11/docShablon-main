import os
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


from registration.models import Profile

class AbstractSupervisor(Profile):
    post = models.CharField(max_length=256)
    class Meta:
        abstract = True

    def __str__(self):
        return self.post + " " + self.get_short_fio()

class SupervisorOPOP(AbstractSupervisor):
    pass


class SupervisorPractice(AbstractSupervisor):
    pass


class Institute(models.Model):


    title = models.CharField(max_length=256, unique=True)


    def __str__(self):
        return self.title
    

class DirectionOfTraining(models.Model):
    

    title = models.CharField(max_length=256)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE,)
    supervisorOPOP = models.ForeignKey(SupervisorOPOP, on_delete=models.CASCADE,)

    def __str__(self):
        return self.title
    

class Group(models.Model):


    level_choices = (
        ('Bachelor', 'Бакалавриат'),
        ('Specialist', 'Специалитет'),
        ('Master', 'Магистратура'),
        ('PhD', 'Аспирантура'),
    )

    form_of_education_choices = (
        ('full-time', 'очная'),
        ('part-time', 'очно-заочная'),
        ('extramural', 'заочная'),
    )

    title = models.CharField(max_length=10)
    direction_of_training = models.ForeignKey(DirectionOfTraining, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=level_choices)
    year = models.PositiveIntegerField()
    specialty_code = models.CharField(max_length=12)
    specialty_name = models.CharField(max_length=512)
    form_of_education = models.CharField(max_length=512, choices=form_of_education_choices)
    group_gid = models.CharField(max_length=128)


    def __str__(self):
        return self.title
    

class Student(Profile):
    state_choices = (
        ('no', 'нет'),
        ('part-time', 'декретный отпуск'),
        ('extramural', 'академический отпуск'),
    )
    
    group =  models.ForeignKey(Group, on_delete=models.CASCADE)
    state = models.CharField(max_length=512, default='no', choices=state_choices)


class Amount(models.Model):

    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title
    

    
class Practice(models.Model):


    type_choices = (
        ('type1', 'преддипломная'),
        ('type2', 'ознакомительная'),
        ('type3', 'технологическая'),
        ('type4', 'производственна'),
        ('type5', 'научно-исследовательская'),
    )

    kind_choices = (
        ('kind1', 'учебная'),
        ('kind2', 'производственная'),
    )


    title = models.CharField(max_length=512, unique=True)
    group = models.ManyToManyField(Group)
    type = models.CharField(max_length=20, choices=type_choices)
    kind = models.CharField(max_length=20, choices=kind_choices)
    date_start = models.DateField()
    date_end = models.DateField()

    #документ
    number_decree = models.CharField(max_length=20)
    date_decree = models.DateField()

    #адрес
    title_place = models.CharField(max_length=512)
    adress_place = models.CharField(max_length=512)

    #связь руководителей практики
    supervisor_practice = models.ForeignKey(SupervisorPractice, on_delete=models.SET_NULL, null=True)

    #руководителя от ЮГУ
    fio_supervisor_YuSU = models.CharField(max_length=512)
    post_supervisor_YuSU = models.CharField(max_length=512)

    #руководитель от организации
    fio_supervisor_company = models.CharField(max_length=512, null=True)
    post_supervisor_company = models.CharField(max_length=512, null=True)

    def __str__(self):
        return self.title
    

class ReportGroup(models.Model):
    title = models.TextField()
    practice = models.ForeignKey(Practice, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    

class PracticeStudent(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    practice = models.ForeignKey(Practice, on_delete=models.CASCADE)
    
    def __str__(self):
        return "Отчет " + self.practice.title
    


class StudentProductionTasks(models.Model):
    
    title = models.CharField(max_length=512)
    data = models.DateField()
    practice_student = models.ForeignKey(PracticeStudent, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.practice_student.student.get_short_fio() + " : " +  self.practice_student.practice.title



class RatingPracticeStudent(models.Model):
    
    type_choices = (
        ('long_term', 'долгосрочный'),
        ('short_term', 'краткосрочный'),
    )

    rating_choices = (
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    )
    
    practice_student = models.OneToOneField(PracticeStudent, on_delete=models.CASCADE)
    production_tasks = models.TextField()
    type = models.CharField(max_length=20, choices=type_choices)
    pay = models.BooleanField()
    production_tasks = models.TextField()
    hard_quality = models.TextField()
    quality = models.TextField()
    amount = models.ForeignKey(Amount, on_delete=models.SET_NULL, null=True)
    remark = models.TextField()
    rating = models.CharField(max_length=2, choices=rating_choices)


def generate_upload_path(instance, filename):
    today = datetime.now()
    path = os.path.join('uploads', today.strftime('%Y/%m/%d'))
    return os.path.join(path, filename)

