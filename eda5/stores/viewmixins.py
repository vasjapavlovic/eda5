from django.db.models import Q


class StoresSearchMixin(object):

    # model fields on which the search can be applied
    # title
    # block_address
    # phone
    # description

    def get_queryset(self):
        queryset = super(StoresSearchMixin, self).get_queryset()

        q = self.request.GET.get("q")

        if q:
            # if filter is applied
            return queryset.filter(
                Q(title__icontains=q) |
                Q(description__icontains=q) |
                Q(block_address__icontains=q)
            )
        # if filter is not applied
        return queryset
