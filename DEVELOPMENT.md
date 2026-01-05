# Development Log: Hobonichi 5-Year Digital Journal

This document outlines all the steps taken to create this project from scratch.

## Project Overview

Creating a digital version of the Hobonichi 5-Year Techo for Notesnook as a single markdown file.

---

## Step 1: Research Phase

### Researched Hobonichi Format
- Searched for "Hobonichi 5-Year Techo format layout structure"
- Key findings:
  - Left page: Same date across 5 years (5 rows)
  - Right page: Graph paper memo space
  - A6 size: 178 graph-paper squares per day
  - A5 size: 352 graph-paper squares per day
  - Additional pages: Yearly calendars, My Lists, My Favorites, Gifts, Personal Notes
- Source: [Hobonichi Official](https://www.1101.com/store/techo/en/5year/)

### Researched Notesnook Capabilities
- Searched for "Notesnook templates markdown features 2026"
- Key findings:
  - Supports markdown shortcuts (not raw markdown)
  - Can import markdown files via Settings → Notesnook Importer
  - Copy/paste markdown directly has limitations
  - Works well with single large files
- Source: [Notesnook Help](https://help.notesnook.com/)

---

## Step 2: Initial Script Development

### Created Python Generator Script
**File:** `generate_hobonichi_5year.py`

**Features implemented:**
```python
- 366 daily entries (including Feb 29 for leap years)
- 5-year format (2026-2030 by default)
- Automatic day-of-week calculation for each year
- Monthly organization
- Additional sections:
  - Yearly Overview
  - My Lists (5 sections)
  - My Favorite Things (9 categories)
  - Gifts tracker (table format by year)
  - Personal Notes (7 sections)
```

**Initial structure per day:**
```markdown
### January 1

**2026** (Thursday)


**2027** (Friday)


... (all 5 years)

**Memo**


---
```

### Generated First Version
```bash
python3 generate_hobonichi_5year.py
```
- Output: `Hobonichi_5Year_2026-2030.md`
- Size: 53,739 characters

---

## Step 3: User Feedback & Improvements

### Adjustment: Added Empty Lines
**User request:** "adjust the template so it contains 'enter' (empty line) under each date"

**Changes made to script:**
1. Added `&nbsp;` (non-breaking space) under each year entry
2. Added `&nbsp;` under the Memo section

**Modified code:**
```python
# Before
f.write(f"**{year}** ({specific_dow})\n\n")
f.write("\n\n")

# After
f.write(f"**{year}** ({specific_dow})\n\n")
f.write("&nbsp;\n\n")  # Empty line for writing
f.write("\n")
```

**Regenerated file:**
```bash
python3 generate_hobonichi_5year.py
```
- New size: 69,111 characters

---

## Step 4: Documentation

### Created README.md
**Content included:**
- Project description and inspiration
- Features list
- Quick start guide (2 options: use pre-generated or generate custom)
- Usage instructions for Notesnook
- Tips for journaling
- Structure overview
- Why Notesnook section
- Contributing guidelines
- License information
- Related links

### Created LICENSE
- Chose **MIT License** for maximum permissiveness with attribution
- Allows commercial use, modification, distribution, private use
- Only requires keeping copyright notice

### Created .gitignore
**Included:**
- Python artifacts (`__pycache__/`, `*.pyc`, `venv/`, etc.)
- IDE files (`.vscode/`, `.idea/`, `.DS_Store`)
- Optional: commented out markdown files in case user wants to exclude generated files

---

## Step 5: Project Organization

### Organized Files into Project Directory
```bash
mkdir -p hobonichi-digital-journal
mv generate_hobonichi_5year.py \
   Hobonichi_5Year_2026-2030.md \
   LICENSE \
   README.md \
   .gitignore \
   hobonichi-digital-journal/
```

**Final structure:**
```
hobonichi-digital-journal/
├── .gitignore
├── LICENSE
├── README.md
├── generate_hobonichi_5year.py
└── Hobonichi_5Year_2026-2030.md
```

---

## Step 6: Git Repository Setup

### Initialize Git Repository
```bash
cd hobonichi-digital-journal
git init
```
- Created `.git/` directory
- Default branch: `master`

### Stage All Files
```bash
git add -A
```
**Files staged:**
- `.gitignore`
- `LICENSE`
- `README.md`
- `generate_hobonichi_5year.py`
- `Hobonichi_5Year_2026-2030.md`

### Create Initial Commit
```bash
git commit -m "$(cat <<'EOF'
Initial commit: Hobonichi 5-Year Digital Journal for Notesnook

- Add Python script to generate 5-year journal markdown
- Include pre-generated 2026-2030 journal file
- Add comprehensive README with usage instructions
- Add MIT license
- Add .gitignore for Python projects

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
EOF
)"
```
- Commit hash: `ac84511`
- 5 files changed, 12,948 insertions(+)

---

## Step 7: GitHub Integration

### Add Remote Repository
```bash
git remote add origin https://github.com/jaal/hobonichi-digital-journal.git
```

### Verify Remote
```bash
git remote -v
```
Output:
```
origin  https://github.com/jaal/hobonichi-digital-journal.git (fetch)
origin  https://github.com/jaal/hobonichi-digital-journal.git (push)
```

### Rename Branch to Main
```bash
git branch -M main
```
- Changed from `master` to `main` (modern convention)

### Push to GitHub
```bash
git push -u origin main
```
- Created new branch `main` on GitHub
- Set up tracking branch
- All files successfully pushed

---

## Step 8: Documentation of Process

### Created DEVELOPMENT.md
This file! Documents all steps taken to create the project.

---

## Technical Details

### Python Script Functionality

**Key functions:**
1. `generate_hobonichi_markdown(start_year, output_file)`
   - Generates complete 5-year journal
   - Customizable start year
   - Customizable output filename

**Date handling:**
- Uses Python's `datetime` module
- Handles leap years (Feb 29)
- Calculates correct day of week for each year
- Base year 2024 used for month/day reference (leap year)

**Output format:**
- UTF-8 encoding
- Markdown format optimized for Notesnook
- `&nbsp;` for visual empty lines
- `---` horizontal rules for separation
- Headers: `#`, `##`, `###`, `####` hierarchy
- Tables for gift tracking

### File Sizes
- Script: ~4.3 KB
- Generated markdown: ~69 KB
- README: ~4.1 KB
- LICENSE: ~1.1 KB
- Total project: ~78.5 KB

---

## Future Customization Options

### Easy Customizations
1. **Change start year:**
   ```python
   generate_hobonichi_markdown(start_year=2025)  # Line 114
   ```

2. **Change output filename:**
   ```python
   generate_hobonichi_markdown(start_year=2026,
                               output_file="MyJournal.md")
   ```

3. **Modify additional sections:**
   - Edit lists in `favorite_categories` (line 80-82)
   - Edit `personal_sections` (line 100-102)
   - Add/remove gift tracker years

### Advanced Customizations
- Add custom headers/footers
- Include additional template sections
- Modify spacing/formatting
- Add metadata or tags
- Create multiple language versions

---

## Lessons Learned

1. **Single file approach:** Better for Notesnook import than multiple files
2. **Empty lines matter:** `&nbsp;` provides better visual separation in markdown
3. **Leap year handling:** Must account for Feb 29 in date calculations
4. **Documentation is key:** Comprehensive README helps users understand and use the project
5. **MIT License:** Best balance of permissiveness and attribution

---

## Resources Used

### Documentation
- [Hobonichi Techo Official Guide](https://www.jetpens.com/blog/Guide-to-the-Hobonichi-Techo-Planner/pt/900)
- [Notesnook Help - Markdown Notes](https://help.notesnook.com/rich-text-editor/markdown-notes-editing)
- [Notesnook Importing Guide](https://help.notesnook.com/importing-notes/)

### Tools
- Python 3.x
- Git
- GitHub
- Claude Code (for development assistance)

---

## Timeline

**Total development time:** ~1 hour

1. Research and planning: 15 minutes
2. Initial script development: 15 minutes
3. Adjustments and testing: 10 minutes
4. Documentation (README, LICENSE): 10 minutes
5. Git setup and GitHub push: 5 minutes
6. This development log: 5 minutes

---

## Repository Information

- **GitHub URL:** https://github.com/jaal/hobonichi-digital-journal
- **License:** MIT License
- **Language:** Python 3
- **Platform:** Cross-platform (macOS, Linux, Windows)
- **Target App:** Notesnook (but works with any markdown app)

---

## Acknowledgments

- Inspired by Hobonichi Techo by Hobonichi Co., Ltd.
- Created for the Notesnook community
- Built with Claude Code

---

**Last Updated:** 2026-01-05
