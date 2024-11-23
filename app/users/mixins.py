from app.mixins import DataMixin


class FormMixin(DataMixin):
    button_text = None
    __default_button_text = "Отправить"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.button_text is not None:
            context.update({"button_text": self.button_text})
        else:
            context.update({"button_text": self.__default_button_text})
        return context
