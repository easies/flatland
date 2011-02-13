# Helper Makefile to amalgamate the sources.


SOURCES = main.pjs events.pjs bezier.pjs

all: flatland.pjs

flatland.pjs: $(SOURCES)
	cat $(SOURCES) > flatland.pjs

clean:
	$(RM) flatland.pjs


.PHONY = all clean
