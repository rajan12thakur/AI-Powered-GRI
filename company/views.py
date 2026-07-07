from django.db.models import Q
from django.views.generic import ListView

from .models import Company


class CompanyListView(ListView):
    model = Company
    template_name = "company/company_list.html"
    context_object_name = "companies"
    paginate_by = 12

    def get_queryset(self):
        qs = Company.objects.all()
        q = self.request.GET.get("q", "").strip()
        status = self.request.GET.get("status", "").strip()

        if q:
            qs = qs.filter(
                Q(legal_name__icontains=q)
                | Q(display_name__icontains=q)
                | Q(registration_number__icontains=q)
            )
        if status:
            qs = qs.filter(status=status)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["status_choices"] = Company._meta.get_field("status").choices
        context["current_query"] = self.request.GET.get("q", "")
        context["current_status"] = self.request.GET.get("status", "")
        return context
