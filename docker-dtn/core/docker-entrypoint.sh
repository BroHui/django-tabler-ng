#!/bin/sh
APP_ROOT='/app'
# STATIC_ROOT='/usr/src/static'
# MEDIA_ROOT='/usr/src/media'
# mkdir -pv $MEDIA_ROOT

# cd $APP_ROOT

# # collect statics
# sed -i '/^MEDIA_ROOT/c\MEDIA_ROOT="'$MEDIA_ROOT'"' `find . | grep settings.py`
# sed -i '/^STATIC_ROOT/c\STATIC_ROOT="'$STATIC_ROOT'"' `find . | grep settings.py`
# python manage.py collectstatic --noinput

# remove debug symbol
#sed -i '/^DEBUG/c\DEBUG=False' `find . | grep settings.py`

exec $@
