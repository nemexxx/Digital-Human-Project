# Data directory

Your personal export data goes here. **Nothing in this folder (except this
README) is committed to git** — see the project `.gitignore`.

The analysis scripts expect the following structure. File and folder names come
from the official Instagram / YouTube data exports (German export names are used
for the browser/YouTube history files):

```
data/
├── Instagram/
│   ├── your_instagram_activity/
│   │   ├── likes/liked_posts.json
│   │   └── threads/liked_threads.json
│   └── ads_information/
│       └── instagram_ads_and_businesses/
│           └── advertisers_using_your_activity_or_information.json
├── Chrome/
│   └── verlauf.json                      # Chrome history export
└── YouTube/
    └── Verlauf/
        ├── Suchverlauf.json              # search history
        └── Wiedergabeverlauf.json        # watch history
```

## Where to get the data

- **Instagram / Threads** — Instagram → *Settings → Your activity → Download
  your information* (request JSON format).
- **Chrome history** — export via Google Takeout, or your preferred history
  export tool, as `verlauf.json`.
- **YouTube** — Google Takeout → *YouTube and YouTube Music → history*
  (JSON), which produces `Suchverlauf.json` and `Wiedergabeverlauf.json`.

If you keep your data somewhere else, set the `DHP_DATA_DIR` environment
variable to point at that directory instead.
