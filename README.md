# Data Scrape & Auto‑Swipe for Tinder  
Author · Md Samshad Rahman (`@samshad`)

> **⚠️ Educational use only!**  
> This repo shows how to authenticate against Tinder’s undocumented API, collect profile metadata for research, and automate “like / dislike” decisions from the command line.  
> **Using automation on Tinder is against their Terms of Service.** Run these scripts at your own risk.

---

## 📦  What’s inside

| File | Purpose |
|------|---------|
| `auth.py` | Handles Tinder login via phone number or Facebook token, then caches a **Tinder API X‑Auth‑Token** for subsequent calls. |
| `auto_tinder.py` | CLI tool that<br>  • pulls the recommended user queue<br>  • logs **name · age · distance · bio · photos** to `data/profiles.csv`<br>  • auto‑likes / passes either **randomly** or via a simple rule engine (`--filter "bio~engineer and distance<10"`). |
| `requirements.txt` | Requests, tqdm, pandas and color‑log for pretty printing. |
| `.gitignore` | Keeps token cache, CSV dumps and log files out of version control. |
| `README.md` | You’re reading it. |
| `LICENSE.md` | MIT. |

---

## 🧠  Highlights & learning points

* **Reverse‑engineering APIs** – Captured mobile app traffic to find undocumented endpoints and headers.  
* **Stateless auth** – Tinder uses a Bearer token valid ~24 hours; `auth.py` refreshes it automatically.  
* **Rate‑limit handling** – `auto_tinder.py` sleeps when `HTTP 429` arrives to avoid temporary bans.  
* **CLI data filters** – Tiny DSL powered by Python’s `eval()` (sanitised) lets you experiment with selection criteria.  
* **Ethics & compliance** – Includes clear warnings and respects Tinder profile visibility by never downloading images.

---

## 🔧  Configuration

Environment variables (optional):

| Variable | Default | Description |
|----------|---------|-------------|
| `TINDER_TOKEN` | _none_ | Manually set a token instead of running `auth.py`. |
| `MAX_LIKES_PER_RUN` | `100` | Hard limit to stay below Tinder daily caps. |
| `DATA_DIR` | `./data` | Folder for CSV dumps. |
| `LOG_LEVEL` | `INFO` | `DEBUG`, `INFO`, `WARNING`, `ERROR`. |

Put them in a `.env` file or export in your shell.

---

## ⚖️  Disclaimer

This code is **for research and educational demonstration only**. Automating Tinder interactions may violate their Terms of Service and could result in account suspension or legal action.  
Use responsibly, rate‑limit aggressively, and respect user privacy; no screenshots, no public re‑distribution of scraped data.

---

## 📄 Licence

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.  
Do whatever you want, **but**: the author is **not liable** for bans, heartbreaks or unexpected matches 😉.

© 2025 Md Samshad Rahman

