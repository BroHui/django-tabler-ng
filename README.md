# django-tabler-ng
Django with Tabler template.

This project transforms the [Tabler](https://github.com/tabler/tabler) dashboard
into a Django package. It provides an extensible base template, error page templates,
and the necessary static assets. django-tabler-ng is based on the 
* Tabler release [v1.0.0-beta12](https://github.com/tabler/tabler/releases/tag/v1.0.0-beta12)
* Django release [3.2 LTS](https://www.djangoproject.com/download/)
* Python relase 3.9

# Installation
* `pip install django-tabler-ng`
* Add `django_tabler_ng` to your `INSTALLED_APPS`

# Usage
Once installed, templates inside your application can extend django-tabler-ng's
base template. A quick example:
```
{% extends "django_tabler_ng/base.html" %}

{% block extra_css %}
    {# add your custom css here #}
{% endblock extra_css %}

{% block content %}
    <h1>This is a Heading</h1>
    <p>This is a paragraph</p>
    <p>{{ some_context_variable }}</p>
{% endblock content %}

{% block extra_js %}
<script>
    {# add your custom javascript here #}
</script
{% endblock extra_js %}
```
Need some inspiration? Check out the [templates](https://github.com/tabler/tabler/tree/dev/dist)
provided by the original project.


### Missing a title in the browser window?
django-tabler-ng's base template adds your site's name to the browser's titlebar using Django's
[Sites](https://docs.djangoproject.com/en/3.2/ref/contrib/sites/) framework.
Follow these steps for setup:
* Add a `SITE_ID` value to your application's settings file
* Add `'django.contrib.sites'` to `INSTALLED_APPS`
* Add `'django.contrib.sites.middleware.CurrentSiteMiddleware'` to `MIDDLE_WARE`
* Run `python manage.py migrate` if necessary
* Inside your application's `django_site` database table, update the record that cooresponds to the `SITE_ID`
value with an appropriate name and domain. A custom migration might be helpful.


### Missing a favicon?
To load a favicon, create an `img/` folder inside your application's `static` directory.
Place `favicon.ico` inside, and the icon will be loaded by the base template.


### Custom error views
django-tabler-ng overrides Django's [default error views](https://docs.djangoproject.com/en/3.2/topics/http/views/#customizing-error-views)
by rendering a custom error template. Your application can access these by
adding the following to your applications' `urls.py` file:
```
handler400 = 'django_tabler_ng.views.error400'
handler403 = 'django_tabler_ng.views.error403'
handler404 = 'django_tabler_ng.views.error404'
handler500 = 'django_tabler_ng.views.error500'
```

Inspiration from @rbennett91/django-tabler.


### Debug with docker
```
docker run -it --rm -v ./example:/app -v ./src/django_tabler_ng:/app/django_tabler_ng -v ./requirements.txt:/app/requirements.txt -p 8000:8000 django:lts /bin/bash
```
