# Python AI Engineer Journey 🚀

I am Karthik ([@nagakarthikravula](https://github.com/nagakarthikravula)), a final year BTech Data Science student from Raghu Engineering College.
My goal is to become an AI/GenAI Engineer and land a fresher job by October-November 2026.

This repository documents my learning journey — real projects built from scratch, one week at a time.

---


## Month 1 — Python Foundations (June 2026)

**Goal:** Strengthen Python to the point where I can build real programs — not college assignments.

**What I learned:**
- Functions — parameters, return values, default arguments, `*args`, `**kwargs`
- Loops — `for`, `while`, `break`, `enumerate`
- List and dictionary comprehensions
- Object-Oriented Programming — classes, objects, `__init__`, `self`, inheritance, `super()`, method overriding
- File handling — reading and writing `.txt` and `.json` files
- Error handling — `try/except`, `FileNotFoundError`, `ValueError`, `json.JSONDecodeError`
- External libraries — `requests`, `python-dotenv`
- JSON parsing — extracting data from API responses
- Environment variables — storing secrets safely with `.env`

---

## Projects Built

### Week 1 — Contact Book CLI App
**Concepts:** Functions, loops, nested dictionaries, list comprehensions

A command-line contact management app that runs in the terminal.

**Features:**
- Add a contact with name, phone number, and email
- View all saved contacts
- Search for a contact by name
- Delete a contact
- Runs in a continuous menu loop until user exits

**How to run:**
```
python contact_book.py
```

**Key functions:**
- `display_all_contacts()` — shows all saved contacts with separator lines
- `add_contacts()` — takes user input and adds a new contact
- `search_contacts()` — searches for a contact by name using the `in` keyword
- `delete_contact()` — removes a contact with confirmation

---

### Week 2 — Bank Account OOP App
**Concepts:** Classes, objects, constructors, instance methods, encapsulation

A fully object-oriented bank account manager with validation and transaction history.

**Features:**
- Create a bank account with a holder name
- Deposit money with input validation
- Withdraw money with overdraft protection
- Check current balance
- View full transaction history
- Runs in a continuous menu loop

**How to run:**
```
python bank_account.py
```

**Class:** `BankAccount`
- `__init__(name)` — creates account with zero balance and empty transaction list
- `deposit(amount)` — validates and adds money
- `withdraw(amount)` — validates, checks overdraft, deducts money
- `check_balance()` — displays current balance
- `show_history()` — displays numbered transaction history

---

### Week 3 — Notes Saver App
**Concepts:** File handling, JSON, error handling, data persistence

A notes app that saves your notes permanently to a JSON file — notes survive even after the program closes.

**Features:**
- Add a note (saved immediately to `notes.json`)
- View all saved notes with numbering
- Delete a note by number
- Handles missing file gracefully on first run
- Validates empty input and out-of-range deletions

**How to run:**
```
python notes_saver.py
```

**Key functions:**
- `load_notes()` — safely loads notes from JSON file, handles `FileNotFoundError` and `json.JSONDecodeError`
- `save_notes(notes)` — writes updated notes list to JSON file
- `add_note(notes)` — takes user input and saves note
- `view_notes(notes)` — displays numbered list of all notes
- `delete_note(notes)` — removes a note by number with full error handling

---

### Week 4 — Weather Fetcher App
**Concepts:** `requests` library, REST APIs, JSON parsing, `python-dotenv`

A weather app that calls a real public API and displays live weather data for any city in the world.

**Features:**
- Enter any city name to get current weather
- Displays condition, temperature, feels-like, humidity, wind speed and direction
- Handles network errors and invalid cities gracefully
- Supports checking multiple cities in one session
- Uses `.env` for environment variable management (API key ready)

**API used:** [wttr.in](https://wttr.in) — free, no API key required

**How to run:**
```
python weather_fetcher.py
```

**Key functions:**
- `get_weather(city)` — calls wttr.in API, returns JSON data or `None` on failure
- `display_weather(data, city)` — extracts and prints formatted weather report

**Sample output:**
```
========================================
  Weather Report: Vizag
========================================
  Condition   : Sunny
  Temperature : 32°C (Feels like 38°C)
  Humidity    : 65%
  Wind Speed  : 17 km/h (SW)
========================================
```

---

## Setup

**Requirements:**
```
pip install requests python-dotenv
```

**Environment:**
- Python 3.13.1
- VS Code
- Virtual environment (`venv`)

**Clone and run:**
```
git clone https://github.com/nagakarthikravula/python-ai-journey.git
cd python-ai-journey
python -m venv venv
venv\Scripts\activate
pip install requests python-dotenv
```

---

*Started: June 9, 2026 | Target job: October-November 2026*
