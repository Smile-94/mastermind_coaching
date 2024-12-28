from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add custom context data
        context["message"] = "Welcome to the Home Page!"
        return context
