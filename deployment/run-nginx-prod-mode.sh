docker run -ti -v /Users/sonlinux/dev/python/djp/deployment/static/:/home/web/static/ --link djp-uwsgi -p 8889:80 -v /Users/sonlinux/dev/python/djp/deployment/media/:/home/web/media/ alisonmukoma/nginx-django