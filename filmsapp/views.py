from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from filmsapp.models import Movie, Category, Genre


class PageMainTitleMixin:
    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=None, **kwargs)
        data['main_title'] = self.main_title
        return data


class MoviesList(PageMainTitleMixin, ListView):
    model = Movie
    main_title = "Список фильмов"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        data = super().get_context_data(object_list=None, **kwargs)
        print(data)
        return data

    def get_queryset(self):
        return self.model.objects.filter(is_active=True)


class MovieDetail(PageMainTitleMixin, DetailView):
    model = Movie
    main_title = "Фильм"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(object_list=None, **kwargs)
        return data


class MovieCatalog(PageMainTitleMixin, ListView):
    model = Category
    main_title = "Категории"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(object_list=None, **kwargs)
        return data


class MovieCatalogPK(PageMainTitleMixin, ListView):
    model = Movie
    main_title = "Категория"

    def get_queryset(self):
        pk = self.kwargs['pk']
        return self.model.objects.filter(category__pk=pk)


class MovieGenre(PageMainTitleMixin, ListView):
    model = Genre
    main_title = "Жанры"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(object_list=None, **kwargs)
        return data


class MovieGenrePK(PageMainTitleMixin, ListView):
    model = Movie
    main_title = "Жанр"

    def get_queryset(self):
        pk = self.kwargs['pk']
        return self.model.objects.filter(genres__pk=pk)
