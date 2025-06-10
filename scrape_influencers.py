from urllib.request import urlopen
from html.parser import HTMLParser
from typing import List, Dict


def fetch_page(url: str) -> str:
    """Fetch HTML content of a public influencer ranking page."""
    with urlopen(url) as resp:
        return resp.read().decode("utf-8")


class TableParser(HTMLParser):
    """Simple HTML table parser for influencer data."""

    def __init__(self) -> None:
        super().__init__()
        self.in_td = False
        self.current_row: List[str] = []
        self.rows: List[List[str]] = []

    def handle_starttag(self, tag, attrs):
        if tag == "td":
            self.in_td = True

    def handle_endtag(self, tag):
        if tag == "td":
            self.in_td = False
        elif tag == "tr" and self.current_row:
            self.rows.append(self.current_row)
            self.current_row = []

    def handle_data(self, data):
        if self.in_td:
            self.current_row.append(data.strip())


def parse_influencer_table(html: str) -> List[Dict[str, str]]:
    """Parse HTML table of influencers into a list of dictionaries."""
    parser = TableParser()
    parser.feed(html)
    rows: List[Dict[str, str]] = []
    for cols in parser.rows:
        if len(cols) >= 4:
            name, followers, niche, location = cols[:4]
            rows.append({
                "name": name,
                "followers": followers,
                "niche": niche,
                "location": location,
            })
    return rows


if __name__ == "__main__":
    # Example usage: replace the URL with an actual public page that allows scraping.
    ranking_url = "https://example.com/tiktok-ranking"
    html = fetch_page(ranking_url)
    influencers = parse_influencer_table(html)
    for inf in influencers:
        print(inf)
