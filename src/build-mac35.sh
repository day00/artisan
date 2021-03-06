#!/bin/sh
export MACOSX_DEPLOYMENT_TARGET=10.7
export PYTHONPATH="/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages"

export PATH=/Library/Frameworks/Python.framework/Versions/3.5/bin/:$PATH

# for PyQt4 running on Qt5
#export ORGPATH=$PATH
export PATH=/Users/luther/Qt5.6.0/5.6/clang_64/bin:$PATH

# translations
pylupdate5 artisan.pro
lrelease -verbose artisan.pro

# distribution
rm -rf build dist
python3.5 setup-mac35.py py2app


# recreate the translations with PyQt4/Qt4 for the Windows releases that are behind

#export PATH=$ORGPATH
#lrelease -verbose artisan.pro