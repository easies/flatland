# Helper Makefile to amalgamate the sources.


SOURCES = main.pjs events.pjs bezier.pjs
# http://www.bdc.cx/software/stripcmt/
STRIPCMT=`which stripcmt || cat`

all: flatland.pjs

flatland.pjs: $(SOURCES)
	$(STRIPCMT) $(SOURCES) > flatland.pjs

clean:
	$(RM) flatland.pjs


.PHONY = all clean
