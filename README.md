# Prima Coffee Brew Data Scraper

A simple Python scraper that reverse engineers the API of [prima-coffee.com](https://prima-coffee.com/) to fetch **all coffee brew data** for research, analysis, or personal dataset building.

## Features

* Reverse engineers the site's API for structured coffee brew data
* Saves results as JSON for easy analysis
* Lightweight, no unnecessary dependencies
## Requirements

* Python 3.9+
* `requirements.txt` is provided to install dependencies.

## Setup

1️⃣ **Clone the repository:**<br>
2️⃣ **(Optional) Create and activate a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3️⃣ **Install dependencies:**

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

The script will fetch and save the coffee brew data to `sorted-products.json` and `5-cheapest-products.json` (configurable inside the script).

## Notes

* This project is for **educational and personal use** only.
* Always respect the target site's `robots.txt` and terms of service.

## License

MIT License.
