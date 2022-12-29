#!/bin/sh

# create a key
rmdir -p ./keystores/
mkdir -p ./keystores/
keytool -genkey -v -keystore ./keystores/key01.keystore -alias key01 -keyalg RSA -keysize 2048 -validity 10000

# export variables
export P4A_RELEASE_KEYSTORE=./keystores/key01.keystore
export P4A_RELEASE_KEYSTORE_PASSWD=olesya
export P4A_RELEASE_KEYALIAS_PASSWD=olesya
export P4A_RELEASE_KEYALIAS=key01

# build
buildozer -v android release

# optimize
.buildozer/android/platform/android-sdk-20/build-tools/23.0.1/zipalign -v 4 ./bin/Your-App-0.1-release.apk ./bin/Your-App-0.1-release-optimized.apk