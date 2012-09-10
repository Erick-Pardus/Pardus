#!/bin/bash

CHANNEL="release"
BRANCH="releases/mozilla-$CHANNEL"
RELEASE_TAG="FIREFOX_14_0_1_RELEASE"
VERSION="14.0.1"

echo "creating compare-locales"
hg clone http://hg.mozilla.org/build/compare-locales
tar cjf compare-locales-$VERSION.tar.bz2 --exclude=.hgtags --exclude=.hgignore --exclude=.hg compare-locales