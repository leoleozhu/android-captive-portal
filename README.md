# android-captive-portal
An heroku ready app replaces Google's generate 204 service.

When an Android device is connected to WiFi, a request to clients3.google.com/generate_204 will be made. 
If the request successfully returns 204, it means the network is ready to use. 
If it cannot return 204, it means the network needs authentication before you can use it.

However, Google is blocked in mainland China. There will be a "!" with your WiFi icon.


After publishing you app, you need to change your device

* Get into adb shell ``$ adb shell``

* In adb shell, execute ``$ settings put global captive_portal_server your-domain.com``

