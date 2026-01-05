#!/usr/bin/env python3
"""
Generate a single markdown file for a 5-Year Hobonichi-style journal.
This creates a digital version suitable for Notesnook.
"""

from datetime import datetime, timedelta

def generate_hobonichi_markdown(start_year=2026, output_file="Hobonichi_5Year_2026-2030.md"):
    """
    Generate a complete 5-year journal in one markdown file.

    Args:
        start_year: The first year of the 5-year period
        output_file: Name of the output markdown file
    """
    years = [start_year + i for i in range(5)]

    with open(output_file, 'w', encoding='utf-8') as f:
        # Write header
        f.write(f"# 5-Year Journal ({years[0]}-{years[4]})\n\n")
        f.write(f"*Digital Hobonichi 5-Year Techo for Notesnook*\n\n")
        f.write("---\n\n")

        # Write yearly overview section
        f.write("## Yearly Overview\n\n")
        for year in years:
            f.write(f"### {year}\n\n")
            f.write("Key moments and reflections:\n\n")
            f.write("---\n\n")

        # Write each day of the year (366 days to include leap day)
        months = [
            ("January", 31), ("February", 29), ("March", 31), ("April", 30),
            ("May", 31), ("June", 30), ("July", 31), ("August", 31),
            ("September", 30), ("October", 31), ("November", 30), ("December", 31)
        ]

        for month_name, days in months:
            f.write(f"## {month_name}\n\n")

            for day in range(1, days + 1):
                # Create a date object to get day of week (using a leap year for reference)
                date_obj = datetime(2024, list(range(1, 13))[months.index((month_name, days))], day)
                day_of_week = date_obj.strftime("%A")

                # Write day header
                f.write(f"### {month_name} {day}\n\n")

                # Write 5 year entries
                for i, year in enumerate(years, 1):
                    # Calculate day of week for each specific year
                    try:
                        specific_date = datetime(year, date_obj.month, date_obj.day)
                        specific_dow = specific_date.strftime("%A")
                    except ValueError:
                        # Handle Feb 29 in non-leap years
                        specific_dow = "N/A"

                    f.write(f"**{year}** ({specific_dow})\n\n")
                    f.write("&nbsp;\n\n")  # Empty line for writing
                    f.write("\n")

                # Write memo section
                f.write("**Memo**\n\n")
                f.write("&nbsp;\n\n")  # Empty line for memo writing
                f.write("\n")
                f.write("---\n\n")

        # Write back pages
        f.write("## Additional Pages\n\n")

        # My Lists
        f.write("### My Lists\n\n")
        for i in range(1, 6):
            f.write(f"#### List {i}\n\n")
            f.write("- \n\n")
        f.write("---\n\n")

        # My Favorite Things
        f.write("### My Favorite Things\n\n")
        favorite_categories = [
            "Books", "Movies", "Music", "Restaurants", "Places",
            "Quotes", "People", "Memories", "Goals Achieved"
        ]
        for category in favorite_categories:
            f.write(f"#### {category}\n\n")
            f.write("\n\n")
        f.write("---\n\n")

        # Gifts tracker
        f.write("### Gifts\n\n")
        for year in years:
            f.write(f"#### {year}\n\n")
            f.write("| Date | Given To/Received From | Gift | Occasion |\n")
            f.write("|------|------------------------|------|----------|\n")
            f.write("| | | | |\n\n")
        f.write("---\n\n")

        # Personal Notes
        f.write("### Personal Notes\n\n")
        personal_sections = [
            "About Me", "Important Contacts", "Health Information",
            "Goals", "Wishes", "Books to Read", "Places to Visit"
        ]
        for section in personal_sections:
            f.write(f"#### {section}\n\n")
            f.write("\n\n")

    print(f"✓ Generated {output_file}")
    print(f"  File size: {len(open(output_file, 'r').read())} characters")
    print(f"  Ready to import into Notesnook!")

if __name__ == "__main__":
    # You can customize the start year here
    generate_hobonichi_markdown(start_year=2026)
