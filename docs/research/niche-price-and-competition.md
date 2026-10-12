# Price point and competition depth in the compound niche

Refs #8. All figures read 2026-10-12 from etsy.com in a browser session located in
Belgium (`region: BE`, locale currency EUR). Every listing price below is the EUR
price Etsy displayed to that visitor; the listing's native currency was not recorded,
so the conversion is Etsy's own, at Etsy's rate, on 2026-10-12.

The July 2026 Notion figures (~125K monthly searches, $5-20 average price, ~40% less
competition, ~20% higher price in niche templates) are the **prior being tested**.
They are provenance, not measurement, and nothing below restates them.

## Headline finding: the compound niche has no occupant

No listing in any probe matched all three axes (country format x language x job
domain). Every trio's compound query returned Etsy's fuzzy match of generic
English-language resume templates, with at most one or two listings matching two
axes. The prices below are therefore the **nearest occupants** of each trio: listings
returned by the trio's compound queries that match its language/country, or its job
domain, named per listing. Listings matching neither were excluded, so the price point
is not the broad `resume template` price.

## Competition depth

Etsy reports an exact count up to 999 and `1,000+ items` above that, so the broad
denominator is a lower bound, not a number.

| Trio | Compound query (verbatim) | Result count | Broad `resume template` | Ratio |
|---|---|---|---|---|
| BE:FR x analytics/finance | `cv belge finance` | 858 | 1,000+ | not reported |
| BE:FR x analytics/finance | `cv belgique analyste` | 665 | 1,000+ | not reported |
| DE:DE x engineering | `Lebenslauf Vorlage Ingenieur` | 990 | 1,000+ | not reported |
| NL:NL x marketing | `cv template nederlands marketing` | 993 | 1,000+ | not reported |
| NL:NL x marketing | `cv sjabloon nederlands marketing` | 822 | 1,000+ | not reported |

Sources: `https://www.etsy.com/search?q=<query>` for each query above, and
<https://www.etsy.com/search?q=resume%20template>, all retrieved 2026-10-12.

No ratio is reported: each compound query returned the broad result set (the same
generic listings — e.g. 1266966425, 1464435354, 1619497373 — top every trio), so none
of them was a compound query in effect. The counts measure Etsy's query relaxation,
not competition. The competition finding is qualitative and stronger than a ratio:
**zero dedicated listings** in all three trios in the first page of results.

## Price point

`SALE` = Etsy shows a struck-through original price; the paid price is the sale price.
`STD` = no discount shown. Retrieved 2026-10-12, read from each listing page.

### BE:FR x analytics/finance

| Listing | Shop | Matches | Paid EUR | Standing EUR | Status | Retrieved |
|---|---|---|---|---|---|---|
| <https://www.etsy.com/listing/1699794185> | WinkyWin | French | 4.94 | 12.33 | SALE | 2026-10-12 |
| <https://www.etsy.com/listing/1699797133> | WinkyWin | French | 4.94 | 12.33 | SALE | 2026-10-12 |
| <https://www.etsy.com/listing/4534792712> | OrganiPro | French + finance | 12.10 | 12.10 | STD | 2026-10-12 |
| <https://www.etsy.com/listing/4474973912> | EverydayDigitalDocs | finance | 7.85 | 15.72 | SALE | 2026-10-12 |
| <https://www.etsy.com/listing/4503394800> | TaktStudioDigital | finance | 11.28 | 11.28 | STD | 2026-10-12 |

Median paid: **7.85 EUR**. Median standing: 12.33 EUR. No Belgium-specific listing found
(queries also tried: `modèle cv belgique`, `cv belge`, `cv français finance`,
`cv analyste financier`).

### DE:DE x engineering

