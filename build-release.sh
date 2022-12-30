#!/bin/sh

# create a key
keytool -genkey -v -keystore ./keystores/cataway.keystore -alias ca-key -keyalg RSA -keysize 2048 -validity 10000

# build
buildozer -v android release

# sign
jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore ./keystores/cataway.keystore ./bin/*release.aab ca-key

# optimize
# $ .buildozer/android/platform/android-sdk-21/tools/zipalign -v 4 ./saythis/bin/SayThis-1.1.6-release-unsigned.apk ./saythis/bin/SayThis.apk
