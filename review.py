"""
Scans all solution files and returns problems solved more than 3 days ago.
"""
import re
from pathlib import Path
from datetime import datetime, timedelta, timezone


PROBLEMS_DIR = Path(__file__).parent / "problems"
DATE_PATTERN = re.compile(r"Date Solved:\s*(\d{4}-\d{2}-\d{2})")
THRESHOLD_DAYS = 3


def extract_metadata(filepath: Path) -> dict:
    """Read only the first line of the file to extract the date."""
    try:
        with filepath.open() as f:
            first_line = f.readline()
            second_line = f.readline()
        date_match = DATE_PATTERN.search(first_line)
        difficulty_match = re.search(r"Difficulty:\s*(\w+)", second_line)

        if date_match and difficulty_match:
            return {
                "date": datetime.strptime(date_match.group(1), "%Y-%m-%d").replace(
                tzinfo=timezone.utc),
                "difficulty": difficulty_match.group(1).title() if difficulty_match else None,
            }
    except (OSError, ValueError):
        pass
    return None


def get_problems_older_than(days: int = THRESHOLD_DAYS) -> list[dict]:
    """
    Scan all .py files under /problems and return those whose
    Date Solved is more than `days` days ago.
    """
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    old_problems = []

    for filepath in sorted(PROBLEMS_DIR.rglob("*.py")):
        problem_info = extract_metadata(filepath)
        if problem_info and problem_info["date"] < cutoff:
            # Build a readable title from the filename
            title = filepath.stem.replace("_", " ").title()
            old_problems.append({
                "title": title,
                "date_solved": problem_info["date"].strftime("%Y-%m-%d"),
                "days_ago": (datetime.now(timezone.utc) - problem_info["date"]).days,
                "path": str(filepath.relative_to(PROBLEMS_DIR.parent)),
                "platform": filepath.parts[-3].title(),   # e.g. "Leetcode"
                "difficulty": problem_info["difficulty"] # e.g. "Medium"
            })

    return old_problems


if __name__ == "__main__":
    results = get_problems_older_than(THRESHOLD_DAYS)

    if not results:
        print(f"No problems solved more than {THRESHOLD_DAYS} days ago.")
    else:
        print(f"\n{len(results)} problem(s) solved more than {THRESHOLD_DAYS} days ago:\n")
        for p in results:
            print(f"  [{p['title']} {p['platform']} - {p['difficulty']}]")
            print(f"    Solved: {p['date_solved']} ({p['days_ago']} days ago)")
            print(f"    Path:   {p['path']}\n")

    # Plain list of titles if you just want the array
    titles = [p["title"] for p in results]
    if titles:
        print("Title array:", titles)