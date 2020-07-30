
# pencil-game
A Python Terminal Game based off the pencil game "One Left", which I developed in 8th Grade.

I was first introduced to "One Left" in a seminar in 8th Grade. The instructor offered to play volunteers, and proceeded to win each game. While these games were occuring, I attempted to reverse engineer the game, and to my delight, discovered the winning strategy. Unfortunately, I wasn't called on and never had a chance to win. Instead, in coming home, I coded this Python bot. It's rather complex and messy (as 8th grade me was) but gets the job done!

# Rules

Set parameters:
1. How many pencils there are
2. Minumum pencils you must take each turn
3. Maximum pencils you can take each turn

Alternate turns between players. The person to take the last pencil (the one left) loses.

# The Winning Strategy

By adding the minimum and maximum number of pencils you can take each turn, you are able to create a "cycle" for every two turns.

For example, if the min = m and max = n, every two turns (one player and one bot), you can guarantee that m + n pencils are taken.
| Player Chooses | Bot Chooses | Sum 
|--|--|--|
| m | n | m + n
| m + 1 | n - 1 | m + n
| m + 2 | n - 2 | m + n
| ... | ... | ...
| n - 2 | m + 2 | m + n
| n - 1 | m + 1 | m + n
| n | m | m + n

Applying modulo m + n, we are able to guarantee victory as long as the current number of pencils is equal to 1 mod m + n.

# Demo

![Demo GIF](https://github.com/bmw02002turbo/pencil-game/blob/master/Pencil%20Game.gif)
