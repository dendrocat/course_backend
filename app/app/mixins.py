from django.views.generic.base import ContextMixin


class DataMixin(ContextMixin):
    title = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.title is not None:
            context.update({"title": self.title})
        return context
