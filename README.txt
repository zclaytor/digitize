digitize.py
(c) Zachary R. Claytor
University of Florida
05 May 2023

This is my stupid brute-force solver to the Digits puzzle from the
New York Times. For today's puzzle, visit https://www.nytimes.com/games/digits.

This solver is horribly inefficient. In fact it's worse than brute force.
It tries a random combination of input numbers and operations until it gets the
right answer. It doesn't try to find the shortest solution. It doesn't even 
check to see if it's tried that combination before. And it will absolutely
multiply by 1 if the combination du jour calls for it. It does check to see if
a resulting answer is negative or a decimal, so there's that.

Here's an example using today's Digits:
Get 63 from 1, 2, 3, 4, 5, 25.

```
from digitize import solve
solve([1,2,3,4,5,25], 63)
```
>>> '25*5+1/2=63'
