from django.db.models import Q



class DelilnikSearchMixin(object):

    # MERITEV = (
    #     (1, "Toplota"),
    #     (2, "Hlad"),
    #     (3, "Topla voda"),
    #     (4, "Hladna voda"),
    #     (5, "Elektrika"),
    #     )
    # stevec
    # oznaka
    # meritev

    def get_queryset(self):
        queryset = super(DelilnikSearchMixin, self).get_queryset()

        q = self.request.GET.get("q")
        distribucija = self.request.GET.get("distribucija")

        if q:
            # if filter is applied
            return queryset.filter(
                Q(oznaka__icontains=q) |
                Q(stevec__naziv__icontains=q)
                # Preveri možnost search v "related fields"
            )

        if distribucija:
            return queryset.filter(stevec__is_distribucija=True)

        # if filter is not applied
        return queryset[:15]
