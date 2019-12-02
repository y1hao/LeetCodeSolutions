# Problem 6: ZigZag Conversion
*Level: medium*
## Description
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
```
P   A   H   N
A P L S I I G
Y   I   R
```
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
```
string convert(string s, int numRows);
```
**Example 1:**
```
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
```
**Example 2:**
```
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
```
## Solutions
### C, 2/12/2019
Analysis:
```c
char * convert(char * s, int numRows){
    int len = strlen(s);
    char * res = malloc(len + 1);
    if (numRows == 1)
    {
        strncpy(res, s, len);
        res[len] = '\0';
        return res;
    }
    int rep = 2 * numRows - 2;
    char *p = res;
    for (int i = 0; i * rep < len; ++i)
        *p++ = s[i * rep];
    for (int i = 1; i <= numRows - 2; ++i)
    {
        for (int j = 0; i + rep * j < len; ++j)
        {
            *p++ = s[i + rep * j];
            if (rep * (j + 1) - i < len)
                *p++ = s[rep * (j + 1) - i];
        }
    }
    for (int i = 0; i * rep + numRows - 1 < len; ++i)
        *p++ = s[i * rep + numRows - 1];
    *p = '\0';
    return res;
}
```
Comments: