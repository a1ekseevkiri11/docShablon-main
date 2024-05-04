import django_filters
from django import forms

from user.models import (
    Practice,
    Group,
    DirectionOfTraining,
)

from .queryset import(
    get_queryset_group_for_SupervisorOPOP
)

class PracticeFilter(django_filters.FilterSet):
    
    type = django_filters.ChoiceFilter(
        field_name='type', 
        choices=Practice.type_choices, 
        widget=forms.RadioSelect,
        label="Тип практики",
    )
    type.field.empty_label = "Все"

    kind = django_filters.ChoiceFilter(
        field_name='kind', 
        choices=Practice.kind_choices, 
        widget=forms.RadioSelect,
        label="Вид практики",
    )
    kind.field.empty_label = "Все"

    group = django_filters.ModelMultipleChoiceFilter(
        field_name='group__title', 
        queryset=Group.objects.all(), 
        widget=forms.CheckboxSelectMultiple,
        label="Группы",
    )

    direction_of_training = django_filters.ModelMultipleChoiceFilter(
        field_name='group__direction_of_training__title', 
        queryset=DirectionOfTraining.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Направления подготовки",
    )


    class Meta:
        model = Practice
        fields = ['type', 'kind', 'direction_of_training', 'group']


    def __init__(self, *args, **kwargs):
        self.supervisoropop = kwargs.pop('supervisoropop', None)  # Получаем пользователя из kwargs
        super().__init__(*args, **kwargs)
        self.filters['direction_of_training'].queryset = self.supervisoropop.directionoftraining_set.all()
        self.filters['group'].queryset = get_queryset_group_for_SupervisorOPOP(self.supervisoropop)