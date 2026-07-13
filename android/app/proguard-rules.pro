# Add ProGuard rules here for release builds.
# By default, the flags in this file are appended to flags specified
# in /path/to/android-sdk/tools/proguard/proguard-android.txt

# Keep WebView JavaScript bridge
-keepclassmembers class * {
    @android.webkit.JavascriptInterface <methods>;
}

# Keep AppCompat
-keep class androidx.appcompat.** { *; }
-keep interface androidx.appcompat.** { *; }
