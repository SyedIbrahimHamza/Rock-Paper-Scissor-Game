# Rock Paper Scissors

A terminal-based Rock Paper Scissors game against the computer, with score tracking across rounds.

## What it does

- Lets you enter your choice (Rock, Paper, or Scissors)
- Validates your input and asks again if it's invalid
- Picks a random choice for the computer
- Decides the winner using standard Rock Paper Scissors rules
- Keeps a running score for both you and the computer across multiple rounds
- Lets you keep playing round after round until you choose to stop, then shows the final score

## How to run it

```bash
python rock_paper_scissors.py
```

Type your choice when prompted, see the result, and choose whether to play another round.

## What I learned building this

- Using `random.choice()` to make the computer pick randomly from a list
- Validating user input with `continue` to re-ask instead of crashing or breaking the loop
- Combining multiple conditions with `or` and `and` to check all the winning combinations
- Keeping and updating a running score across loop iterations using variables
- Using `.title()` to normalize user input so "rock", "Rock", and "ROCK" are all treated the same