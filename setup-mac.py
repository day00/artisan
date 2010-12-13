"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

import sys, os
from setuptools import setup


# current version of Artisan
VERSION = '0.0.31'
LICENSE = 'GNU General Public License (GPL)'

QTDIR = r'/Developer/Applications/Qt/'

APP = ['artisan.pyw']

DATA_FILES = [
    "index.html",
    ("../PlugIns/iconengines", [QTDIR + r'/plugins/iconengines/libqsvgicon.dylib']),
    ("../PlugIns/imageformats", [QTDIR + r'/plugins/imageformats/libqsvg.dylib'])
  ]
  
OPTIONS = {
    'argv_emulation': False,
    'semi_standalone': False,
    'site_packages': True,
    'optimize':  1,
    'iconfile': 'artisan.icns',
    'includes': ['sip',
                 'serial',
                 'PyQt4.QtCore',
                 'PyQt4.QtGui',
                 'PyQt4.QtSvg',
                 'PyQt4.QtXml'],
    'excludes' : ['_tkagg','_ps','_fltkagg',
                  '_agg','_cairo','_gtk','gtkcairo',
                  '_wxagg','_tkagg','_cocoaagg','_wx'],
    'plist'    : {  'CFBundleDisplayName': 'Artisan',
                    'CFBundleGetInfoString' : 'Artisan, Roast Logger',
                    'CFBundleIdentifier':'com.google.groups.questm3',
                    'CFBundleShortVersionString':VERSION,
                    'CFBundleVersion': 'Artisan ' + VERSION,
                    'LSMinimumSystemVersion':'10.6',
                    'LSMultipleInstancesProhibited':'true',
                    'NSHumanReadableCopyright':LICENSE
                }}

setup(
    name='Artisan',
    version=VERSION,
    author='YOU',
    author_email='zauborg@yahoo.com',
    license=LICENSE,
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

print '*** Removing Qt debug libs ***'
for root, dirs, files in os.walk('./dist'):
    for file in files:
        if 'debug' in file:
            print 'Deleting', file
            os.remove(os.path.join(root,file))
        if 'test_' in file:
            print 'Deleting', file
            os.remove(os.path.join(root,file))
        if '_tests' in file:
            print 'Deleting', file
            os.remove(os.path.join(root,file))
            
        
os.chdir('dist')
os.system(r'macdeployqt Artisan.app -dmg')