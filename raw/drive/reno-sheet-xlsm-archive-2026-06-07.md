# 02 Reno Sheet.xlsm (archived binary spreadsheet — metadata only)

**Source:** Google Drive → 04 Renovation / 0 Archive  
**File ID:** `1u1VyORHiyh6bZEH2M-RMw5fzFmJbQTL-`  
**Folder path:** 04 Renovation / 0 Archive /  
**Pulled:** 2026-06-07  
**Owner:** mc.risye@gmail.com  
**MIME type:** `application/vnd.ms-excel.sheet.macroenabled.12` (Excel macro-enabled workbook, .xlsm)  
**File size:** 430,500 bytes  
**Created:** 2026-03-28  
**Last modified (Drive):** 2026-06-02  

---

## Content

**NOT EXTRACTABLE via available read-only MCP tools — metadata-only snapshot.**

`read_file_content` failed with: *"File content cannot be retrieved for item
1u1VyORHiyh6bZEH2M-RMw5fzFmJbQTL- due to unsupported mime type. Try using `download_file_content`
to see if the file contents can be downloaded and decoded."*

`download_file_content` (with `exportMimeType: "text/csv"`) was attempted as a fallback. The
result (574,144 characters, saved to a temp file due to exceeding token limits) was inspected
via `python3` + `base64` decoding: the decoded bytes begin with the ZIP magic number `PK\x03\x04`
and contain internal paths like `xl/worksheets/sheet1.xml` — confirming this is the **raw,
unmodified XLSM binary file**, base64-encoded, NOT a CSV/text export. `download_file_content`
silently IGNORES the `exportMimeType` parameter for non-Google-native binary files and returns
the original file bytes verbatim.

**Conclusion:** This file's structured content cannot be extracted as natural-language text via
the available read-only Drive MCP tools (`read_file_content` / `download_file_content`). Proper
extraction would require either (a) opening the file in Excel/a spreadsheet tool capable of
parsing .xlsm binaries, or (b) Google Drive converting it to a native Sheets format first
(outside Ingestion's read-only scope — would require `copy_file`/`create_file`, which Ingestion
must NOT call).

**Likely content:** Based on the filename ("02 Reno Sheet.xlsm") and folder location (0 Archive),
this is very likely an OLDER/ARCHIVED VERSION of the Bud Studio Reno Sheet — the same document
already pulled in its live Google Sheets form as `raw/sheets/reno-sheet-bud-studio-2026-06-07.md`
(File ID `1cFfCsIXtQXqY4kU2dRp13rjjI5XJjmovX8wiUKnvV78`, "02 Reno Sheet x Bud Studio [External]").
The "x Bud Studio [External]" live sheet is the authoritative/current version; this .xlsm is
likely a stale snapshot/export retained for archival purposes. No further extraction attempted —
recording metadata here is sufficient for traceability; the Extractor/Compiler should treat the
live Google Sheets version as authoritative.

**View URL:** https://drive.google.com/file/d/1u1VyORHiyh6bZEH2M-RMw5fzFmJbQTL-/view?usp=drivesdk
