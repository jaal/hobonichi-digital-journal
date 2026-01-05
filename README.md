# Hobonichi 5-Year Digital Journal for Notesnook

A digital version of the beloved Hobonichi 5-Year Techo, formatted as a single markdown file optimized for [Notesnook](https://notesnook.com/).

## What is this?

The Hobonichi 5-Year Techo is a popular Japanese journaling system where each page shows the same date across five consecutive years, allowing you to see how your life evolves over time. This project creates a digital version that you can use in Notesnook or any markdown-compatible note-taking app.

## Features

- **366 Daily Entries** - One for each day of the year (including leap day)
- **5-Year Format** - Each day has space for 5 consecutive years
- **Day of Week** - Automatically calculates the correct day of week for each year
- **Additional Sections**:
  - Yearly Overview pages
  - My Lists (5 customizable lists)
  - My Favorite Things (Books, Movies, Music, Places, Quotes, etc.)
  - Gift Tracker (with tables by year)
  - Personal Notes (Goals, Wishes, Books to Read, Places to Visit, etc.)
- **Proper Spacing** - Empty lines under each date for comfortable writing
- **Single File** - Entire 5-year journal in one markdown file (~69KB)

## Quick Start

### Option 1: Use Pre-generated File

1. Download `Hobonichi_5Year_2026-2030.md` from this repository
2. Import into Notesnook:
   - Open Notesnook
   - Go to **Settings** → **Notesnook Importer** → **Import from Markdown files**
   - Select the downloaded file
3. Start journaling!

### Option 2: Generate Custom Years

If you want different years:

1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/hobonichi-digital-journal.git
   cd hobonichi-digital-journal
   ```

2. Run the generator script:
   ```bash
   python3 generate_hobonichi_5year.py
   ```

3. Customize the start year by editing line 114 in `generate_hobonichi_5year.py`:
   ```python
   generate_hobonichi_markdown(start_year=2026)  # Change to your preferred year
   ```

## Requirements

- Python 3.6 or higher (only if generating custom files)
- [Notesnook](https://notesnook.com/) or any markdown-compatible note app

## How to Use

### Daily Journaling

Each day has this format:

```markdown
### January 1

**2026** (Thursday)

[Your entry here]

**2027** (Friday)

[Your entry here]

... and so on for all 5 years

**Memo**

[Additional notes for this date across all years]
```

### Tips

1. **Use Notesnook's Search** - Quickly find specific dates or entries
2. **Add Tags** - Tag your entries with themes or moods
3. **Lock the Note** - Keep your journal private with Notesnook's encryption
4. **Backup Regularly** - Notesnook syncs automatically if you have Pro
5. **Table of Contents** - Use Notesnook's outline feature to navigate by month

## Structure

```
Hobonichi 5-Year Journal
├── Yearly Overview (5 sections for annual reflections)
├── January through December (366 daily entries)
└── Additional Pages
    ├── My Lists
    ├── My Favorite Things
    ├── Gifts
    └── Personal Notes
```

## Why Notesnook?

- **Privacy-focused** - End-to-end encrypted
- **Cross-platform** - Available on desktop, mobile, and web
- **Markdown support** - Perfect for this journal format
- **Search** - Find any entry instantly
- **Free** - Core features available for free

## Contributing

Contributions are welcome! Feel free to:
- Report bugs or issues
- Suggest new features
- Submit pull requests
- Share how you're using it

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Inspired by the [Hobonichi Techo](https://www.1101.com/store/techo/en/) by Hobonichi Co., Ltd.
- Created for the [Notesnook](https://notesnook.com/) community
- Japanese 5-year journal tradition

## Related Links

- [Hobonichi Official Website](https://www.1101.com/store/techo/en/)
- [Notesnook Official Website](https://notesnook.com/)
- [Notesnook Documentation](https://help.notesnook.com/)

---

**Happy Journaling!** 📔✨

If you find this useful, please star the repository and share it with others who might enjoy digital journaling.
