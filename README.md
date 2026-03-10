# 🎮 Game Glitch Investigator

This project is a Streamlit number guessing game that started with several AI-generated bugs. My goal was to find the problems, fix the logic, add tests, and reflect on how I used AI during debugging.

## Demo

The app is a number guessing game with:
- Easy, Normal, and Hard difficulty
- Score tracking
- Guess history
- Hint messages
- Debug info during testing

Run the app:
```bash
python3 -m streamlit run app.py
```

Run the tests:
```bash
python3 -m pytest
```

## What Was Broken

At the beginning, the game had a few problems:
* Hint messages were confusing
* Difficulty behavior was not fully consistent
* Some logic was mixed with the UI, which made testing harder
* Score behavior needed testing and verification

## Fixes I Made

I improved the project by:
* Moving game logic into `logic_utils.py`
* Fixing the guessing logic
* Correcting the hint behavior
* Improving reset and game flow behavior
* Adding pytest tests
* Updating the reflection

## Files

* `app.py` – Streamlit app
* `logic_utils.py` – game logic
* `tests/test_game_logic.py` – tests
* `reflection.md` – reflection answers

## My Experience

This project helped me practice debugging AI-generated code carefully. AI was helpful for finding bugs and suggesting fixes, but I still needed to test the code myself and make sure the changes really worked.

## How to Run

```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
python3 -m streamlit run app.py
```

## Reflection

See `reflection.md` for my notes about the bugs, fixes, testing process, and what I learned from working with AI.
