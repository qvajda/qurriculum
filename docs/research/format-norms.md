# What format comparable digital-download shops actually ship

Refs #6. All listings read 2026-10-12 from etsy.com in a browser session located in
Belgium. The sample is the same fifteen listings #8 priced
([niche-price-and-competition.md](niche-price-and-competition.md)), five per trio, so
the two research rows read against one sample frame.

ADR-0001 D-1's editable `.docx` is the **prior under test**. Its basis — a July 2026
Notion pass with no source URL — is provenance, not measurement, and nothing below
leans on it.

## How the delivered files were read

Each listing exposes two things about what the buyer receives:

1. **Etsy's own `Digital file type(s)` field** (Item details). Etsy fills this from the
   uploaded files. Quoted verbatim below. For 13 of 15 listings it reads `ZIP`, which
   names the container and not what is in it.
2. **The seller's statement of contents** in the description (`Fichiers Microsoft
   Word`, `Du erhältst: Microsoft Word (.docx)`, `WAT IS INBEGREPEN`, ...). Quoted below,
   translated where not English.

The classification uses (2) wherever (1) is a bare ZIP. That is the seller's own
contents list, not marketing copy or a preview image, but it is a claim nobody here
has unzipped. No listing was bought. A listing with neither a readable field nor a
contents statement would be `UNREADABLE`; none was.

"PDF" in the class names means a PDF **of the CV itself**. Several listings ship PDFs
that are guides or carriers for editor links; those are named per row and do not
make a listing `DOCX+PDF`.

## Per listing

Classes: `DOCX` (Word source, no CV PDF), `DOCX+PDF` (Word source plus a PDF of the
CV), `PDF-ONLY`, `LINK` (Canva / Google Docs / Figma link, no file source), `OTHER`.

### BE:FR x analytics/finance

| Listing | Shop | Etsy field (verbatim) | Seller-stated contents | Class | Retrieved |
|---|---|---|---|---|---|
| <https://www.etsy.com/listing/1699794185> | WinkyWin | `1 ZIP` | Microsoft Word files + Mac Pages files | DOCX | 2026-10-12 |
| <https://www.etsy.com/listing/1699797133> | WinkyWin | `1 ZIP` | Microsoft Word files + Mac Pages files | DOCX | 2026-10-12 |
| <https://www.etsy.com/listing/4534792712> | OrganiPro | `1 ZIP` | "a PDF file containing the Canva links" to the CV and letter templates; Canva guide | LINK | 2026-10-12 |
| <https://www.etsy.com/listing/4474973912> | EverydayDigitalDocs | `1 ZIP` | Microsoft Word files + Google Docs files/access | DOCX | 2026-10-12 |
| <https://www.etsy.com/listing/4503394800> | TaktStudioDigital | `1 PDF, 1 ZIP` | ZIP: Microsoft Word (.docx files) + Google Docs copy links; PDFs are a strategy guide and a quick-start guide | DOCX | 2026-10-12 |

### DE:DE x engineering

| Listing | Shop | Etsy field (verbatim) | Seller-stated contents | Class | Retrieved |
|---|---|---|---|---|---|
| <https://www.etsy.com/listing/1385848259> | PinkTieBewerbungen | `1 ZIP` | template editable in Microsoft Word or Apple Pages; font links | DOCX | 2026-10-12 |
| <https://www.etsy.com/listing/1691577310> | ElsabeDesign | `1 ZIP` | Microsoft Word files (.docx), DIN A4; "Word only, not Google Docs, Pages, ..." | DOCX | 2026-10-12 |
| <https://www.etsy.com/listing/4383473504> | ZeeWins | `2 ZIP` | Microsoft Word (.docx) + Canva + Apple Pages; application guide (PDF), interview guide (PDF) | DOCX | 2026-10-12 |
| <https://www.etsy.com/listing/1873473676> | WinkyWin | `2 PDF, 1 ZIP` | Microsoft Word, Mac Pages, LibreOffice files + Google Docs + Canva; the two PDFs' contents are not stated | DOCX | 2026-10-12 |
| <https://www.etsy.com/listing/4427048130> | ZeeWins | `3 ZIP` | Microsoft Word (.docx) + Canva + Apple Pages; application guide (PDF), interview guide (PDF) | DOCX | 2026-10-12 |

1873473676 is the one row whose PDFs are not accounted for. Read as `DOCX` because the
ZIP carries the Word source either way; if both PDFs turned out to be the CV and letter,
it would move to `DOCX+PDF` and the verdict below would not change.

### NL:NL x marketing

| Listing | Shop | Etsy field (verbatim) | Seller-stated contents | Class | Retrieved |
|---|---|---|---|---|---|
| <https://www.etsy.com/listing/1845446165> | WinkyWin | `1 ZIP` | Microsoft Word files + Mac Pages files | DOCX | 2026-10-12 |
| <https://www.etsy.com/listing/1644179550> | WinkyWin | `1 ZIP` | Microsoft Word files + Mac Pages files | DOCX | 2026-10-12 |
| <https://www.etsy.com/listing/4584337500> | KitoraDesign | `2 Files` | Microsoft Word files (CV + cover letter) | DOCX | 2026-10-12 |
| <https://www.etsy.com/listing/4383253921> | Designbyster | `1 ZIP` | thank-you card with the Canva link, CV + letter "editable in Canva", instruction PDF | LINK | 2026-10-12 |
| <https://www.etsy.com/listing/4508474101> | BloomByAliveCo | `1 PDF` | "PDF with Canva link" — open, make own copy in Canva | LINK | 2026-10-12 |

## What the fifteen show

- **Word is the floor, not the whole offer.** 12/15 ship a Word source; 10 of those 12
  ship it *alongside* at least one other editor (Mac Pages 8, Google Docs 3, Canva 3,
  LibreOffice 1). Only 2 are Word-only: 1691577310 (which explicitly excludes every
  other editor) and 4584337500.
- **Nobody ships a PDF of the CV.** Zero `DOCX+PDF`, zero `PDF-ONLY`. Every PDF in the
  sample is a guide or a carrier for Canva/Docs links. The buyer exports their own PDF
  (several listings say so: "als PDF speichern", "Save your final document as a
  Standard PDF").
- **The alternative norm is Canva, delivered as a link.** All 3 `LINK` listings are
  Canva, and they cluster in the two French/Dutch trios (BE:FR 1/5, NL:NL 2/5); DE:DE
  has none.
- **Concentration.** WinkyWin holds 5/15 (all `DOCX`, Word + Pages); without it the
  sample is 7 `DOCX` / 3 `LINK` of 10 — still a majority, a thinner one.

## What this does not settle

- What is inside each ZIP. The contents are seller-stated; confirming them means buying.
- Whether D-1 should add Pages, Google Docs or Canva variants. A second editor is the
  norm among the Word-based listings, but that is a build question for the owner, not
  this row's (ADR-0001 is not edited here).

DOCX: 12/15
DOCX+PDF: 0/15
PDF-ONLY: 0/15
LINK: 3/15
OTHER: 0/15
VERDICT: The sample validates D-1's editable `.docx` as the sold artifact — 12/15 ship a Word source and none ships a CV PDF — though 10 of those 12 pair Word with a second editor and the only alternative norm is a Canva link (3/15).
