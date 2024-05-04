from django.shortcuts import render, get_object_or_404

from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
)

from django.views.generic import (
    ListView,
    DetailView,
    View,
    CreateView,
    UpdateView,
    DeleteView,
    ListView
)

from django.db.models import Q


from registration.permission import isSupervisorPractice

from user.models import (
    PracticeStudent,
    Practice,
    RatingPracticeStudent,
    Group,
    ReportGroup
)

from .forms import (
    RatingPracticeStudentForm,
    ReportGroupForm,
)

from .filters import (
    PracticeStudentFilter,
)

from .queryset import (
    get_queryset_practice_student_for_SupervisorPractice,
    get_queryset_group_for_SupervisorPractice,
    get_queryset_practice_for_SupervisorPractice,
)

from django.urls import (
    reverse_lazy,
    reverse,
)

from django.http import HttpResponseRedirect


class SupervisorPracticeMixin(LoginRequiredMixin, UserPassesTestMixin):

    def extra_test_func(self):
        return True
    
    def test_func(self):
        return isSupervisorPractice(self.request.user) and self.extra_test_func()




class PracticeStudentListView(ListView, SupervisorPracticeMixin):
    template_name = 'supervisorPractice/practice_student_list.html'
    context_object_name = 'practices'
    paginate_by = 1


    def get_queryset(self):
        queryset = get_queryset_practice_student_for_SupervisorPractice(self.request.user.supervisorpractice)
        query = self.request.GET.get('q')
        filters = self.request.GET
        
        if query:
            queryset = queryset.filter(Q(title__icontains=query))
        
        self.filterset = PracticeStudentFilter(filters, queryset=queryset, supervisorpractice=self.request.user.supervisorpractice,)
        return self.filterset.qs
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filters'] = self.filterset.form
        context['applied_filters'] = self.request.GET.urlencode()
        return context



class PracticeStudentDetailView(View, SupervisorPracticeMixin):
    template_name = 'supervisorPractice/practice_student_detail.html'

    def get(self, request, pk):
        practice_student = get_object_or_404(PracticeStudent, pk=pk)
        context = {}
        context['practice'] = practice_student.practice
        context['practice_student'] = practice_student
        return render(request, self.template_name, context)


class RatingPracticeStudentCreateView(CreateView, SupervisorPracticeMixin):
    template_name = 'supervisorPractice/practice_student_form.html'
    model = RatingPracticeStudent
    form_class = RatingPracticeStudentForm

    def extra_test_func(self):
        practice_student_id = self.kwargs['practice_student_id']
        practice_student = get_object_or_404(PracticeStudent, id=practice_student_id)
        return practice_student.practice.supervisor_practice == self.request.user.supervisorpractice
    
    def form_valid(self, form):
        practice_student_id = self.kwargs['practice_student_id']
        practice_student = get_object_or_404(PracticeStudent, id=practice_student_id)
        form.instance.practice_student = practice_student
        return super().form_valid(form)

    def get_success_url(self):
        practice_student_id = self.kwargs['practice_student_id']
        return reverse('supervisor-practice-practice-student-detail', kwargs={'pk': practice_student_id})






class RatingPracticeStudentUpdateView(UpdateView, SupervisorPracticeMixin):
    template_name = 'supervisorPractice/practice_student_form.html'
    model = RatingPracticeStudent
    form_class = RatingPracticeStudentForm

    def extra_test_func(self):
        practice_student_id = self.kwargs['practice_student_id']
        practice_student = get_object_or_404(PracticeStudent, id=practice_student_id)
        return practice_student.practice.supervisor_practice == self.request.user.supervisorpractice
    
    def form_valid(self, form):
        practice_student_id = self.kwargs['practice_student_id']
        practice_student = get_object_or_404(PracticeStudent, id=practice_student_id)
        form.instance.practice_student = practice_student
        return super().form_valid(form)

    def get_success_url(self):
        practice_student_id = self.kwargs['practice_student_id']
        return reverse('supervisor-practice-practice-student-detail', kwargs={'pk': practice_student_id})
    

class ReportGroupListView(ListView, SupervisorPracticeMixin):
    template_name = 'supervisorPractice/report_group_list.html'
    context_object_name = 'practices'
    paginate_by = 1


    def get_queryset(self):
        practice = get_queryset_practice_for_SupervisorPractice(self.request.user.supervisorpractice)
        practice = practice.filter(reportgroup__isnull=True)
        return practice
        
    

class ReportGroupCreateView(CreateView, SupervisorPracticeMixin):
    template_name = 'supervisorPractice/report_group_form.html'
    context_object_name = 'group'
    model = ReportGroup
    form_class = ReportGroupForm
    success_url = reverse_lazy('report-group-list')




    def form_valid(self, form):
        practice_id = self.kwargs['practice_id']
        group_id = self.kwargs['group_id']

        practice = get_object_or_404(Practice, id=practice_id)
        group =  get_object_or_404(Group, id=group_id)
        form.instance.practice = practice
        form.instance.group = group
        return super().form_valid(form)



class ReportGroupUpdateView(UpdateView, SupervisorPracticeMixin):

    template_name = 'supervisorPractice/report_group_form.html'
    context_object_name = 'group'
    model = ReportGroup
    form_class = ReportGroupForm
    success_url = reverse_lazy('report-group-list')


