#!/usr/bin/python3
# -*- coding: utf-8 -*-

# This script updates the problems table in README.md
# It needs to be run every time new solutions are added to the project

import os
import re

info = """# Leetcode Solutions

*Author: Yihao Wang*

This repository contains my record of [Leetcode](https://leetcode.com/) training.

The goal is to use C to solve all problems in the beginning 400 which do not require a subscription.

I also take part in weekly contests occasionaly, the problems from contests are mainly implemented in JavaScript.

Here is a reference table for all the problems I have solved up to now. The plan is to include an analysis to the problem and some comments on the implementation in each problem's markdown. However, these parts may be missing in some recently solved problems, since they take time to complete.
"""
base = "https://github.com/CoderYihaoWang/LeetCodeSolutions/blob/master/"
thead = """|No.|Title|Diffuculty|Language|First Solved|
|---|---|---|---|---|"""
rsolution = re.compile(r"\d+_.+\.md")
rdifficulty = re.compile(r"\*Level: (\S+)\*")
rlang = re.compile(r"```(\S+)")
rtime = re.compile(r".+\, (\d+\/\d+\/\d+)")

content = []
solutions = filter(lambda x:rsolution.match(x), os.listdir("."))
for solution in solutions:
    words = solution.split(".")[0].split("_")
    number = words[0]
    title = "[" + " ".join(words[1:]) + "](" + base + solution + ")"
    difficulty = ""
    language = ""
    time = ""
    with open(solution, "r") as f:
        for line in f.readlines():
            l = rlang.match(line)
            if l:
                if not language:
                    language = l.group(1)
                else:
                    language += "/" + l.group(1)
            if not difficulty:
                d = rdifficulty.match(line)
                if d: difficulty = d.group(1)
            if not time:
                t = rtime.match(line)
                if t: time = t.group(1)
    content.append((number, title, difficulty, language, time))
content.sort(key = lambda x:int(x[0]))
with open("README.md", "w") as out:
    print(info, file = out)
    print(thead, file = out)
    for record in content:
        print("|", end = "", file = out)
        for field in record:
            print(field, end = "|", file = out)
        print("", file = out)