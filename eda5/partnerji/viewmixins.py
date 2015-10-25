from django.db.models import Q


class PartnerSearchMixin(object):

    # model fields on which the search can be applied
    # davcna_st
    # maticna_st
    # dolgo_ime
    # kratko_ime
    # naslov
    # posta

    def get_queryset(self):
        queryset = super(PartnerSearchMixin, self).get_queryset()

        q = self.request.GET.get("q")

        if q:
            # if filter is applied
            return queryset.filter(
                Q(davcna_st__icontains=q) |
                Q(maticna_st__icontains=q) |
                Q(dolgo_ime__icontains=q) |
                Q(kratko_ime__icontains=q) |
                Q(naslov__icontains=q)
                # Preveri možnost search v "related fields"
            )
        # if filter is not applied
        return queryset
