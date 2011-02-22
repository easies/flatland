# Helper Makefile to amalgamate the sources.


SOURCES = main.pjs events.pjs bezier.pjs gameoflife.pjs map.pjs polygon.pjs\
	world.pjs penta.pjs menu.pjs
# cpp strips out comments. -P disables header comments.
JS_MAPS = map1.js map2.js
python = /usr/bin/python

all: flatland.pjs preload.pjs map1.js map2.js index.html

%.js: data/%.png
	$(python) preprocessor/map.py $< > $@

index.html: $(JS_MAPS)
	$(python) generate_index.py $(JS_MAPS) >$@

preload.pjs:
	./generate_preload.sh > preload.pjs

debug: $(SOURCES) preload.pjs
	cat $(SOURCES) | cpp -P -DDEBUG > flatland.pjs

flatland.pjs: $(SOURCES)
	cat $(SOURCES) | cpp -P > flatland.pjs

clean:
	$(RM) flatland.pjs preload.pjs index.html

clean-all: clean
	$(RM) map*.js

.PHONY = all clean clean-all debug
