# Etsy: delivery mechanism for the digital download

Refs #10. All sources are Etsy's own pages, read in a browser on 2026-10-12.
Earlier automated runs got HTTP 403 from `help.etsy.com`. A real browser
session did not.

- Seller page: <https://help.etsy.com/hc/en-us/articles/115015628347-How-to-Manage-Your-Digital-Listings>
- Buyer page: <https://help.etsy.com/hc/en-us/articles/115013328108-How-to-Download-a-Digital-Item>
- Seller Policy: <https://www.etsy.com/legal/sellers>

## Mechanisms Etsy documents

Etsy names two kinds of digital item:

> Instant downloads: Ready-made files that the buyer can access immediately upon purchase
>
> Made-to-order downloads: Custom files made to a buyer's specification that will be sent to them upon completion.

Source: the seller page, retrieved 2026-10-12.

1. **Instant download.** The seller uploads the files to the listing, and Etsy
   releases them when payment is confirmed.
2. **Made-to-order download.** No file is attached to the listing. The seller
   uploads the files when they mark the order complete, and Etsy emails the
   buyer.
3. **External host or licence-key flow: not documented by Etsy.** I found no
   Etsy page describing delivery through a link to an outside host or a
   licence-key service. The Seller Policy
   (<https://www.etsy.com/legal/sellers>, retrieved 2026-10-12) mentions
   "digitally delivered items" only to say that listings must offer an item
   for sale. It describes no route outside Etsy's own file delivery.

## Limits: instant download

File size: 20MB per file. Etsy states no per-listing total, so the effective
maximum is 5 × 20MB.
"You can upload up to five digital files. The maximum size for each file is 20MB."
Source: <https://help.etsy.com/hc/en-us/articles/115015628347-How-to-Manage-Your-Digital-Listings>, retrieved 2026-10-12.

File count: up to 5 files per listing. A listing needs at least one file
before it can be published or saved.
Source: <https://help.etsy.com/hc/en-us/articles/115015628347-How-to-Manage-Your-Digital-Listings>, retrieved 2026-10-12.

File types: `.bmp .doc .gif .jpeg .jpg .mobi .mov .mp3 .mpeg .pdf .png .psp .rtf .stl .txt .zip .ePUB .iBook`.
**`.docx` is not on the list.** `.doc` and `.zip` are. File names are limited to 70
alphanumeric characters, periods, underscores or hyphens, and cannot be renamed
after upload.
Source: <https://help.etsy.com/hc/en-us/articles/115015628347-How-to-Manage-Your-Digital-Listings>
(the "Supported file types" section is collapsed by default), retrieved 2026-10-12.

Post-sale replacement: the seller can swap a listing's files by removing them
(X) and adding new ones in the listing editor. Etsy does not document what a
buyer who already paid then receives: the original file or the new one.
That part is **not documented**. The buyer page says only that "Download Files"
opens "the Downloads page for all the files attached to your order" and that
there are "generally no limits for when or how many times you can download a
file". Revoking access is documented: "Canceling an order is the only way to
revoke a buyer's access to a file after it has been purchased."
Sources: <https://help.etsy.com/hc/en-us/articles/115015628347-How-to-Manage-Your-Digital-Listings>,
<https://help.etsy.com/hc/en-us/articles/115013328108-How-to-Download-a-Digital-Item>, both retrieved 2026-10-12.

Other limits: digital items cannot have variations, and the seller page says so.
Buyers cannot download through the Etsy app, only in a browser, as the buyer page says.

## Limits: made-to-order download

The same cap applies: "You can attach up to five files with a maximum size of
20MB each". Files are uploaded per order at completion, so each order is
handled by hand. Replacement after sale is not documented for this route either.
Source: <https://help.etsy.com/hc/en-us/articles/115015628347-How-to-Manage-Your-Digital-Listings>, retrieved 2026-10-12.

## Choice

Mechanism: Etsy instant download, with one `.zip` holding the `.docx` and a how-to `.pdf`.

The `.zip` is required, because `.docx` is not an accepted type. This is a finding
against ADR-0001 D-1, which makes `.docx` the sold artifact. The artifact is
still the `.docx`, but it cannot be uploaded bare and has to travel inside the
`.zip`. The package #6 proposed (`CV.docx` + `how-to.pdf` in one ZIP) is
therefore required, not just conventional. Etsy's buyer page already explains
ZIP extraction to buyers. A generated `.docx` plus a short PDF sits far below
20MB, and one ZIP uses 1 of the 5 file slots.

Made-to-order is ruled out because it needs a seller action on every order.
That is incompatible with an automated batch of identical files.
D-10 is unaffected: uploading the ZIP is part of building the draft listing, and
nothing here touches the live account. The AI-disclosure constraint
(`docs/constraints/etsy-ai-disclosure.md`) concerns a listing field, not the
file delivery, so it does not interact with this choice.

## Open

- **Post-sale updates.** Whether an existing buyer receives a replaced file is
  undocumented. Do not promise "free updates" in listing copy until a test order
  on a draft-then-live listing settles it. That test is outside this row (D-10).
- **`.docx` upload.** The uploader may accept `.docx` even though the help page
  omits it. That is unverified, and the ZIP makes the question moot.
