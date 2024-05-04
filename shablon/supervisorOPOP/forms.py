from django import forms
from django.forms import DateInput

from user.models import (
    Practice,
    Group,
    DirectionOfTraining
)

from .queryset import(
    get_queryset_group_for_SupervisorOPOP
)



class PracticeForm(forms.ModelForm):
    fio_supervisor_company = forms.CharField(required=False)

    post_supervisor_company = forms.CharField(required=False)

    group = forms.ModelMultipleChoiceField(
        queryset=Group.objects.none(),
        widget=forms.CheckboxSelectMultiple(),
        required=False
    )

    date_start = forms.DateField(
        label="Дата начала",
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"]
    )

    date_end = forms.DateField(
        label="Дата окончания",
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"]
    )

    date_decree = forms.DateField(
        label="Дата подписания документа",
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"]
    )

    def __init__(self, supervisoropop, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['group'].queryset = get_queryset_group_for_SupervisorOPOP(supervisoropop)

        instance = kwargs.get('instance')
        if instance:
            self.fields['date_start'].widget.attrs['value'] = instance.date_start.strftime('%Y-%m-%d')
            self.fields['date_end'].widget.attrs['value'] = instance.date_end.strftime('%Y-%m-%d')
            self.fields['date_decree'].widget.attrs['value'] = instance.date_decree.strftime('%Y-%m-%d')

    class Meta:
        model = Practice
        fields = [
            'title',
            'group',
            'type',
            'kind',
            'date_start',
            'date_end',
            'number_decree',
            'date_decree',
            'title_place',
            'adress_place',
            'fio_supervisor_YuSU',
            'post_supervisor_YuSU',
            'fio_supervisor_company',
            'post_supervisor_company',
            'supervisor_practice',
        ]
        widgets = {
            'date_start': DateInput(attrs={'type': 'date'}),
            'date_end': DateInput(attrs={'type': 'date'}),
            'date_decree': DateInput(attrs={'type': 'date'}),
        }