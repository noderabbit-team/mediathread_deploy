Wrapper project to deploy MediaThread
=====================================

1. Get the MediaThread code and submodules::

	$ git clone --recursive git://github.com/natea/mediathread_deploy.git
	$ cd mediathread_deploy/mediathread
	$ git submodule init
	$ git submodule update

2. Create a directory mediathread/deploy_specific::

    $ mkdir mediathread/deploy_specific
    
3. Add a file __init__.py file into the deploy_specific directory.

    $ touch mediathread/deploy_specific/__init__.py
    
4. Create a symlink to the settings.py file::

    $ ln -s settings.py mediathread/deploy_specific/settings.py

5. Login to MediaThread by pointing your browser at http://mediathread.stackato-xxxx.local 

6. Use these login credentials (can be changed in stackato.yml)::

	un: admin
	pw: secret123
