import django_filters
from django import forms

from user.models import (
    PracticeStudent,
    Practice,
    Group,
    DirectionOfTraining,
    Amount,
    RatingPracticeStudent
)

from .queryset import (
    get_queryset_direction_of_training_for_SupervisorPractice,
    get_queryset_group_for_SupervisorPractice,
)


class PracticeStudentFilter(django_filters.FilterSet):
    
    APPRECIATED_CHOICES = [
        (True, 'Да'),
        (False, 'Нет')
    ]

    appreciated = django_filters.ChoiceFilter(
        choices=APPRECIATED_CHOICES,
        widget=forms.RadioSelect,
        label='Выставлена оценка',
        method = 'filter_rating',
        empty_label = "Все",
    )


    group = django_filters.ModelMultipleChoiceFilter(
        field_name='practice__group',
        queryset=Group.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Группы",
    )

    direction_of_training = django_filters.ModelMultipleChoiceFilter(
        field_name='practice__group__direction_of_training',
        queryset=DirectionOfTraining.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Направления подготовки",
    )



    class Meta:
        model = PracticeStudent
        fields = [
            'direction_of_training', 
            'group', 
            'appreciated',
        ]


    def __init__(self, *args, **kwargs):
        self.supervisorpractice = kwargs.pop('supervisorpractice', None)  # Получаем пользователя из kwargs
        super().__init__(*args, **kwargs)
        self.filters['direction_of_training'].queryset = get_queryset_direction_of_training_for_SupervisorPractice(self.supervisorpractice)
        self.filters['group'].queryset = get_queryset_group_for_SupervisorPractice(self.supervisorpractice)


    def filter_rating(self, queryset, name, value):
        if value == 'True':
            return queryset.exclude(ratingpracticestudent__isnull=True)
        elif value == 'False':
            return queryset.filter(ratingpracticestudent__isnull=True)
        else:
            return queryset
