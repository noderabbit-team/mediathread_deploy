import os

# ## Pull in CloudFoundry's production settings
if 'VCAP_SERVICES' in os.environ:
    
    EXTRA_INSTALLED_APPS = (
        'django_stackato',
        )
    
    INSTALLED_APPS = EXTRA_INSTALLED_APPS + INSTALLED_APPS
    
    import json
    vcap_services = json.loads(os.environ['VCAP_SERVICES'])
    # XXX: avoid hardcoding here
#    srv = vcap_services['postgresql-8.4'][0]
    srv = vcap_services['mysql-5.1'][0]
    cred = srv['credentials']
    DATABASES = {
        'default': {
#            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': cred['name'],                      # Or path to database file if using sqlite3.
            'USER': cred['user'],                      # Not used with sqlite3.
            'PASSWORD': cred['password'],                  # Not used with sqlite3.
            'HOST': cred['hostname'],                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': cred['port'],                      # Set to empty string for default. Not used with sqlite3.
            }
        }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'mediathread',                      # Or path to database file if using sqlite3.
            'USER': '',                      # Not used with sqlite3.
            'PASSWORD': '',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
            }
        }
