# Problem 20: Valid Parenthesis
*Level: easy*
## Description
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.
**Example 1:**
```
Input: "()"
Output: true
```
**Example 2:**
```
Input: "()[]{}"
Output: true
```
**Example 3:**
```
Input: "(]"
Output: false
```
**Example 4:**
```
Input: "([)]"
Output: false
```
**Example 5:**
```
Input: "{[]}"
Output: true
```
## Solutions
### C, 18/11/2019
Analysis:
```c
#define MAX_LEN 10000
bool isValid(char * s){
    char stack[MAX_LEN];
    char match[256];
    match[')'] = '(';
    match[']'] = '[';
    match['}'] = '{';
    int sp = 0;
    char cur;
    while((cur = *s++) != '\0')
        switch (cur)
        {
            case '(': case '[': case '{':
                stack[sp++] = cur;
                break;
            case ')': case ']': case '}':
                if (sp == 0 || stack[sp - 1] != match[cur])
                    return false;
                else
                    --sp;
                break;
            default: break;
        }
    return sp == 0;
}


```
Comments: