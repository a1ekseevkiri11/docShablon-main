from user.models import (
    DirectionOfTraining,
    Group,
    Practice,
    PracticeStudent,
)


def get_queryset_practice_for_SupervisorPractice(supervisorpractice):
    return Practice.objects.filter(supervisor_practice=supervisorpractice)



def get_queryset_practice_student_for_SupervisorPractice(supervisorpractice):
    practice = get_queryset_practice_for_SupervisorPractice(supervisorpractice)
    return PracticeStudent.objects.filter(practice__in=practice)



def get_queryset_group_for_SupervisorPractice(supervisorpractice):
    practices = Practice.objects.filter(supervisor_practice=supervisorpractice)
    groups = Group.objects.filter(practice__in=practices).distinct()
    return groups

def get_queryset_direction_of_training_for_SupervisorPractice(supervisorpractice):
    groups = get_queryset_group_for_SupervisorPractice(supervisorpractice)

    if not groups:
        return DirectionOfTraining.objects.none()
    
    return DirectionOfTraining.objects.filter(group__in=groups).distinct()
