from django.views.generic import DetailView
from django.views.generic.edit import CreateView

from .models import Employee


class EmployeeCreateView(CreateView):
    model = Employee
    fields = ['name', 'role', 'date_joined', 'email']  # Add other fields as needed
    template_name = 'uprofile/create.html'  # Create a template for the form
    success_url = '/employee/profile/'  # Redirect to the employee's profile page after creation

    def get_success_url(self):
        return reverse('employee_profile', kwargs={'pk': self.object.pk})
        
class EmployeeProfileView(DetailView):
    model = Employee
    template_name = 'uprofile/employee.html'
    context_object_name = 'employees'