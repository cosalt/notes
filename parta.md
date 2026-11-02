## What Hinger is

Hinger is a two-player game on a 5×5 board where players take turns removing counters.

- **Board:** each cell holds some number of counters. 0 means empty; 1 or more means **active**. The `grid` is just those numbers stored as a 5×5 list.
- **Neighbours:** the up-to-8 cells around a cell, diagonals included (like a king in chess).
- **Region:** a group of active cells joined through neighbours. Think of islands on a map.
- **Hinger:** a cell with exactly one counter that acts as a bridge. Taking that counter away splits a region, so the number of regions goes up.

## How to play

On your turn you take **one counter** from any active cell. Each move is named by that cell's letter:

```
A B C D E
F G H I J
K L M N O
P Q R S T
U V W X Y
```

- **Z** isn't a cell. It means "I declare the game over", and whoever plays it **loses immediately**.
- **Scoring:** both players start on 100. A move costs you the number of active neighbours that cell has. You get **+100 if the cell is a hinger** at the moment you take it.
- **End:** when the last counter is gone, the higher score wins. Equal scores are a draw.
- **Illegal moves:** in your game code, taking from an empty cell or using a letter that isn't a cell ends the game, and the opponent wins.

The +100 bonus is far bigger than any cost (at most 8). So the game is really about grabbing hingers and not leaving them for your opponent.

**Worked example (Figure 1.1):**

```
   s1                s2                s3
1 1 0 0 1         1 1 0 0 1         1 1 0 0 1
1 1 0 0 0         1 1 0 0 0         1 1 0 0 0
0 0 1 1 1  ─ Y ►  0 0 1 1 1  ─ M ►  0 0 0 1 1
0 0 0 1 1         0 0 0 1 1         0 0 0 1 1
0 0 0 0 1         0 0 0 0 0         0 0 0 0 0
```

- **s1** has 11 active cells in 2 regions: the lone top-right cell, and everything else. The top-left block touches the centre cell diagonally, so they count as joined.
- **Alice plays Y** (bottom-right). It has 2 active neighbours and isn't a hinger, so her score is 100 − 2 = **98**.
- **Bob plays M** (centre). It has 3 active neighbours, but it's the only link between the top-left block and the right-hand group. Removing it leaves 3 regions, so it's a hinger and his score is 100 − 3 + 100 = **197**.

## How to code it

### `a1_state.py`: the board (Task 1)
1. **Letter ↔ cell helpers.** Turn a letter into a number with `ord(letter) − ord('A')`, then `row, col = divmod(number, 5)`. Only A–Y are cells. You'll use these everywhere.
2. **`__init__(grid)`.** Store a copy of each row, not the list you were given. Otherwise the states made in `successors()` share rows, and changing one changes them all.
3. **`__str__`.** Numbers separated by spaces, one row per line, no borders.
4. **`neighbours(r, c)`.** Returns the up-to-8 surrounding cells that are on the board. Cost, regions and hingers all use it.
5. **`numRegions()`.** Go through the cells. Each time you reach an active cell you haven't visited yet, count a new region. Then visit everything connected to it, using `neighbours` with a queue or recursion (BFS or DFS).
6. **`numHingers()`.** For each cell with exactly 1 counter:
   - count the regions
   - set the cell to 0 and count again
   - put the counter back

   If the count went up, it's a hinger. A single counter on its own makes the count go *down*, so it isn't a hinger.
