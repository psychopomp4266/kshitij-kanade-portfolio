# Kshitij Kanade: portfolio site

A static site. `index.html` holds the page and all of its content, `resumes/` holds the PDFs.

## Before you publish
1. Replace `resumes/Kshitij_Kanade_Master.pdf` with a corrected copy. The current file still has your phone number and the original typos.
2. Open `index.html`, find the content block near the top of the `<script>`, and fill in:
   - `PHOTO` (for example `"assets/photo.jpg"`, with the file added in an `assets/` folder)
   - the Maintenance Script repo link and the Edge Impulse certificate link (currently `null`)
   - the railgun and Vajra certificate links, which currently point to the same file

## Deploy on GitHub Pages
1. On github.com, create a **public** repository. Naming it `psychopomp4266.github.io` gives you the short address `https://psychopomp4266.github.io`.
2. Upload everything in this folder (including the `resumes/` folder) to the repository root.
3. Go to Settings → Pages. Under Build and deployment, choose "Deploy from a branch", pick `main` and `/ (root)`, and save.
4. After about a minute the site is live at the address Pages shows.

## Make the QR code
    pip install segno
    python make_qr.py https://psychopomp4266.github.io

Use `qr.svg` for print and `qr.png` for screens. The QR holds only the web address, so you can edit the site any time without remaking it.

## Add a role-specific resume later
1. Put the PDF in `resumes/`, for example `resumes/Kshitij_Kanade_VLSI.pdf`.
2. In `index.html`, add a line to the `RESUMES` list:
   `{ id: "vlsi", label: "VLSI / Computer Architecture", file: "resumes/Kshitij_Kanade_VLSI.pdf" }`
