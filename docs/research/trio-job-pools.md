# Candidate trios ranked by job pool size

Retrieved 2026-10-03. Refs #38, epic #4. Scope: size only. Not Etsy demand or price (#8),
not CV content differences, not build order.

## Method

- **Trio** = `COUNTRY:LANGUAGE:FIELD`, e.g. `BE:FR:OC2`.
- **Job pool** = employed persons aged 15-74, thousands, annual 2024.
- **Field scheme**: ISCO-08 major groups (1-digit, `OC1`-`OC9`, `OC0`) for every
  country. No other occupation scheme is used anywhere in this table.
- **Primary source for every figure**: Eurostat LFS, dataset `lfsa_egais`
  (employed persons by occupation). Language splits use Eurostat
  `lfst_r_lfe2emp` (employed persons by NUTS 2 region). Both 2024 annual. No
  national statistics office was needed: Eurostat covers every country asked for.
- **Countries**: BE, FR, DE, AT, CH, NL, PL, ES, IT, SE, DK, NO, FI (#12's set).
- **Languages**: one working language per country except BE (FR, NL) and CH
  (DE, FR, IT). Minority languages (e.g. SV in FI, CA in ES) are not split out:
  no sourced share was gathered, and D-5 forbids an unsourced one.
- **Language split rule**: trio pool = national ISCO-group count x the language
  region's share of national employment (NUTS 2, source above). Assumes the
  occupation mix inside a region equals the national mix; untested, because
  these Eurostat tables give occupation only nationally.
  - BE: NL = BE2 Flanders (3090.3 of 5056.3 thousand employed), FR = BE3 Wallonia
    (1453.4 of 5056.3). BE1 Brussels (512.6) is bilingual and counted in neither,
    so BE:FR is understated.
  - CH: DE = CH03+CH04+CH05+CH06 (2762.7 of 4829.5), FR = CH01 Lac Leman (843.6),
    IT = CH07 Ticino (164.7). CH02 Espace Mittelland (1058.5) mixes DE and FR and is
    counted in neither, so CH:DE and CH:FR are understated.
- **Ranking**: descending pool. Rank 30 is PL:PL:OC5 at 2140.1 thousand; rank 31 is
  FR:FR:OC1 at 2112.2 thousand.

## LAUNCH SET:

- DE:DE:OC2
- DE:DE:OC3
- FR:FR:OC2
- DE:DE:OC5
- DE:DE:OC4
- FR:FR:OC3
- ES:ES:OC5
- DE:DE:OC7
- ES:ES:OC2
- IT:IT:OC3
- IT:IT:OC5
- FR:FR:OC5
- PL:PL:OC2
- IT:IT:OC2
- IT:IT:OC7
- NL:NL:OC2
- DE:DE:OC9
- IT:IT:OC4
- FR:FR:OC7
- ES:ES:OC3
- ES:ES:OC9
- DE:DE:OC8
- IT:IT:OC9
- PL:PL:OC7
- FR:FR:OC9
- PL:PL:OC3
- ES:ES:OC7
- FR:FR:OC4
- ES:ES:OC4
- PL:PL:OC5

## Ranked table

Fields: `OC1` Managers; `OC2` Professionals; `OC3` Technicians and associate professionals; `OC4` Clerical support workers; `OC5` Service and sales workers; `OC6` Skilled agricultural, forestry and fishery workers; `OC7` Craft and related trades workers; `OC8` Plant and machine operators and assemblers; `OC9` Elementary occupations; `OC0` Armed forces occupations.

| rank | trio | pool (thousand) | national count (thousand) | region share | source | retrieved |
|---|---|---|---|---|---|---|
| 1 | DE:DE:OC2 | 9762.9 | 9762.9 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=DE&isco08=OC2 | 2026-10-03 |
| 2 | DE:DE:OC3 | 8367.2 | 8367.2 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=DE&isco08=OC3 | 2026-10-03 |
| 3 | FR:FR:OC2 | 7097.4 | 7097.4 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=FR&isco08=OC2 | 2026-10-03 |
| 4 | DE:DE:OC5 | 5811.9 | 5811.9 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=DE&isco08=OC5 | 2026-10-03 |
| 5 | DE:DE:OC4 | 5380.5 | 5380.5 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=DE&isco08=OC4 | 2026-10-03 |
| 6 | FR:FR:OC3 | 5168.1 | 5168.1 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=FR&isco08=OC3 | 2026-10-03 |
| 7 | ES:ES:OC5 | 4511.9 | 4511.9 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=ES&isco08=OC5 | 2026-10-03 |
| 8 | DE:DE:OC7 | 4449.6 | 4449.6 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=DE&isco08=OC7 | 2026-10-03 |
| 9 | ES:ES:OC2 | 4318.3 | 4318.3 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=ES&isco08=OC2 | 2026-10-03 |
| 10 | IT:IT:OC3 | 4217.3 | 4217.3 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=IT&isco08=OC3 | 2026-10-03 |
| 11 | IT:IT:OC5 | 4150.8 | 4150.8 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=IT&isco08=OC5 | 2026-10-03 |
| 12 | FR:FR:OC5 | 4141.7 | 4141.7 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=FR&isco08=OC5 | 2026-10-03 |
| 13 | PL:PL:OC2 | 4062.0 | 4062.0 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=PL&isco08=OC2 | 2026-10-03 |
| 14 | IT:IT:OC2 | 3781.4 | 3781.4 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=IT&isco08=OC2 | 2026-10-03 |
| 15 | IT:IT:OC7 | 3157.7 | 3157.7 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=IT&isco08=OC7 | 2026-10-03 |
| 16 | NL:NL:OC2 | 3123.4 | 3123.4 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=NL&isco08=OC2 | 2026-10-03 |
| 17 | DE:DE:OC9 | 3071.9 | 3071.9 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=DE&isco08=OC9 | 2026-10-03 |
| 18 | IT:IT:OC4 | 2894.4 | 2894.4 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=IT&isco08=OC4 | 2026-10-03 |
| 19 | FR:FR:OC7 | 2727.9 | 2727.9 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=FR&isco08=OC7 | 2026-10-03 |
| 20 | ES:ES:OC3 | 2677.5 | 2677.5 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=ES&isco08=OC3 | 2026-10-03 |
| 21 | ES:ES:OC9 | 2641.4 | 2641.4 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=ES&isco08=OC9 | 2026-10-03 |
| 22 | DE:DE:OC8 | 2606.8 | 2606.8 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=DE&isco08=OC8 | 2026-10-03 |
| 23 | IT:IT:OC9 | 2494.7 | 2494.7 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=IT&isco08=OC9 | 2026-10-03 |
| 24 | PL:PL:OC7 | 2436.7 | 2436.7 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=PL&isco08=OC7 | 2026-10-03 |
| 25 | FR:FR:OC9 | 2425.5 | 2425.5 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=FR&isco08=OC9 | 2026-10-03 |
| 26 | PL:PL:OC3 | 2332.0 | 2332.0 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=PL&isco08=OC3 | 2026-10-03 |
| 27 | ES:ES:OC7 | 2315.6 | 2315.6 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=ES&isco08=OC7 | 2026-10-03 |
| 28 | FR:FR:OC4 | 2315.1 | 2315.1 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=FR&isco08=OC4 | 2026-10-03 |
| 29 | ES:ES:OC4 | 2169.6 | 2169.6 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=ES&isco08=OC4 | 2026-10-03 |
| 30 | PL:PL:OC5 | 2140.1 | 2140.1 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=PL&isco08=OC5 | 2026-10-03 |
| 31 | FR:FR:OC1 | 2112.2 | 2112.2 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=FR&isco08=OC1 | 2026-10-03 |
| 32 | DE:DE:OC1 | 1849.1 | 1849.1 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=DE&isco08=OC1 | 2026-10-03 |
| 33 | FR:FR:OC8 | 1794.2 | 1794.2 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=FR&isco08=OC8 | 2026-10-03 |
| 34 | SE:SV:OC2 | 1754.5 | 1754.5 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=SE&isco08=OC2 | 2026-10-03 |
| 35 | NL:NL:OC3 | 1672.9 | 1672.9 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=NL&isco08=OC3 | 2026-10-03 |
| 36 | NL:NL:OC5 | 1632.8 | 1632.8 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=NL&isco08=OC5 | 2026-10-03 |
| 37 | ES:ES:OC8 | 1623.6 | 1623.6 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=ES&isco08=OC8 | 2026-10-03 |
| 38 | PL:PL:OC8 | 1561.2 | 1561.2 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=PL&isco08=OC8 | 2026-10-03 |
| 39 | IT:IT:OC8 | 1503.4 | 1503.4 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=IT&isco08=OC8 | 2026-10-03 |
| 40 | PL:PL:OC4 | 1356.3 | 1356.3 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=PL&isco08=OC4 | 2026-10-03 |
| 41 | PL:PL:OC1 | 1259.4 | 1259.4 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=PL&isco08=OC1 | 2026-10-03 |
| 42 | PL:PL:OC6 | 1024.9 | 1024.9 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=PL&isco08=OC6 | 2026-10-03 |
| 43 | AT:DE:OC2 | 1017.9 | 1017.9 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=AT&isco08=OC2 | 2026-10-03 |
| 44 | SE:SV:OC3 | 953.8 | 953.8 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=SE&isco08=OC3 | 2026-10-03 |
| 45 | IT:IT:OC1 | 929.6 | 929.6 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=IT&isco08=OC1 | 2026-10-03 |
| 46 | DK:DA:OC2 | 879.2 | 879.2 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=DK&isco08=OC2 | 2026-10-03 |
| 47 | ES:ES:OC1 | 859.7 | 859.7 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=ES&isco08=OC1 | 2026-10-03 |
| 48 | SE:SV:OC5 | 851.8 | 851.8 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=SE&isco08=OC5 | 2026-10-03 |
| 49 | BE:NL:OC2 | 850.8 | 1392.0 | 0.611 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=BE&isco08=OC2 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=BE | 2026-10-03 |
| 50 | NO:NO:OC2 | 843.2 | 843.2 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=NO&isco08=OC2 | 2026-10-03 |
| 51 | NL:NL:OC4 | 820.4 | 820.4 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=NL&isco08=OC4 | 2026-10-03 |
| 52 | AT:DE:OC3 | 804.8 | 804.8 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=AT&isco08=OC3 | 2026-10-03 |
| 53 | AT:DE:OC5 | 780.7 | 780.7 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=AT&isco08=OC5 | 2026-10-03 |
| 54 | CH:DE:OC2 | 730.9 | 1277.7 | 0.572 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=CH&isco08=OC2 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=CH | 2026-10-03 |
| 55 | PL:PL:OC9 | 730.2 | 730.2 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=PL&isco08=OC9 | 2026-10-03 |
| 56 | NL:NL:OC9 | 712.2 | 712.2 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=NL&isco08=OC9 | 2026-10-03 |
| 57 | FR:FR:OC6 | 711.7 | 711.7 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=FR&isco08=OC6 | 2026-10-03 |
| 58 | FI:FI:OC2 | 685.1 | 685.1 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=FI&isco08=OC2 | 2026-10-03 |
| 59 | NL:NL:OC7 | 638.6 | 638.6 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=NL&isco08=OC7 | 2026-10-03 |
| 60 | NO:NO:OC5 | 601.8 | 601.8 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=NO&isco08=OC5 | 2026-10-03 |
| 61 | NL:NL:OC1 | 590.7 | 590.7 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=NL&isco08=OC1 | 2026-10-03 |
| 62 | DK:DA:OC5 | 575.9 | 575.9 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=DK&isco08=OC5 | 2026-10-03 |
| 63 | DE:DE:OC6 | 535.7 | 535.7 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=DE&isco08=OC6 | 2026-10-03 |
| 64 | DK:DA:OC3 | 520.9 | 520.9 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=DK&isco08=OC3 | 2026-10-03 |
| 65 | FI:FI:OC5 | 505.2 | 505.2 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=FI&isco08=OC5 | 2026-10-03 |
| 66 | AT:DE:OC7 | 504.2 | 504.2 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=AT&isco08=OC7 | 2026-10-03 |
| 67 | IT:IT:OC6 | 503.9 | 503.9 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=IT&isco08=OC6 | 2026-10-03 |
| 68 | FI:FI:OC3 | 478.4 | 478.4 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=FI&isco08=OC3 | 2026-10-03 |
| 69 | CH:DE:OC3 | 468.7 | 819.4 | 0.572 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=CH&isco08=OC3 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=CH | 2026-10-03 |
| 70 | BE:NL:OC3 | 461.1 | 754.4 | 0.611 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=BE&isco08=OC3 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=BE | 2026-10-03 |
| 71 | NO:NO:OC3 | 436.3 | 436.3 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=NO&isco08=OC3 | 2026-10-03 |
| 72 | SE:SV:OC7 | 431.9 | 431.9 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=SE&isco08=OC7 | 2026-10-03 |
| 73 | AT:DE:OC4 | 426.4 | 426.4 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=AT&isco08=OC4 | 2026-10-03 |
| 74 | ES:ES:OC6 | 417.2 | 417.2 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=ES&isco08=OC6 | 2026-10-03 |
| 75 | BE:NL:OC5 | 408.3 | 668.0 | 0.611 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=BE&isco08=OC5 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=BE | 2026-10-03 |
| 76 | BE:FR:OC2 | 400.1 | 1392.0 | 0.287 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=BE&isco08=OC2 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=BE | 2026-10-03 |
| 77 | NL:NL:OC8 | 389.6 | 389.6 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=NL&isco08=OC8 | 2026-10-03 |
| 78 | CH:DE:OC5 | 359.6 | 628.7 | 0.572 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=CH&isco08=OC5 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=CH | 2026-10-03 |
| 79 | BE:NL:OC4 | 344.7 | 564.0 | 0.611 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=BE&isco08=OC4 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=BE | 2026-10-03 |
| 80 | AT:DE:OC9 | 342.9 | 342.9 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=AT&isco08=OC9 | 2026-10-03 |
| 81 | SE:SV:OC1 | 332.5 | 332.5 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=SE&isco08=OC1 | 2026-10-03 |
| 82 | CH:DE:OC4 | 332.0 | 580.3 | 0.572 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=CH&isco08=OC4 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=CH | 2026-10-03 |
| 83 | SE:SV:OC4 | 307.0 | 307.0 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=SE&isco08=OC4 | 2026-10-03 |
| 84 | DK:DA:OC9 | 303.0 | 303.0 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=DK&isco08=OC9 | 2026-10-03 |
| 85 | BE:NL:OC7 | 282.5 | 462.3 | 0.611 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=BE&isco08=OC7 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=BE | 2026-10-03 |
| 86 | SE:SV:OC8 | 279.5 | 279.5 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=SE&isco08=OC8 | 2026-10-03 |
| 87 | BE:NL:OC9 | 279.4 | 457.1 | 0.611 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=BE&isco08=OC9 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=BE | 2026-10-03 |
| 88 | CH:DE:OC7 | 253.7 | 443.5 | 0.572 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=CH&isco08=OC7 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=CH | 2026-10-03 |
| 89 | FI:FI:OC7 | 246.6 | 246.6 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=FI&isco08=OC7 | 2026-10-03 |
| 90 | BE:NL:OC1 | 245.3 | 401.4 | 0.611 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=BE&isco08=OC1 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=BE | 2026-10-03 |
| 91 | NO:NO:OC7 | 238.8 | 238.8 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=NO&isco08=OC7 | 2026-10-03 |
| 92 | CH:DE:OC1 | 238.5 | 417.0 | 0.572 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=CH&isco08=OC1 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=CH | 2026-10-03 |
| 93 | AT:DE:OC8 | 236.0 | 236.0 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=AT&isco08=OC8 | 2026-10-03 |
| 94 | IT:IT:OC0 | 234.5 | 234.5 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=IT&isco08=OC0 | 2026-10-03 |
| 95 | AT:DE:OC1 | 230.7 | 230.7 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=AT&isco08=OC1 | 2026-10-03 |
| 96 | SE:SV:OC9 | 224.3 | 224.3 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=SE&isco08=OC9 | 2026-10-03 |
| 97 | CH:FR:OC2 | 223.2 | 1277.7 | 0.175 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=CH&isco08=OC2 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=CH | 2026-10-03 |
| 98 | NO:NO:OC1 | 221.9 | 221.9 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=NO&isco08=OC1 | 2026-10-03 |
| 99 | BE:FR:OC3 | 216.8 | 754.4 | 0.287 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=BE&isco08=OC3 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=BE | 2026-10-03 |
| 100 | DK:DA:OC4 | 213.2 | 213.2 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=DK&isco08=OC4 | 2026-10-03 |
| 101 | DK:DA:OC7 | 210.1 | 210.1 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=DK&isco08=OC7 | 2026-10-03 |
| 102 | BE:FR:OC5 | 192.0 | 668.0 | 0.287 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=BE&isco08=OC5 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=BE | 2026-10-03 |
| 103 | FR:FR:OC0 | 191.3 | 191.3 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=FR&isco08=OC0 | 2026-10-03 |
| 104 | FI:FI:OC8 | 186.5 | 186.5 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=FI&isco08=OC8 | 2026-10-03 |
| 105 | FI:FI:OC9 | 183.4 | 183.4 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=FI&isco08=OC9 | 2026-10-03 |
| 106 | BE:NL:OC8 | 171.9 | 281.2 | 0.611 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=BE&isco08=OC8 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=BE | 2026-10-03 |
| 107 | DE:DE:OC0 | 164.3 | 164.3 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=DE&isco08=OC0 | 2026-10-03 |
| 108 | NO:NO:OC4 | 163.0 | 163.0 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=NO&isco08=OC4 | 2026-10-03 |
| 109 | BE:FR:OC4 | 162.1 | 564.0 | 0.287 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=BE&isco08=OC4 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=BE | 2026-10-03 |
| 110 | NO:NO:OC8 | 161.2 | 161.2 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=NO&isco08=OC8 | 2026-10-03 |
| 111 | CH:DE:OC9 | 159.8 | 279.3 | 0.572 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=CH&isco08=OC9 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=CH | 2026-10-03 |
| 112 | PL:PL:OC0 | 158.3 | 158.3 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=PL&isco08=OC0 | 2026-10-03 |
| 113 | CH:FR:OC3 | 143.1 | 819.4 | 0.175 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=CH&isco08=OC3 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=CH | 2026-10-03 |
| 114 | NL:NL:OC6 | 138.7 | 138.7 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=NL&isco08=OC6 | 2026-10-03 |
| 115 | DK:DA:OC8 | 134.1 | 134.1 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=DK&isco08=OC8 | 2026-10-03 |
| 116 | BE:FR:OC7 | 132.9 | 462.3 | 0.287 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=BE&isco08=OC7 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=BE | 2026-10-03 |
| 117 | BE:FR:OC9 | 131.4 | 457.1 | 0.287 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=BE&isco08=OC9 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=BE | 2026-10-03 |
| 118 | FI:FI:OC4 | 128.3 | 128.3 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=FI&isco08=OC4 | 2026-10-03 |
| 119 | AT:DE:OC6 | 121.6 | 121.6 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=AT&isco08=OC6 | 2026-10-03 |
| 120 | BE:FR:OC1 | 115.4 | 401.4 | 0.287 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=BE&isco08=OC1 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=BE | 2026-10-03 |
| 121 | CH:FR:OC5 | 109.8 | 628.7 | 0.175 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=CH&isco08=OC5 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=CH | 2026-10-03 |
| 122 | NO:NO:OC9 | 105.9 | 105.9 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=NO&isco08=OC9 | 2026-10-03 |
| 123 | CH:FR:OC4 | 101.4 | 580.3 | 0.175 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=CH&isco08=OC4 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=CH | 2026-10-03 |
| 124 | CH:DE:OC8 | 99.7 | 174.3 | 0.572 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=CH&isco08=OC8 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=CH | 2026-10-03 |
| 125 | ES:ES:OC0 | 99.4 | 99.4 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=ES&isco08=OC0 | 2026-10-03 |
| 126 | FI:FI:OC1 | 89.5 | 89.5 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=FI&isco08=OC1 | 2026-10-03 |
| 127 | DK:DA:OC1 | 85.4 | 85.4 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=DK&isco08=OC1 | 2026-10-03 |
| 128 | BE:FR:OC8 | 80.8 | 281.2 | 0.287 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=BE&isco08=OC8 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=BE | 2026-10-03 |
| 129 | SE:SV:OC6 | 78.7 | 78.7 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=SE&isco08=OC6 | 2026-10-03 |
| 130 | CH:FR:OC7 | 77.5 | 443.5 | 0.175 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=CH&isco08=OC7 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=CH | 2026-10-03 |
| 131 | FI:FI:OC6 | 73.1 | 73.1 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=FI&isco08=OC6 | 2026-10-03 |
| 132 | CH:FR:OC1 | 72.8 | 417.0 | 0.175 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=CH&isco08=OC1 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=CH | 2026-10-03 |
| 133 | NO:NO:OC6 | 56.5 | 56.5 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=NO&isco08=OC6 | 2026-10-03 |
| 134 | CH:DE:OC6 | 55.5 | 97.1 | 0.572 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=CH&isco08=OC6 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=CH | 2026-10-03 |
| 135 | CH:FR:OC9 | 48.8 | 279.3 | 0.175 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=CH&isco08=OC9 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=CH | 2026-10-03 |
| 136 | DK:DA:OC6 | 44.2 | 44.2 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=DK&isco08=OC6 | 2026-10-03 |
| 137 | CH:IT:OC2 | 43.6 | 1277.7 | 0.034 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=CH&isco08=OC2 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=CH | 2026-10-03 |
| 138 | BE:NL:OC6 | 34.4 | 56.3 | 0.611 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=BE&isco08=OC6 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=BE | 2026-10-03 |
| 139 | CH:FR:OC8 | 30.4 | 174.3 | 0.175 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=CH&isco08=OC8 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=CH | 2026-10-03 |
| 140 | NL:NL:OC0 | 28.8 | 28.8 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=NL&isco08=OC0 | 2026-10-03 |
| 141 | CH:IT:OC3 | 27.9 | 819.4 | 0.034 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=CH&isco08=OC3 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=CH | 2026-10-03 |
| 142 | CH:IT:OC5 | 21.4 | 628.7 | 0.034 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=CH&isco08=OC5 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=CH | 2026-10-03 |
| 143 | CH:IT:OC4 | 19.8 | 580.3 | 0.034 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=CH&isco08=OC4 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=CH | 2026-10-03 |
| 144 | SE:SV:OC0 | 19.2 | 19.2 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=SE&isco08=OC0 | 2026-10-03 |
| 145 | CH:FR:OC6 | 17.0 | 97.1 | 0.175 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=CH&isco08=OC6 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=CH | 2026-10-03 |
| 146 | BE:FR:OC6 | 16.2 | 56.3 | 0.287 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=BE&isco08=OC6 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=BE | 2026-10-03 |
| 147 | CH:IT:OC7 | 15.1 | 443.5 | 0.034 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=CH&isco08=OC7 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=CH | 2026-10-03 |
| 148 | CH:IT:OC1 | 14.2 | 417.0 | 0.034 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=CH&isco08=OC1 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=CH | 2026-10-03 |
| 149 | DK:DA:OC0 | 13.0 | 13.0 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=DK&isco08=OC0 | 2026-10-03 |
| 150 | BE:NL:OC0 | 11.8 | 19.3 | 0.611 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=BE&isco08=OC0 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=BE | 2026-10-03 |
| 151 | AT:DE:OC0 | 11.5 | 11.5 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=AT&isco08=OC0 | 2026-10-03 |
| 152 | CH:IT:OC9 | 9.5 | 279.3 | 0.034 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=CH&isco08=OC9 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=CH | 2026-10-03 |
| 153 | FI:FI:OC0 | 8.9 | 8.9 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=FI&isco08=OC0 | 2026-10-03 |
| 154 | NO:NO:OC0 | 8.2 | 8.2 | 1.000 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=NO&isco08=OC0 | 2026-10-03 |
| 155 | CH:IT:OC8 | 5.9 | 174.3 | 0.034 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=CH&isco08=OC8 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=CH | 2026-10-03 |
| 156 | BE:FR:OC0 | 5.5 | 19.3 | 0.287 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=BE&isco08=OC0 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=BE | 2026-10-03 |
| 157 | CH:IT:OC6 | 3.3 | 97.1 | 0.034 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=CH&isco08=OC6 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=CH | 2026-10-03 |
| 158 | CH:DE:OC0 | 2.8 | 4.9 | 0.572 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=CH&isco08=OC0 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=CH | 2026-10-03 |
| 159 | CH:FR:OC0 | 0.9 | 4.9 | 0.175 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=CH&isco08=OC0 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=CH | 2026-10-03 |
| 160 | CH:IT:OC0 | 0.2 | 4.9 | 0.034 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_egais?sex=T&age=Y15-74&wstatus=EMP&time=2024&unit=THS_PER&geo=CH&isco08=OC0 ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfst_r_lfe2emp?sex=T&age=Y15-74&time=2024&unit=THS_PER&geo=CH | 2026-10-03 |
