# Kshitij Kanade: Portfolio

Personal portfolio site for **Kshitij Kanade**, M.S. Electrical & Computer Engineering (Computer Engineering track) at UC San Diego.

**Live site:** https://psychopomp4266.github.io/kshitij-kanade-portfolio/

The site covers education, research and work experience, projects, leadership, skills, certifications (each linked to its credential) and a resume viewer. It also has a built-in QR code, so anyone can scan it from a phone and open the profile.

## What's in this repo

| Path | Purpose |
|---|---|
| `index.html` | The whole site: page layout, styling and all content in one file |
| `resumes/` | Resume PDFs shown in the Resume tab |
| `make_qr.py` | Script that makes a print-ready QR code (`qr.svg`, `qr.png`) for the live address |
| `.nojekyll` | Tells GitHub Pages to serve the files as they are |

It is a static site with no build step and no framework. GitHub Pages serves `index.html` directly.

## Editing the site

All text, links and lists live in one block near the top of the `<script>` in `index.html`, under the heading `CONTENT`. To change something:

1. Open `index.html` in this repo and click the pencil icon.
2. Find the entry you want (Ctrl+F helps) and edit the text between the quotation marks.
3. Click **Commit changes**. The live site updates within a couple of minutes (use Ctrl+Shift+R to bypass your browser's cache).

Sections you can edit in that block: `PROFILE` (name, tagline, summary, contact, highlights), `EDUCATION`, `EXPERIENCE`, `PROJECTS`, `LEADERSHIP`, `SKILLS`, `CERTS` and `RESUMES`.

**Links:** a link set to `null` shows as a dashed "link to be added" chip. Replace `null` with a web address in quotation marks to turn it into a real link.

**Photo:** upload an image to an `assets/` folder, then set `const PHOTO = "assets/your-photo.jpg";` near the top of the script.

## Adding a role-specific resume

1. Upload the PDF into the `resumes/` folder, for example `resumes/Kshitij_Kanade_VLSI.pdf`.
2. In `index.html`, add a line to the `RESUMES` list:

   ```js
   { id: "vlsi", label: "VLSI / Computer Architecture", file: "resumes/Kshitij_Kanade_VLSI.pdf" }
   ```

3. Commit. A version dropdown appears automatically on the Resume tab.

## Making the QR code

The share button on the site (square-grid icon next to the name) shows a QR code for the page you are viewing. For a print-quality file:

```
pip install segno
python make_qr.py https://psychopomp4266.github.io/kshitij-kanade-portfolio/
```

This writes `qr.svg` (vector, best for print) and `qr.png` (for screens and slides). The QR code holds only the web address, so you can keep editing the site without remaking it. Remake it only if the address changes, such as when the repository is renamed or a custom domain is added.

## Hosting

The site is published with GitHub Pages: **Settings → Pages → Deploy from a branch → `main` / `(root)`**. Any commit to `main` redeploys it.

## Built with

Plain HTML, CSS and JavaScript. Fonts: Bricolage Grotesque, IBM Plex Sans and IBM Plex Mono (Google Fonts). QR generation in the browser uses [qrcode-generator](https://github.com/kazuhikoarase/qrcode-generator).
