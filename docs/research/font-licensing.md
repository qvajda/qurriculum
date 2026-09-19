# Font licensing for fonts inside a sold .docx

Retrieved 2026-09-19. Refs #9, epic #4. Scope: which families the templates may
use, not which they do use (build epic's call).

Two cases, kept apart because the grants differ:
**embed** (font bytes travel inside the sold file: redistribution) vs
**depend** (file names the font, buyer's machine supplies it: no redistribution,
substitution risk only).

Not verified: the `fsType` (OS/2) embedding bit of each font file. No font files
were obtained in this session; Word enforces that bit regardless of the written
licence, so check it before any embed.

## Class A: Microsoft fonts (depend)

Source for the five below, https://learn.microsoft.com/en-us/typography/fonts/font-faq
(Font redistribution FAQ, page dated 2024-11-19), retrieved 2026-09-19. The FAQ
covers fonts "supplied with Windows"; it says of other fonts "Microsoft can't
provide guidance to fonts that we didn't supply."

General rule, quoted:

> Although the redistribution of fonts supplied with Windows is generally not allowed, "document font embedding" is a special case which is allowed in some circumstances.

> If an application follows the rules and restrictions defined in the OpenType or TrueType specification, you can use it to embed Windows supplied fonts in any document file it creates. For example, Microsoft Word and PowerPoint follow the rules and restrictions, so you can use these applications to create documents (such as Word documents, PowerPoint decks and PDFs) that include embedded fonts.

> Apart from the document embedding rights described previously, you may not redistribute the Windows fonts. You may not copy them to other computers or servers, and you may not convert them to other formats, including bitmap formats, or modify them.

Reading: embedding is allowed only by an application (Word) honouring the
`fsType` flag, not by us shipping the font file. So we never bundle the file;
we may name the font. Depending needs no redistribution grant. If the buyer
lacks the font, Word substitutes another.

### Arial, Times New Roman, Georgia
Licence: Microsoft Windows font licence (Windows EULA plus the FAQ above).
Page: https://learn.microsoft.com/en-us/typography/font-list/georgia states
"Font redistribution FAQ for Windows"; extended rights come from Monotype.
The FAQ clause above governs. Depend: yes. Ship the file: no.

### Calibri, Cambria
Licence: Microsoft (Calibri), Tiro Typeworks/Microsoft (Cambria); the font-list
pages https://learn.microsoft.com/en-us/typography/font-list/calibri and
https://learn.microsoft.com/en-us/typography/font-list/cambria point to the same
FAQ. Cambria's page says:

> These Microsoft fonts can be licensed from Tiro Typeworks or Monotype for a range of uses, including individual device use outside of Microsoft products, webfonts, app embedding, enterprise computing and server installations, and hardware and software redistribution.

Ships with Office; the FAQ's own scope is Windows-supplied fonts, so the clause
applies to Calibri/Cambria by the font-list page's pointer, not by their text.
Depend: yes. Ship the file: no.

### Aptos
Source: https://learn.microsoft.com/en-us/typography/font-list/aptos, retrieved 2026-09-19.

> This typeface is available within Office applications. For more information visit Cloud fonts in Office.

Aptos is a cloud font delivered inside Microsoft 365. No clause found that
permits redistribution, and a buyer without Microsoft 365 may not have it. No
clause permitting either case was found: excluded.

## Class B: open licence (embed)

Licence for both: SIL Open Font License 1.1 (26 February 2007). Grant, quoted from
the licence text shipped with each family:

> Permission is hereby granted, free of charge, to any person obtaining a copy of the Font Software, to use, study, copy, merge, embed, modify, redistribute, and sell modified and unmodified copies of the Font Software, subject to the following conditions:

> 1) Neither the Font Software nor any of its individual components, in Original or Modified Versions, may be sold by itself.

> 2) Original or Modified Versions of the Font Software may be bundled, redistributed and/or sold with any software, provided that each copy contains the above copyright notice and this license.

A sold `.docx` is a document bundling the font, not the font sold by itself, so
condition 1 is met; condition 2 requires the copyright notice and licence text to
travel with the bundle, so ship them alongside the templates (e.g. in the
product's licence file). Do not modify or subset-rename the font under the
Reserved Font Name.

### Lato
Copyright (c) 2010-2014 by tyPoland Lukasz Dziedzic, Reserved Font Name "Lato".
Source: https://raw.githubusercontent.com/google/fonts/main/ofl/lato/OFL.txt,
retrieved 2026-09-19. Embed: yes (OFL 1.1 above). Depend: yes.

### EB Garamond
Copyright 2017 The EB Garamond Project Authors, https://github.com/octaviopardo/EBGaramond12.
Source: https://raw.githubusercontent.com/google/fonts/main/ofl/ebgaramond/OFL.txt,
retrieved 2026-09-19. Embed: yes (OFL 1.1 above). Depend: yes.

## Conclusion

MAY EMBED: Lato, EB Garamond
MAY DEPEND ON, MUST NOT EMBED: Arial, Times New Roman, Georgia, Calibri, Cambria
EXCLUDED: Aptos (cloud font, no clause found permitting redistribution)

Caveats: web licences are a different grant and were not used here; a Word-made
embed of a Microsoft font is governed by its `fsType` bit, unchecked.
