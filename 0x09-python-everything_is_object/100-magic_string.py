#!/usr/bin/python3
def magic_string(count_var={"count": 0}):
    count_var["count"] += 1
    return str("BestSchool, " * count_var["count"])[:-2]
