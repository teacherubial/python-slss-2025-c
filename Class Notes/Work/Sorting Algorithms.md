## Sorting Algorithms

> Given the following list, using selection sort, sort the indicated element. Outline the steps you would follow in a way similar to the notes.

```
The List:

-- indicates that this part of the list is already sorted
** indicates the element that you should sort

  --  --  **   3    4   5
[-11,  1, 55, 43, 100, 34]

    0  1  **   3    4   5
[-11,  1, 55, 43, 100, 34]

lowest_num   = 1
lowest_index = 0

First Comparison (* indicates the entry we're sorting, %% indicates the current entry we're comparing)
    0  1  **   3    4   5
[-11,  1, 55, 43, 100, 34]

lowest_num   = 1
current_num  = -11
lowest_index = 0

"current_num isn't lower, move on to the next one"

2nd Comparison
--------------
 *   1  %%    3    4   5
[-11,  1, 55, 43, 100, 34]lowest_num   = 1
current_num  = 55
lowest_index = 0"current_num still isn't lower, move on to the next one"3rd Comparison
--------------
 *   1   2   %%    4   5
[-11,  1, 55, 43, 100, 34]lowest_num   = 1
current_num  = 43
lowest_index = 0"current_num is now lowest! set lowest_num to -11, and lowest_index to 3"New values:
lowest_num = -11
lowest_index = 3```


Message Sarah
:bell:Slack needs your permission to enable notifications. 