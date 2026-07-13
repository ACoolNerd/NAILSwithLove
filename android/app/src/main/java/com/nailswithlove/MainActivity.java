package com.nailswithlove.yesenia;

import android.annotation.SuppressLint;
import android.net.ConnectivityManager;
import android.net.NetworkCapabilities;
import android.os.Build;
import android.os.Bundle;
import android.view.View;
import android.webkit.WebChromeClient;
import android.webkit.WebResourceRequest;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Button;
import android.content.Intent;
import android.net.Uri;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    /** Production website URL. Change this once the site is deployed. */
    private static final String SITE_URL      = "https://nailswithlove.co";
    private static final String WHATSAPP_NUM  = "573108486630";
    private static final String WHATSAPP_LINK = "https://wa.me/" + WHATSAPP_NUM +
            "?text=Hola%20Yesenia%2C%20quiero%20reservar%20una%20cita%20%F0%9F%92%85";

    private WebView webView;
    private LinearLayout offlineLayout;

    @SuppressLint("SetJavaScriptEnabled")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        webView       = findViewById(R.id.webView);
        offlineLayout = findViewById(R.id.offlineLayout);
        Button btnWhatsApp = findViewById(R.id.btnWhatsApp);
        Button btnRetry    = findViewById(R.id.btnRetry);

        /* ── WebView settings ── */
        WebSettings settings = webView.getSettings();
        settings.setJavaScriptEnabled(true);
        settings.setDomStorageEnabled(true);
        settings.setCacheMode(WebSettings.LOAD_DEFAULT);
        settings.setMixedContentMode(WebSettings.MIXED_CONTENT_NEVER_ALLOW);
        settings.setAllowFileAccess(false);
        settings.setAllowContentAccess(false);
        settings.setGeolocationEnabled(false);

        /* ── WebViewClient: handle navigation & offline fallback ── */
        webView.setWebViewClient(new WebViewClient() {
            @Override
            public boolean shouldOverrideUrlLoading(WebView view, WebResourceRequest request) {
                String url = request.getUrl().toString();
                /* Open external links (WhatsApp, DIAN, etc.) in the system browser */
                if (!url.startsWith(SITE_URL) && !url.startsWith("file://")) {
                    startActivity(new Intent(Intent.ACTION_VIEW, Uri.parse(url)));
                    return true;
                }
                return false;
            }

            @Override
            public void onPageFinished(WebView view, String url) {
                if (isNetworkAvailable()) {
                    webView.setVisibility(View.VISIBLE);
                    offlineLayout.setVisibility(View.GONE);
                }
            }

            @Override
            public void onReceivedError(WebView view, int errorCode,
                                        String description, String failingUrl) {
                showOffline();
            }
        });

        webView.setWebChromeClient(new WebChromeClient());

        /* ── Buttons ── */
        btnWhatsApp.setOnClickListener(v ->
                startActivity(new Intent(Intent.ACTION_VIEW, Uri.parse(WHATSAPP_LINK))));

        btnRetry.setOnClickListener(v -> {
            if (isNetworkAvailable()) {
                offlineLayout.setVisibility(View.GONE);
                webView.setVisibility(View.VISIBLE);
                webView.reload();
            }
        });

        /* ── Initial load ── */
        if (isNetworkAvailable()) {
            webView.loadUrl(SITE_URL);
        } else {
            showOffline();
        }
    }

    @Override
    protected void onResume() {
        super.onResume();
        if (isNetworkAvailable() && offlineLayout.getVisibility() == View.VISIBLE) {
            offlineLayout.setVisibility(View.GONE);
            webView.setVisibility(View.VISIBLE);
            webView.reload();
        }
    }

    @Override
    public void onBackPressed() {
        if (webView.canGoBack()) {
            webView.goBack();
        } else {
            super.onBackPressed();
        }
    }

    // ── Helpers ──────────────────────────────────────────────────────────────

    private void showOffline() {
        webView.setVisibility(View.GONE);
        offlineLayout.setVisibility(View.VISIBLE);
    }

    private boolean isNetworkAvailable() {
        ConnectivityManager cm =
                (ConnectivityManager) getSystemService(CONNECTIVITY_SERVICE);
        if (cm == null) return false;
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
            NetworkCapabilities caps = cm.getNetworkCapabilities(cm.getActiveNetwork());
            return caps != null && (
                    caps.hasTransport(NetworkCapabilities.TRANSPORT_WIFI) ||
                    caps.hasTransport(NetworkCapabilities.TRANSPORT_CELLULAR) ||
                    caps.hasTransport(NetworkCapabilities.TRANSPORT_ETHERNET)
            );
        }
        android.net.NetworkInfo info = cm.getActiveNetworkInfo();
        return info != null && info.isConnected();
    }
}
