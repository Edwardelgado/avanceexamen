from django.contrib import admin
from .models import Doctor, Especialidad, Citas, Paciente, Tipodocumento, Tiposeguro

# Register your models here.


admin.site.register(Doctor)
admin.site.register(Especialidad)
admin.site.register(Citas)
admin.site.register(Paciente)
admin.site.register(Tipodocumento)
admin.site.register(Tiposeguro)
