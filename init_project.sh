#! /bin/bash
cd mediathread
git submodule init
git submodule update
cd ..
mkdir -p mediathread/deploy_specific
touch mediathread/deploy_specific/__init__.py
ln -sf ../../settings.py mediathread/deploy_specific/settings.py
