
from django.urls import path, include

from app.views import (
    DefaultFormByFieldView,
    DefaultFormsetView,
    DefaultFormView,
    FormHorizontalView,
    FormInlineView,
    FormWithFilesView,
    HomePageView,
    MiscView,
    PaginationView,
    index
)

handler404 = 'django_tabler_ng.views.error404'

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("index", index, name="index"),
    path("formset", DefaultFormsetView.as_view(), name="formset_default"),
    path("form", DefaultFormView.as_view(), name="form_default"),
    path("form_by_field", DefaultFormByFieldView.as_view(), name="form_by_field"),
    path("form_horizontal", FormHorizontalView.as_view(), name="form_horizontal"),
    path("form_inline", FormInlineView.as_view(), name="form_inline"),
    path("form_with_files", FormWithFilesView.as_view(), name="form_with_files"),
    path("pagination", PaginationView.as_view(), name="pagination"),
    path("misc", MiscView.as_view(), name="misc"),
    path('dtn/', include('django_tabler_ng.urls')),
]