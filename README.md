# Nails with Love by Yesenia
## Home Boutique & Mobile Nail Service — Cali, Colombia

Bilingual repository containing the complete launch package, administration dashboard, automated scripts, legal guides, training academy manuals, and the native offline Android app.

---

## English Version

This workspace serves as the launch hub for Yesenia's home-based and mobile beauty service in Cali.

### Project Structure
*   `launch-system-9.7/`: Core marketing slides, Spanish/English business plans, financial sheet, and geocoded contact directories.
*   `launch-system-9.7/website/`: Static client-facing landing page.
*   `launch-system-9.7/website/dashboard/`: Responsive mobile-first administration dashboard (appointments, client CRM, B2B leads, marketing copies).
*   `yesenia-android-app/`: Android project wrapping the local website offline.
*   `scripts/`: Automation python scripts for local B2B leads scraping and content splitting.
*   `master-package/`: PowerPoint slide decks, printable business cards, A4 counter stand, and social ads.

### Quick Start
1.  **Install Node & Python Dependencies**:
    ```bash
    npm install pptxgenjs sharp
    pip3 install reportlab --break-system-packages
    ```
2.  **Run Automation Scripts**:
    *   Find beauty salon/spa partners in Cali: `python3 scripts/find_local_leads.py`
    *   Split plans into social media content pieces: `python3 scripts/split_content.py`
3.  **Compile Marketing Assets**:
    *   Build PPTX & PDF slides: `node build_master_package.js`
    *   Build Client Playbook PDF: `python3 build_client_pdf.py`
4.  **Local Dashboard Login**:
    *   Open `launch-system-9.7/website/dashboard/index.html` in your browser.
    *   Default passcode: **`1234`**

---

## Versión en Español

Este repositorio contiene todo el sistema de lanzamiento comercial y tecnológico para la marca de servicio ornamental Nails with Love en Cali, Colombia.

### Estructura del Proyecto
*   `launch-system-9.7/`: Presentación de aliados, planes de negocio en español e inglés, modelo financiero y directorio de contactos en Cali.
*   `launch-system-9.7/website/`: Página de aterrizaje pública para las clientas.
*   `launch-system-9.7/website/dashboard/`: Panel administrativo móvil-first (calendario, CRM, prospectos locales de Cali, marketing hub).
*   `yesenia-android-app/`: Proyecto nativo de Android que empaqueta el sitio web de forma local y offline.
*   `scripts/`: Scripts en Python para extracción de leads comerciales y división de contenido.
*   `master-package/`: Diapositivas maestras, tarjetas de presentación imprimibles y anuncios de Instagram.

### Instrucciones de Uso
1.  **Instalar dependencias**:
    ```bash
    npm install pptxgenjs sharp
    pip3 install reportlab --break-system-packages
    ```
2.  **Ejecutar Generación de Datos**:
    *   Buscar peluquerías en Cali: `python3 scripts/find_local_leads.py`
    *   Actualizar copias de anuncios: `python3 scripts/split_content.py`
3.  **Compilar Presentaciones y PDFs**:
    *   Compilar diapositivas de aliados: `node build_master_package.js`
    *   Compilar Playbook en PDF: `python3 build_client_pdf.py`
4.  **Acceso al Panel Admin**:
    *   Abre `launch-system-9.7/website/dashboard/index.html`.
    *   Código de acceso por defecto: **`1234`**