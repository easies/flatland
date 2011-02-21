# Helper Makefile to amalgamate the sources.


SOURCES = main.pjs events.pjs bezier.pjs gameoflife.pjs map.pjs polygon.pjs\
	world.pjs penta.pjs
# cpp strips out comments. -P disables header comments.

all: flatland.pjs preload.pjs map1.js map2.js

%.js: data/%.png
	python preprocessor/map.py $< > $@

preload.pjs:
	./generate_preload.sh > preload.pjs

debug: $(SOURCES) preload.pjs
	cat $(SOURCES) | cpp -P -DDEBUG > flatland.pjs

flatland.pjs: $(SOURCES)
	cat $(SOURCES) | cpp -P > flatland.pjs

clean:
	$(RM) flatland.pjs preload.pjs


.PHONY = all clean
