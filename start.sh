#!/bin/bash
Xvfb :10 -ac &
/usr/local/bin/gunicorn --name=selenium --bind=0.0.0.0:5056 --log-level=DEBUG --workers=3 --timeout=6000 wsgi:app