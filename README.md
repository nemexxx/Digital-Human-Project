# Digital Human Project — Echo

**Echo** turns your personal platform exports into a private, self-hosted
dashboard about your own digital habits. It reads the raw JSON you download from
Instagram, Threads, Chrome, and YouTube, aggregates it locally, and renders a
small static website — your most-liked accounts, most-visited domains, peak
browsing/watching hours, and search & watch trends over time.

Everything runs **100% locally**. No data leaves your machine, and no personal
data is stored in this repository.

## Screens

- **Dashboard** — a summary across all sources.
- **Instagram** — accounts you like most + advertisers targeting you.
- **Threads** — accounts you like most.
- **Chrome** — most-visited domains, most-frequent page titles, peak hour.
- **YouTube** — top searches & channels, peak hours, monthly/yearly trends.

> The charts and tables ship with **placeholder sample data** so the site
> renders out of the box. Running the pipeline replaces them with your own
> results locally.

## Requirements

- Python 3.9+ (standard library only — no `pip install` needed)
- A modern web browser

## Getting started

1. **Clone the repo**
   ```bash
   git clone https://github.com/nemexxx/Digital-Human-Project.git
   cd Digital-Human-Project
   ```

2. **Add your export data.** Download your data from each platform and place the
   JSON files under `data/` following the structure described in
   [`data/README.md`](data/README.md). This folder is git-ignored, so your data
   stays local.

3. **Run the pipeline** from the project root:
   ```bash
   python master.py
   ```
   This runs every analysis, injects the results into the HTML templates in
   `website/`, and opens the dashboard in your browser.

   Prefer a different data location? Point the pipeline at it:
   ```bash
   DHP_DATA_DIR=/path/to/your/exports python master.py
   ```

You can also run any single analysis module on its own to print results to the
terminal, e.g.:

```bash
python -m data_analysis.chrome_history
```

## Project structure

```
.
├── master.py                 # Orchestrates all analyses and updates the website
├── data_analysis/            # One module per data source
│   ├── config.py             # Resolves the data directory (DHP_DATA_DIR)
│   ├── instagram_likes.py
│   ├── threads_likes.py
│   ├── instagram_advertisers.py
│   ├── chrome_history.py
│   └── youtube_history.py
├── website/                  # Static dashboard (HTML/CSS/JS + Chart.js)
├── data/                     # Your local exports (git-ignored)
└── README.md
```

## How it works

Each module in `data_analysis/` reads one export file and returns aggregated
counts. `master.py` formats those into HTML table rows and injects them between
named `<!-- marker -->` / `<!-- End of marker -->` comments in the pages under
`website/`, so re-running the pipeline simply refreshes the numbers.

## Privacy

- Your raw exports live under `data/`, which is excluded from git via
  `.gitignore`.
- The committed HTML/JS contains only neutral placeholder sample data.
- Nothing is uploaded anywhere — the dashboard is a local static site.

## License

Released under the [MIT License](LICENSE).
