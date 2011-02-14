# Helper Makefile to amalgamate the sources.


SOURCES = main.pjs events.pjs bezier.pjs
# cpp strips out comments. -P disables header comments.

all: flatland.pjs

debug:
	cat $(SOURCES) | cpp -P -DDEBUG > flatland.pjs

flatland.pjs:
	cat $(SOURCES) | cpp -P > flatland.pjs

clean:
	$(RM) flatland.pjs


.PHONY = all clean
