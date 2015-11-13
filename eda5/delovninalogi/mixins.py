from django.contrib import messages


class MessagesActionMixin(object):

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(MessagesActionMixin, self).form_valid(form)
