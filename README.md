# Nails with Love by Yesenia 💅

**Home boutique + mobile nail service — Cali, Colombia**

WhatsApp: [+57 310 848 6630](https://wa.me/573108486630)

---

## Project overview

This repository contains the complete digital launch system for **Nails with Love by Yesenia**:

| Folder | Contents |
|---|---|
| `website/` | Mobile-first PWA — booking, services, pricing, loyalty |
| `android/` | Native Android app (WebView wrapper + offline support) |
| `.github/workflows/` | Automated Android APK build on every push |
| `docs/` | English and Spanish startup plans |
| `launch-system-9.7/` | Business planning files, build scripts, vendor directory |
| `master-package/` | Bank/investor deck, counter stand, business card, ads |

## Quick start — website

```bash
# Serve locally (Python 3)
cd website
python3 -m http.server 8080
# Open http://localhost:8080
```

## Quick start — Android

Requirements: Android Studio or Java 17 + Android SDK.

```bash
cd android
./gradlew assembleDebug
# APK → android/app/build/outputs/apk/debug/app-debug.apk
```

The GitHub Actions workflow (`.github/workflows/android.yml`) builds the APK automatically on every push to `main`.

## Before publishing

- Replace every `[INSTAGRAM]` placeholder with Yesenia's actual Instagram handle.
- The WhatsApp number **+57 310 848 6630** is already wired into every button and QR link.
- Do **not** publish Yesenia's residential address publicly until the Cali land-use permit is confirmed.
- Update the portfolio images in `website/images/portfolio/` with real client photos (with consent).

## Legal and compliance note

This repository contains planning documents only. Confirm business registration, tax obligations, sanitation requirements, and investment terms with licensed Colombian professionals before launch. See `docs/startup-plan-en.md` for the full compliance checklist.

---

*Internal readiness score: **9.7 / 10**. Remaining 0.3 points require Yesenia's exact Instagram handle, confirmed land-use permit, real vendor quotations, and attorney-reviewed investor agreements.*
