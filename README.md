# WebScraper

A small Python web crawler that starts from a few web pages, follows their links, and saves the pages that talk about a chosen topic. As shipped, it collects pages about video game consoles, starting from Wikipedia.

## What it does

- Starts from two Wikipedia pages (Nintendo 64 and Home video game console).
- Downloads each page and checks whether it mentions at least two of the topic words: xbox, playstation, nintendo, atari, odyssey, steam, handheld, console, gameboy, japan.
- Saves matching pages as HTML files, and follows the links found on them.
- Stops after 500 pages have been saved, or when there are no more links to visit.
- Writes two logs when it finishes: `visited.txt` (every URL tried) and `saved.txt` (every URL that matched).

The topic, start pages and word list are described in `FINAL.txt`, and are set in the `run()` function of `FINAL.py`.

## Tech stack

- Python 3
- [BeautifulSoup 4](https://pypi.org/project/beautifulsoup4/) for parsing HTML
- Python standard library (`urllib`) for downloading pages

## How to run

1. Install Python 3.
2. Install the one dependency: `pip install beautifulsoup4`
3. Run the crawler from an empty folder, because it writes its output files into the current directory:

   ```
   mkdir output && cd output
   python ../FINAL.py
   ```

4. Watch the progress in the terminal. Saved pages appear as `<number> <page title>.html` next to `visited.txt` and `saved.txt`.

Stop it at any time with Ctrl+C. Note that the log files are only written when the crawl finishes normally.

Please be polite to the sites you crawl. The script does not pause between requests, so consider adding a delay before pointing it at smaller websites.

## Status

Working prototype. It was written as a student style project in 2018 and has no tests, no robots.txt handling and no request delay. There is no live demo, since it is a command line tool that downloads many pages.

## Credits

Written by Max Awad. It uses BeautifulSoup, by Leonard Richardson, and starts from pages on Wikipedia.
