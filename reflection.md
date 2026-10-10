# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?



- What did the game look like the first time you ran it?
What was broken was the attempt number was off by 1, the difficulty of normal and hard were swapped(normal should be 1 - 50 and hard should be 1 - 100), the new game button would also not start a new game.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  Difficulty of normal and hard should be swapped normal should be 1-50 and hard 1-100.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| attempts | attempts should be 8| attempts was 7 | attempts left 1 |
|Difficulty: normal 1-100 | normal 1-50 | normal 1-100 | guess was 70, above 50 |
| Go higher/lower |  go higher means guess is higher and lower means guess is lower| guess is lower but says go higher, guess is higher but says go lower | answer is 15, guess is 20, console says go higher|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- The suggestion of fixing when it says go higher when the answer is lower, and go lower when the answer is higher.

- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? 
- By refreshing the page many times and playing all the difficulty to make sure it was fixed and checked if the secret dev info was correct each time.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- reruns are like setting a new save point after fixing up bugs and go back to the begining to make sure it worked

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  I would say being able to use git and fork code and edit it myself for my own purpose.
- What is one thing you would do differently next time you work with AI on a coding task? 
- Rely on it a little less but use it to futher my understanding.

- In one or two sentences, describe how this project changed the way you think about AI generated code. 
- My thoughts on AI-generated code are that it is very cool to see it actually work, and it can be used to help not only just do it for you. Meaning you can work along side it to make your code exactly as you see in you mind.
