# nyspex.mickla.se

Direktionens arbetsbok för nyuppsättningar av Chalmersspex: tidplan, steg för steg, beslut och händelser, öppna frågor. Bygger på FGV:s och Jubileumskommitténs nyuppsättningsguide (v5, 2026). Sammanställd av Dan Engström.

Allt som fylls i sparas i webbläsaren och delas inom direktionen genom att spara och läsa in en fil.

## Ändra innehållet

- Kapitlens text och punkter: `src/content_ch.js`
- Faktarutor (lokaljämförelse, mötesagenda, organisationsmodell): `src/content_info.js`
- Layout, stil och logik: `src/template.html`
- Bilder: `src/bg/` och `src/logo.png`

Bygg sedan om sidan med `python src/build.py` och committa både källfilerna och `index.html`.
