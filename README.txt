.. vim: ft=rst :

Third-party code
================

Flatland uses these third-party libraries:

    * Processing.js (1.0.0)

        * flatland/js/processing-1.0.0.js
        * flatland/js/processing-1.0.0.min.js

    * Google's jsapi to load:

        * jQuery

Image sources
=============

    The house diagram used in map1 is from _Flatland_. It was downloaded from
    `http://en.wikipedia.org/wiki/File:Flatland_house_diagram.png`
    It is public domain.

    The detailed diagram used in map1 is also from _Flatland_. It was
    downloaded from `http://www.eldritchpress.org/eaa/GIF/A081.GIF`.

Documentation
=============

The documentation sources are at ``./doc/``. The generated documentation will
be at ``./flatland/doc/``. You can browse it by launching a browser to that
location (it is also linked from the app).

To generate the documentation, you need `sphinx <http://sphinx.pocoo.org/>`_.

    virtualenv env
    source env/bin/activate
    pip install sphinx
    cd ./doc/ && make html

Running
=======

A shell script ``./run.sh`` is included, which will make, run a webserver,
then launch a browser. To do it manually:

    cd flatland && make
    python -m SimpleHTTPServer &
    google-chrome http://localhost:8000

Tests
=====

The tests are located at ``./flatland/tests``. To run the test, you need to
``make`` in the directory then launch a browser at ``./flatland/tests/``.

LICENSE.txt
===========

The license applies to everything other than the third-party code mentioned
above.
