from django import forms
from django.forms import DateInput

from user.models import (
    RatingPracticeStudent,
    ReportGroup,
)


class RatingPracticeStudentForm(forms.ModelForm):
    class Meta:
        model = RatingPracticeStudent
        fields = [
            'type',
            'pay',
            'production_tasks',
            'hard_quality',
            'quality',
            'amount',
            'remark',
            'rating',
        ]



class ReportGroupForm(forms.ModelForm):
    class Meta:
        model = ReportGroup
        fields = [
            'title',
        ]