| Listing | Shop | Matches | Paid EUR | Standing EUR | Status | Retrieved |
|---|---|---|---|---|---|---|
| <https://www.etsy.com/listing/1385848259> | PinkTieBewerbungen | German | 12.17 | 12.17 | STD | 2026-10-12 |
| <https://www.etsy.com/listing/1691577310> | ElsabeDesign | German | 11.52 | 11.52 | STD | 2026-10-12 |
| <https://www.etsy.com/listing/4383473504> | ZeeWins | German | 3.96 | 9.89 | SALE | 2026-10-12 |
| <https://www.etsy.com/listing/1873473676> | WinkyWin | German | 8.08 | 20.21 | SALE | 2026-10-12 |
| <https://www.etsy.com/listing/4427048130> | ZeeWins | German | 3.96 | 9.89 | SALE | 2026-10-12 |

Median paid: **8.08 EUR**. Median standing: 11.52 EUR. No engineering-specific listing
found (queries also tried: `Lebenslauf Ingenieur`, `Bewerbungsvorlage Ingenieur`).

### NL:NL x marketing

| Listing | Shop | Matches | Paid EUR | Standing EUR | Status | Retrieved |
|---|---|---|---|---|---|---|
| <https://www.etsy.com/listing/1845446165> | WinkyWin | Dutch | 4.94 | 12.33 | SALE | 2026-10-12 |
| <https://www.etsy.com/listing/1644179550> | WinkyWin | Dutch | 4.94 | 12.33 | SALE | 2026-10-12 |
| <https://www.etsy.com/listing/4584337500> | KitoraDesign | Dutch | 4.39 | 5.49 | SALE | 2026-10-12 |
| <https://www.etsy.com/listing/4383253921> | Designbyster | Dutch | 11.00 | 11.00 | STD | 2026-10-12 |
| <https://www.etsy.com/listing/4508474101> | BloomByAliveCo | Dutch | 12.95 | 12.95 | STD | 2026-10-12 |

Median paid: **4.94 EUR**. Median standing: 12.33 EUR. No marketing-specific listing
found; Dutch listings surfaced only under `cv sjabloon nederlands`,
`curriculum vitae nederlands`, `sollicitatie cv` and `motivatiebrief`.

### Across the fifteen

Median paid: **7.85 EUR**. Median standing: 12.17 EUR.

The price point uses the **paid** price, because that is the revenue a sale produces
and D-6 is a revenue floor; the standing-price median is shown so the sale/standing
split is not silent. 9 of 15 listings are on permanent-looking sale (35-75% off), and
one shop (WinkyWin) holds 5 of the 15, so its sale pricing drags every median down.

## Fees

Per sale of a digital listing, for a Belgium-based seller on Etsy Payments:

- Listing fee: $0.20 USD, renewed after each sale of a multi-quantity listing.
  <https://www.etsy.com/legal/fees/>, retrieved 2026-10-12.
- Transaction fee: 6.5% of the displayed price.
  <https://www.etsy.com/legal/fees/>, retrieved 2026-10-12.
- Payment processing, Belgium: 4% + 0.30 EUR.
  <https://www.etsy.com/legal/etsy-payments>, retrieved 2026-10-12.
- $0.20 = 0.18 EUR at the ECB reference rate 1.1206 USD/EUR of 2026-10-09,
  <https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml>, retrieved 2026-10-12.

Not counted: VAT on Etsy's fees, and the Offsite Ads fee on ad-attributed offsite
sales. Both only lower the net figure further.

## Derivation against the EUR 175/month floor (ADR-0001 D-6)

- Gross: 175 / 7.85 = 22.3 sales/month.
- Net per sale: 7.85 x (1 - 0.065 - 0.04) - 0.30 - 0.18 = 6.55 EUR.
- Net: 175 / 6.55 = 26.7 sales/month.

D-6 assumes 12-35 sales/month. At the standing-price median (12.17 EUR, net 10.41 EUR)
the net figure would be 16.8 — also inside the band, but not what buyers pay today.

## What this does not settle

- Whether 27 sales/month is reachable: no listing here exposes its sales count, and
  the compound niche has no occupant whose volume could be read.
- Whether the niche is empty because it is unserved or because it has no buyers.
  Zero competition and zero demand look identical from search results.

PRICE POINT: 7.85 EUR
SALES PER MONTH GROSS: 22.3
SALES PER MONTH NET: 26.7
VERDICT: Inside D-6's 12-35 band — 26.7 net sales/month at a 7.85 EUR price point, in the upper half of it.
