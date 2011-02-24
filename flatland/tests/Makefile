# Helper Makefile for tests.


SOURCES = asserts.pjs test_*.pjs ../polygon.pjs ../gameoflife.pjs
# cpp strips out comments. -P disables header comments.

python = /usr/bin/python

all: all_tests.pjs index.html

index.html:
	$(python) ./generate_test.py all_tests.pjs >$@
	
#../polygon.pjs test_main.pjs >$@

all_tests.pjs: $(SOURCES)
	cat $(SOURCES) | cpp -P > $@

clean:
	$(RM) all_tests.pjs *.html

.PHONY = all clean
