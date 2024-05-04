from user.models import (
    Student,
    SupervisorOPOP,
    SupervisorPractice,
)


def isStudent(user):
    return Student.objects.filter(user=user).exists()


def isSupervisorOPOP(user):
    return SupervisorOPOP.objects.filter(user=user).exists()


def isSupervisorPractice(user):
    return SupervisorPractice.objects.filter(user=user).exists()
