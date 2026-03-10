# 🎮 Game Glitch Investigator

A Streamlit number guessing game that started with several AI-generated bugs. In this project, I investigated the glitches, fixed the broken game logic, added tests, and reflected on how I used AI as a debugging teammate.

## Demo

This project is a number guessing game built with Streamlit.

Features:
- Difficulty levels: Easy, Normal, Hard
- Score tracking
- Guess history
- Hint feedback for high and low guesses
- Debug panel for testing during development

To run the app locally:

```bash
python3 -m streamlit run app.py
```

To run the tests:

```bash
python3 -m pytest
```

## What Was Broken

When I started, the game had several issues:
* Hint messages were confusing or incorrect
* Difficulty ranges did not always match expected behavior
* Some logic was hard to test because game logic and UI were mixed together
* The score and guess handling needed verification through testing

## Fixes I Made

I repaired the game by:
* Moving reusable game logic into `logic_utils.py`
* Fixing the guessing logic
* Correcting the hint behavior
* Improving reset and game flow behavior
* Adding automated pytest tests
* Rewriting the reflection with clear explanations of what I fixed and how I verified it

## Files in This Project

* `app.py` – Streamlit UI and game state
* `logic_utils.py` – helper functions for game logic
* `tests/test_game_logic.py` – pytest test cases
* `reflection.md` – reflection on debugging and AI collaboration

## Document Your Experience

This project helped me practice debugging AI-generated code instead of blindly trusting it. AI was useful for speeding up code review and suggesting refactors, but I still had to verify each change carefully by running the app and checking test results.

One helpful suggestion was separating the game logic from the Streamlit UI so the functions could be tested more easily. A less helpful part was that some suggested fixes did not fully match the app behavior, so I had to review and adjust them myself.

Overall, this project showed me that AI can be a strong teammate, but human judgment is still necessary to confirm whether the fix is actually correct.

## How to Run

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies
4. Run the Streamlit app

```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
python3 -m streamlit run app.py
```

## Test the Project

```bash
python3 -m pytest
```

## Reflection

See `reflection.md` for:
* What bugs I found
* How I used AI as a teammate
* How I tested my fixes
* What I learned about Streamlit session state
* What habits I want to keep using in future projects
