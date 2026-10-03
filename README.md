# passcheck

A command-line password strength analyzer written in Python.

> 🚧 Work in progress — currently building **v1**.

## Features

- [ ] **v1** — Score passwords on length and character variety, with improvement tips
- [ ] **v2** — Flag passwords found in common-password wordlists
- [ ] **v3** — Check for breached passwords via the Have I Been Pwned API (k-anonymity, password never leaves your machine)
- [ ] **v4** — Command-line flags with `argparse`

## Installation

```bash
git clone https://github.com/<your-username>/passcheck.git
cd passcheck
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

## Usage

```bash
python -m passcheck.main
```

Example output:

```
Enter a password: hunter2
Score: 2/6
Rating: Weak
Tips:
  - Use at least 8 characters
  - Use at least 12 characters
  - Add an uppercase letter
  - Add a symbol
```

## Running tests

```bash
pytest
```

## How scoring works

| Rule                      | Points |
|---------------------------|--------|
| At least 8 characters     | +1     |
| At least 12 characters    | +1     |
| Contains lowercase letter | +1     |
| Contains uppercase letter | +1     |
| Contains digit            | +1     |
| Contains symbol           | +1     |

**0–2** Weak · **3–4** Medium · **5–6** Strong
