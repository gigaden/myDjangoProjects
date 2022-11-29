from django.contrib import admin
from .models import Movie, Director
from django.db.models import QuerySet


# Register your models here.


class DirectorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'director_email']
    list_editable = ['director_email']

admin.site.register(Director, DirectorAdmin)

class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'year', 'budget', 'rating_status', 'currency']
    list_editable = ['rating', 'year', 'budget', 'currency']
    ordering = ['budget']
    list_per_page = 3
    actions = ['set_dollars']
    search_fields = ['name']

    def rating_status(self, mov: Movie):
        if mov.rating < 90:
            return 'Зачем это смотреть'

    @admin.action(description='всё в баксы переводим мы')
    def set_dollars(self, request, qs: QuerySet):
        qount_update = qs.update(currency=Movie.USD)
        self.message_user(request,f'было обновлено{qount_update} записей')


admin.site.register(Movie, MovieAdmin)
