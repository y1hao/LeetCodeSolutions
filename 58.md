# Problem 58: Length of Last Word
*Level: easy*
## Description
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.
## Solutions
### C, 18/11/2019
Analysis:
```c
int lengthOfLastWord(char * s){
    int len = 0;
    bool inspace = true;
    char cur;
    while ((cur = *s++) != '\0')
    {
        if (isspace(cur))
            inspace = true;
        else if(inspace)
        {
            inspace = false;
            len = 1;
        }
        else
            ++len;
    }
    return len;
}
```
Comments: