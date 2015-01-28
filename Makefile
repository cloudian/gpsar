#########################
PKG               = gpsar
VERSION           = 0.6
RELEASE_CANDIDATE = 1
#########################

RPMVERSION = $(VERSION)
RPMRELEASE = $(RELEASE_CANDIDATE)
COMMIT     = $(shell git rev-parse --short HEAD)
APPVERSION = "$(VERSION)_$(RELEASE_CANDIDATE)_g$(COMMIT)"

PWD        = $(shell pwd)

.PHONY: all \
	rpm \
	version \
	clean

all:

version:
	# Only run from rpm as it modifies the script
	sed -i -e "s/APP_VERSION/${APPVERSION}/" bin/gpsar

clean:
	-rm -rf rpmbuild

rpm:
	-rm -rf rpmbuild
	mkdir rpmbuild
	(cd rpmbuild; mkdir BUILD BUILDROOT RPMS SOURCES SPECS SRPMS)
	tar -cz --exclude rpmbuild -f rpmbuild/SOURCES/$(PKG)-$(RPMVERSION).tar.gz .
	rpmbuild -bb --clean \
             --define "_topdir $(PWD)/rpmbuild/" \
             --define "_version $(RPMVERSION)" \
             --define "_release $(RPMRELEASE)" \
             --define "_app_version $(APPVERSION)" $(PKG).spec
