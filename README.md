# 🐈 Data Structures Lab Programs — Neumorphic Sigma Cat Edition

A premium, modern **Neumorphic (Soft UI)** Data Structures practical code library with sigma orange cat personality. Clean, elegant, warm cream and beige depth effects paired with real orange cats and warm orange silhouettes.

---

## 🎨 1. Neumorphic (Soft UI) Design System

- **Warm Cream & Ivory Palette**: `--neu-bg: #ece7dc;`, with soft dual-shadow highlights (`#ffffff`) and soft ambient shadows (`#c5beae`).
- **Soft Extruded Surfaces**: Replaced harsh brutalist black strokes with natural raised surfaces, gently curved corners (`border-radius: 22px;`), and organic depth.
- **Inset Controls**: Search box, category counters, and code frame feature realistic inset neumorphic shadows (`inset 5px 5px 10px #c5beae, inset -5px -5px 10px #ffffff`).
- **Warm Orange Cat Accents**: Vibrant ginger orange (`#ea580c` / `#f97316`) for primary focus states, badge tags, and icons.

---

## 🐱 2. Real Orange Cat Photos + Orange Silhouettes

- **100% Authentic Real Cat Photographs**: Extracted directly from user reference screenshots without cartoonization or modification:
  - 🕶️ **Sigma Boss Cat with Sunglasses** (Hero mascot)
  - 🎧 **Tactical Balaclava Hacker Cat** (Header avatar & lab guardian)
  - ☕ **Corporate Cat with Collar & Coffee** (Companion near Copy Code button)
  - 🍞 **In-Bread Standing Cat** (Circular queue badge)
  - 🐱 **Pana Miguel Kitten** (Gentle walking cat)
  - ⚡ **Wet Matrix Punk Cat with Silver Shades**
  - 🥤 **Gamer Cat drinking Monster Energy**
  - 😴 **Sleepy Cat on Exam Notes**
  - 🙀 **Shocked Gasping Cat**
- **Orange Silhouette Cats**: Clean vector silhouettes in poses (walking, stretching, sitting upright, curled up) integrated as subtle decorative elements and background watermarks.

---

## 🧘 3. 70% Clean Functionality + 30% Sigma Cat Personality

- **Clutter-Free & Focused**: Removed excessive floating text and flying banners. The experiment cards are prominent, clear, and full-width clickable.
- **Natural, Lightweight Animations**:
  - Gentle, slow walking cat along the bottom screen edge (`gentleWalk 34s`).
  - Subtle breathing animation on the sleepy corner cat (`softBreathe 4s`).
  - Corner peeking cat sits quietly until hovered.
- **Calm, High-Readability Code Page**:
  - Dark IDE window (`#111520`) with line numbers and clear C syntax highlighting.
  - Large prominent **COPY CODE** button with smooth neumorphic depth and single-click copy.
  - Companion cat sits politely outside the editor near the Copy button.
  - Zero overlapping of code or buttons.

---

## 📁 Project Structure

```text
Codes web/
├── index.html            # Neumorphic HTML structure
├── style.css             # Neumorphic soft dual-shadows, cream palette & smooth transitions
├── app.js                # Routing, syntax highlighter, copy logic & auto-image recover
├── cat-assets.js         # Embedded high-res fallback assets for GitHub Pages
├── experiments-data.js   # Complete lab manual data (10 programs)
├── .nojekyll             # Prevents GitHub Pages from ignoring folders or subdirectories
├── assets/cats/
│   ├── cat_masala_dosa.jpg # Clean programmer cat (MASALA DOSA? splash)
│   ├── cat_cap_mascot.png  # Denim cap cat with bell collar (Chief Debugger)
│   ├── cat_*.png           # Extracted authentic real cat photographs
│   └── silhouettes/        # Warm orange vector cat silhouettes
└── README.md             # Documentation
```

---

## 🌐 Deploying to GitHub Pages (Broken Images Fix)

When deploying to GitHub Pages:
1. Make sure to upload **all files** in this folder, especially:
   - `index.html`
   - `style.css`
   - `app.js`
   - `cat-assets.js` *(Critical for 100% reliable image fallback)*
   - `experiments-data.js`
   - `.nojekyll` *(Disables Jekyll so GitHub Pages doesn't block asset folders)*
   - The entire `assets/` folder (with `assets/cats/`)
2. **Bulletproof Fallback**: Even if the `assets` folder is missed during GitHub Web upload, `cat-assets.js` contains embedded high-resolution Base64 versions of all cat characters, ensuring that **broken image icons never appear on your live site**.

---

## 🚀 How to Run Locally

1. Open [index.html](file:///c:/Users/TEJASWINI/Codes%20web/index.html) in any web browser.
2. Search, filter, click any experiment card, and copy the full C code with one click!
