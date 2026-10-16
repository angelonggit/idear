"""把 ideas/voice-legacy-journal.md 里的每日灵感同步进 site/voice-legacy.html 的 journal-data。

用法（在仓库根目录）：python3 site/sync_journal.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MD = ROOT / "ideas" / "voice-legacy-journal.md"
HTML = ROOT / "site" / "voice-legacy.html"


def parse(md):
    entries = []
    for blk in re.split(r"\n(?=## \d{4}-\d{2}-\d{2} · )", md)[1:]:
        head = re.match(r"## (\S+) · (.+)", blk)
        body, _, tail = blk.partition("### 今天的一个想法")
        idea, _, more = tail.partition("### 可以继续挖")
        finds = []
        for name, rest in re.findall(r"^- \*\*(.+?)\*\*[：:](.+)$", body, re.M):
            urls = re.findall(r"\]\((https?://[^)]+)\)", rest)
            text = re.sub(r"\s*(·\s*)?\[[^\]]+\]\([^)]+\)", "", rest).strip().rstrip("·").strip()
            finds.append({"name": name, "text": text, "url": urls[0] if urls else ""})
        entries.append({
            "date": head.group(1),
            "theme": head.group(2).strip(),
            "finds": finds,
            "idea": idea.strip().replace("**", ""),
            "more": [l[2:].strip() for l in more.strip().splitlines() if l.startswith("- ")],
        })
    return entries


def main():
    entries = parse(MD.read_text(encoding="utf-8"))
    data = json.dumps(entries, ensure_ascii=False).replace("</", "<\\/")
    html = HTML.read_text(encoding="utf-8")
    html, n = re.subn(
        r'(<script type="application/json" id="journal-data">).*?(</script>)',
        lambda m: m.group(1) + data + m.group(2),
        html,
        flags=re.S,
    )
    if n != 1:
        raise SystemExit("journal-data block not found")
    HTML.write_text(html, encoding="utf-8")
    print(f"synced {len(entries)} entries")


if __name__ == "__main__":
    main()
