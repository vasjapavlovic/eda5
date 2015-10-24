from django.shortcuts import render
from django.utils import timezone
from django.db.models import Q


class SearchMixin(object):

    def get_queryset(self):
        queryset = super(SearchMixin, self).get_queryset()

        q = self.request.GET.get("q")
        sf = self.request.GET.get("search_field")
        print(sf, q )
        # When search filed selected is "TITLE"
        if sf == "title":
            # return filter on field "title"
            if q:
                # return a filtered queryset
                return queryset.filter(title__icontains=q)
            # no q is specified so we return queryset
            return queryset

        elif sf == "address":
                # return filter on field "title"
            if q:
                    # return a filtered queryset
                return queryset.filter(block_address__icontains=q)
                # no q is specified so we return queryset
            return queryset

        elif sf == "description":
            # return filter on field "title"
            if q:
                    # return a filtered queryset
                return queryset.filter(description__icontains=q)
                # no q is specified so we return queryset
            return queryset

        elif sf == "all":
            # return filter on field "title"
            if q:
                    # return a filtered queryset
                return queryset.filter(Q(title__icontains=q) | Q(description__icontains=q) | Q(block_address__icontains=q))
                # no q is specified so we return queryset
            return queryset

        else:
            return queryset
