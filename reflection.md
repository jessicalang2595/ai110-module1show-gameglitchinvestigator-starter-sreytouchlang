# 💭 Reflection: Game Glitch Investigator

## 1. What was broken when you started?

When I first opened the game, it looked fine, but the guessing part did not work correctly. The hint messages were backwards, so the app told the player the wrong direction. I also saw that the range display stayed at 1 to 100 even when the difficulty changed, which made the game confusing.

## 2. How did you use AI as a teammate?

I used Claude to help me look through the code and find the bugs faster. One helpful suggestion was moving the repeated logic into logic_utils.py because it made the code cleaner and easier to test. I did not just trust the AI output, though. I checked the code myself and tested each fix to make sure it really worked.

## 3. Debugging and testing your fixes

I tested the game by running the app and trying guesses that were too high, too low, and correct. I also used the debug panel to compare my guesses with the secret number. After that, I ran pytest to make sure the logic functions were working correctly.

## 4. What did you learn about Streamlit and state?

I learned that Streamlit reruns the whole script every time the user interacts with the app. Because of that, session state is very important. It helps the game remember values like the secret number, score, and attempts instead of resetting everything each time.

## 5. Looking ahead: your developer habits

This project reminded me to separate game logic from UI because it makes debugging easier. I also learned that AI can help speed things up, but I still need to review and test everything carefully before trusting it.
