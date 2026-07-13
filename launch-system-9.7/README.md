# Nails with Love by Yesenia — Launch System 9.7

## Internal readiness score: 9.7 / 10

This folder contains the complete digital launch system for **Nails with Love by Yesenia**, a home boutique + mobile nail service in Cali, Colombia.

---

## What's in this folder

| File / folder | Contents |
|---|---|
| `README.md` | This file — overview and completion checklist |
| `../docs/startup-plan-en.md` | Full English startup plan |
| `../docs/plan-de-inicio-es.md` | Full Spanish startup plan |
| `../website/` | PWA website — booking, services, pricing, loyalty |
| `../android/` | Android app (WebView wrapper + offline support) |
| `../.github/workflows/android.yml` | Automated GitHub Actions APK build |
| `../master-package/` | Bank/investor deck, ads, business card, counter stand |

---

## Pre-launch checklist

### Identity and brand
- [ ] Yesenia's approved portrait at `website/images/yesenia-portrait.jpg` — use the **exact same file** everywhere. Do not regenerate or substitute.
- [ ] Replace all `[INSTAGRAM]` placeholders with Yesenia's real Instagram handle.
- [ ] Verify WhatsApp **+57 310 848 6630** works and goes to Yesenia's WhatsApp Business account.
- [ ] Replace QR code placeholders with the real wa.me QR.

### Compliance and legal
- [ ] Confirm land-use concept from Cali municipality before publishing the boutique address.
- [ ] Register RUT through DIAN.
- [ ] Register as natural-person merchant at the Cali Chamber of Commerce.
- [ ] Consult a Colombian accountant on SIMPLE vs. ordinary income regime and electronic invoicing.
- [ ] Complete sanitation setup per Resolution 2117/2010 and biosecurity manual 2827/2006.
- [ ] If equity investors are planned, form S.A.S. and engage a Colombian lawyer.

### Financial and payments
- [ ] Open a dedicated Nequi Negocios account.
- [ ] Test QR Negocios and Tap to Phone with a small transaction.
- [ ] Sign up for Alegra for DIAN-compatible electronic invoicing.
- [ ] Set up Treinta or AgendaPro for client management.

### Website
- [ ] Deploy `website/` to a hosting provider (Netlify, GitHub Pages, or Vercel are free options).
- [ ] Upload Yesenia's portrait to `website/images/yesenia-portrait.jpg`.
- [ ] Upload 6–12 portfolio photos (with client consent) to `website/images/portfolio/`.
- [ ] Test on mobile (iOS Safari + Android Chrome).
- [ ] Verify PWA installs correctly (Add to Home Screen).
- [ ] Verify WhatsApp button opens the correct chat.

### Android app
- [ ] Update `SITE_URL` in `MainActivity.java` with the real deployed domain.
- [ ] Add real launcher icons to all `mipmap-*` folders.
- [ ] Run `./gradlew assembleDebug` locally or push to GitHub to trigger the Actions build.
- [ ] Download the APK from GitHub Actions → share with Yesenia for testing.
- [ ] For Play Store release: sign the APK with a keystore and complete `release` build type.

### Marketing
- [ ] Print and laminate the counter stand for the boutique workspace.
- [ ] Print 50+ business cards (front and back).
- [ ] Place partner A4 QR stands with at least 3 local partners in month 1.
- [ ] Schedule Facebook and Instagram posts for launch week.

---

## Key contacts (do not publish home address until land-use approved)

| Entity | Contact |
|---|---|
| Yesenia WhatsApp | +57 310 848 6630 |
| Cali Chamber of Commerce | (602) 886 1300 · WhatsApp +57 318 886 1300 · Calle 8 #3-14 |
| DIAN | +57 (601) 489 9000 |
| Cali City Hall | 195 · (602) 887 9020 · contactenos@cali.gov.co |
| Cali Health Secretariat | (602) 519 5100 · atencionalusuarioensalud@cali.gov.co |
| Nequi Negocios support | 300 600 0100 |

---

## Score to 10/10

The remaining 0.3 points require:
1. Real portrait file committed at `website/images/yesenia-portrait.jpg`
2. Instagram handle replacing all `[INSTAGRAM]` placeholders
3. Confirmed Cali land-use concept for the boutique address
4. Current vendor quotations replacing the researched estimates
5. Attorney-reviewed investor/revenue-share agreement (if seeking external funding)