7. **`move(letter)`.** If the letter is A–Y and that cell is active, take one counter and return True. Otherwise change nothing and return False. Leave Z to the game loop.
8. **Extra helpers (1.7):** `move_cost(letter)` (counts active neighbours), `is_hinger(r, c)`, `legal_moves()`, `is_empty()` and `copy()`. The game and the AI need the cost and hinger checks **before** a move is made.
9. **`successors()`.** A generator: for each active cell, copy the state, make that move on the copy, and `yield` it. Also pass back the letter, either as `(letter, state)` pairs or saved on the new state, because the AI needs to know which move produced each state.
10. **`tester()`.** Run it from an `if __name__ == "__main__":` block.
    - Create `sa` as s1 and print it.
    - Check the answers you already know from the figure:
      - `sa.numRegions()` is 2, and s1 has 11 successors
      - Y costs 2 with no bonus; after Y, M costs 3 and is a hinger
      - after "YM" there are 3 regions
      - illegal moves (C, Z, a lowercase letter, "?") return False and leave the board unchanged
    - **Watch out:** `numHingers()` should be **2** for s1 and s2, not 1. The figure only bolds the centre cell, but G (row 1, col 1) is a hinger too: remove it and the top-left three cells are cut off. s3 has 0 hingers.

### `a2_agent.py`: the AI player (Task 2)
1. **Set-up.** `__init__(name="A01")` uses your group name as the default, and `self.modes = ["minimax", "alphabeta"]`. `__str__` shows the name and the modes.
2. **Decide what the AI maximises.** The state doesn't store scores, so the AI works with the **score difference**.
   - Each move is worth `bonus − cost`.
   - Add it when it's the AI's move; subtract it when it's the opponent's.
   - Both players start on 100, so the starting scores cancel out. The final result is the scores so far plus whatever happens from here, so maximising the difference from here is the right goal.
3. **Never consider Z**, because it's an instant loss. Only look at A–Y moves on active cells. If there are none, return None.
4. **Minimax.** A recursive function takes a state, a depth and whose turn it is.
   - On the AI's turn it takes the highest value over all successors; on the opponent's turn, the lowest.
   - It stops at depth 0 or when the board is empty.
   - The top level returns the move with the best value.
5. **Depth limit.** You can't search the whole game: s1 alone has 11! ≈ 40 million possible move orders. So look 3–5 moves ahead. At the cut-off, use the score difference so far, plus an extra estimate if you want one (for example, how many hingers are available).
6. **Alpha-beta.** The same search, but it keeps track of the best outcome each side is already guaranteed. It skips branches that can't change the decision. It finds a move just as good as minimax does while checking far fewer positions. Trying hinger moves first lets it skip even more.
7. **Measure both.** Count the positions checked and the time per move for minimax and alpha-beta. Part 1 is about comparing efficiency, so these are your numbers.
8. **Optional speed-up.** The same boards come up again and again (s1 has only 2,048 possible smaller boards), so save results keyed by (board, whose turn) and reuse them.
9. **`next_move(state, mode="alphabeta")`.** Calls the chosen strategy. The default should be your best one.
10. **`tester()`:**
    - on s2, an AI looking 1 move ahead should pick M (worth 97) over G (96)
    - minimax and alpha-beta should find equally good moves
    - alpha-beta should check fewer positions
    - an empty board should give None
11. **[*] MCTS (optional).** An extra mode that plays lots of random games from the current board and favours the moves that win most often.

### `a3_game.py`: the game loop (Task 3)
1. **`play(state, agentA, agentB)`.** Both scores start at 100, A moves first, and the loop runs while counters remain.
2. **Get the move.** For an AI, call `agent.next_move(state)`. If the agent is None, it's a human: use `input()` and convert to uppercase.
3. **Z:** that player loses. Announce it and return the opponent as the winner.
4. **Illegal move** (not A–Y, or an empty cell): the game ends and the opponent wins. Check this before changing the board.
5. **Score, then move.**
   - Work out the cost and hinger bonus first, because hinger status changes once the counter is gone.
   - Update the player's score and make the move.
   - Print the board and scores, then switch player.
6. **Board empty:** the higher score wins, so return (name, score). If the scores are equal, announce a draw and return None.
7. **`tester()`:**
   - AI vs AI starting from s1
   - a fake "human" (a tiny class with a fixed list of moves) to test an illegal move, Z and a draw without having to type anything
8. **[*] Extras:** a move counter, a turn timer, saving the move string (like "YM") to a file, or a graphical interface.

