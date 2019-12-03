# Problem 10: Regular Expression Matching
*Level: hard*
## Description
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

**Note:**

    - s could be empty and contains only lowercase letters a-z.
    - p could be empty and contains only lowercase letters a-z, and characters like . or *.

**Example 1:**
```
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```
**Example 2:**
```
Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
```
**Example 3:**
```
Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
```
**Example 4:**
```
Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
```
**Example 5:**
```
Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
```

## Solutions
### C, 3/12/2019
Analysis:
```c
#define MATCH(sc, pc) ((pc) == '.' || (pc) == (sc))
struct ele {
    struct ele *next;
    char c;
    bool mult;
};
bool _match (char * s, struct ele *e)
{
    if (*s == '\0' && e->c == '\0')
        return true;
    else if (e->c == '\0')
        return false;
    if (e->mult)
    {
        if (_match(s, e->next))
            return true;
        while (*s != '\0' && MATCH(*s, e->c))
        {
            if (_match(s + 1, e->next))
                return true;
            ++s;
        }
    }
    else
        if (*s != '\0' && MATCH(*s, e->c))
            return _match(s + 1, e->next);
    return false;
}
bool isMatch(char * s, char * p){
    struct ele head = {NULL, 0, false}, *cur = &head;
    while (*p++ != '\0')
    {
        cur->next = malloc(sizeof(struct ele));
        cur = cur->next;
        cur->next = NULL;
        cur->c = *(p - 1);
        if (*p == '*')
        {
            cur->mult = true;
            ++p;
        }
        else
            cur->mult = false;
    }
    cur = cur->next = malloc(sizeof(struct ele));
    cur->c = '\0';
    cur->next = NULL;
    bool res = _match(s, head.next);
    for (struct ele *pe = head.next, *qe; pe; pe = qe)
    {
        qe = pe->next;
        free(pe);
    }
    return res;
}
#undef MATCH
```
Comments: