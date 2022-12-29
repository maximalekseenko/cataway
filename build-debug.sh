#!/bin/sh

# build
buildozer -v android debug

# install on android
adb install -r bin/*debug.apk

# run
echo 'Please connect on transfer files mode the cellphone'
adb logcat -s "python"