# Problem 11: Container With Most Water
*Level: medium*
## Description
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

**Note:** You may not slant the container and n is at least 2.

**Example:**
```
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
```
## Solutions
### C, 3/12/2019
Analysis:
```c
#define area(left,right) (((right)-(left))*(*(left)>*(right)?*(right):*(left)))
int maxArea(int* height, int heightSize){
    if (heightSize < 2)
        return 0;
    int cur, res = 0;
    for (int i = 0; i < heightSize - 1; ++i)
        for (int j = i + 1; j < heightSize; ++j)
            if ((cur = area(height + i, height + j)) > res)
                res = cur;
    return res;
}
#undef area
```
Comments: