from user.models import (
    DirectionOfTraining,
    Group,
    Practice,
)


def get_queryset_practice_for_SupervisorOPOP(supervisoropop):
    directions = supervisoropop.directionoftraining_set.all()
    groups = Group.objects.filter(direction_of_training__in=directions)
    return Practice.objects.filter(group__in=groups)

def get_queryset_group_for_SupervisorOPOP(supervisoropop):
    directions = supervisoropop.directionoftraining_set.all()
    return Group.objects.filter(direction_of_training__in=directions)
    

