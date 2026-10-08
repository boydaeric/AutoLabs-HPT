# Review conventions

These rules apply to every file in `./review/`.

## 1. Findings get IDs

* Number findings `F-001`, `F-002`, … in the order they are first written. Never reuse or renumber an ID. A withdrawn finding keeps its ID and is marked withdrawn.
* Cite a finding by its ID everywhere else (comments, the draft, other roles' files).

## 2. Each role writes only its own file

* A role creates and edits only the files it owns. It never edits, reformats or deletes another role's file.
* To respond to another role's file, write in your own file and cite the other file and the item (finding ID, section or line).
* Current ownership:

| File | Owner |
|---|---|
| `review/CONVENTIONS.md` | Editor (changes only on the editor's instruction) |
| `review/article_draft.md` | Author |
| `review/findings.csv`, `review/findings.md` | Comment analyst (public-comment evidence) |

A new role adds a row here only through the editor.

## 3. Counts state as-filed and corrected docket totals

* Every count of comments gives both docket views:
  * **as filed**: the docket the comment carries on regulations.gov
  * **corrected**: after moving letters filed in the wrong docket (`docket_corrections.csv`; today only `CMS-2026-2476-0199`, a CMS-2449-P letter filed under CMS-2452-P)
* Write it as "N as filed / M corrected". When the two are equal, say so ("N in both views").
* Say whether a count covers all comments or distinct texts (campaign copies counted once).
* Keyword-match counts that were not read one by one are approximate. Round them and hedge them ("about 120").

## 4. Commenter estimates are labeled advocacy figures

* Any number a commenter produced itself, rather than quoting CMS, CBO or another named source, is labeled **advocacy figure**. Give its unit and period, and say who produced it.
* A commenter's restatement of a CMS, CBO or other figure is labeled with the original source ("CMS figure, as quoted by …"). Check that the restatement matches before relying on it.

## 5. Quotes

* A quote is verbatim and at most 24 words. Mark a cut with `…`.
* Use at most one quote per source (one comment, letter or document) across a file. Paraphrase anything else from that source.
* Every quote carries its source ID (for comments, the regulations.gov comment ID) and, where the source has pages, a page.

## Departures

* **Repeated quotes from one source.** The verification notes (October 8, 2026) in `review/findings.csv`, `review/findings.md` and `review/findings_v16_unmapped.csv` quote CMS-2452-P more than once, in F-005, F-006, F-007, F-011, F-015 and U-3, because the verification request asked for exact wording in each note. This departs from the one-quote-per-source rule in section 5. Each quote is verbatim and at most 24 words.
* **Idaho quote not checked word for word.** The quotation from Idaho Code § 56-1404(4) in the F-022 verification note came through a web-fetch tool that returns extracted text, so it was not compared word for word with the statute. Every other verification-note quote was matched by script against the downloaded source document.
