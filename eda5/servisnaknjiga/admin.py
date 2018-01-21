from django.contrib import admin


from .models import Parameter

@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    raw_id_fields=(
        'plan_kontrola_specifikacija',
        'projektno_mesto',
    )
