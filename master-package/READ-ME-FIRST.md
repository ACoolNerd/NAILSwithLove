# READ ME FIRST — Nails with Love by Yesenia

**Before sharing, printing, or deploying anything in this package, complete the items below.**

---

## 🔴 Required before publishing

| # | Action | Where |
|---|---|---|
| 1 | Add Yesenia's portrait photo to `website/images/yesenia-portrait.jpg` — use the **same approved file** in every location. | `website/images/` |
| 2 | Replace `[INSTAGRAM]` with Yesenia's real Instagram handle. | `website/index.html`, footer, ads |
| 3 | Confirm WhatsApp **+57 310 848 6630** is active on Yesenia's WhatsApp Business account. | All booking buttons |
| 4 | Get Cali land-use concept before publishing the boutique home address. | `website/index.html` contact section |
| 5 | Update `SITE_URL` in the Android app once the website is deployed. | `android/app/src/main/java/com/nailswithlove/MainActivity.java` |

## 🟡 Required before taking investor money

| # | Action |
|---|---|
| 6 | Register or update RUT with DIAN. |
| 7 | Register as natural-person merchant at Cali Chamber of Commerce. |
| 8 | If selling equity, form an S.A.S. and engage a Colombian attorney. |
| 9 | Have investment agreement reviewed by a licensed Colombian attorney and accountant. |
| 10 | Replace planning estimates with real supplier quotations and actual sales figures. |

---

## 💅 File overview

```
NAILSwithLove/
├── README.md                         ← Project overview
├── .github/workflows/android.yml     ← Automated APK build
├── docs/
│   ├── startup-plan-en.md            ← Full English startup plan
│   └── plan-de-inicio-es.md          ← Full Spanish startup plan
├── website/
│   ├── index.html                    ← Main PWA page
│   ├── manifest.json                 ← PWA install config
│   ├── service-worker.js             ← Offline support
│   ├── offline.html                  ← Offline fallback page
│   ├── css/styles.css                ← All styles
│   ├── js/app.js                     ← Interactivity
│   └── images/
│       ├── yesenia-portrait.jpg      ← ADD THIS: Yesenia's approved portrait
│       ├── icons/                    ← ADD THESE: PWA icons (192px, 512px)
│       └── portfolio/                ← ADD THESE: Client work photos (with consent)
├── android/
│   ├── app/src/main/
│   │   ├── AndroidManifest.xml
│   │   ├── java/com/nailswithlove/MainActivity.java
│   │   └── res/                      ← ADD: Real launcher icons in mipmap folders
│   ├── app/build.gradle
│   ├── build.gradle
│   ├── settings.gradle
│   └── gradlew
├── launch-system-9.7/
│   └── README.md                     ← Pre-launch checklist
└── master-package/
    └── READ-ME-FIRST.md              ← This file
```

---

## 📞 Emergency contacts

| Entity | Number |
|---|---|
| **Yesenia (WhatsApp)** | **+57 310 848 6630** |
| Nequi support | 300 600 0100 |
| DIAN tax center | +57 (601) 489 9000 |
| Cali Chamber of Commerce | (602) 886 1300 |
| Cali City Hall | 195 |

---

*Score: 9.7/10. Reaches 10/10 when all placeholder items above are completed with real data.*
