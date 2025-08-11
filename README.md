# Log Analyzer & Report Generator

A professional **Python + PyQt6** desktop application for analyzing web server logs (Apache/Nginx combined format).
It parses log files, calculates useful metrics, and presents them in an interactive desktop interface with charts and export options.

## ✨ Features
- **User-friendly desktop interface** (PyQt6)
- Parse Apache/Nginx combined log format
- View and analyze:
  - Top status codes
  - Top endpoints (paths)
  - Top IP addresses
  - Error rates
  - Requests per minute/hour
- Interactive tables and charts
- Export reports to HTML and CSV
- *(Planned)* PDF export

## 🛠 Tech Stack
- Python 3.11+
- PyQt6 – GUI framework
- Jinja2 – HTML report templates
- Matplotlib – charts and graphs
- `collections.Counter` – fast statistics
- pytest – testing
