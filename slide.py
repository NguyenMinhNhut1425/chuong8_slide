# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 19:18:18 2024

@author: MINH NHUT
"""

dictUni = {
    520189: "MIT",
    "IT": "Information Technology",
    "SE": "Computer Engineering",
    "CS": "Computer Science"}
print(dictUni[520189])
print(dictUni["SE"])
dictUni["DS"] = 'Data Science'
print(dictUni)

#del dictUni["IT"]
#print(dictUni)

#dictUni.clear()
#print(dictUni)
#del dictUni

dictUni["CS"] = "Com. Sci."
print(dictUni)
print(len(dictUni))
print(str(dictUni))
print(dictUni.copy())
print(dictUni.get("SE"))
print(dictUni.items())
print(dictUni.fromkeys(dictUni["SE"]))
print(dictUni.keys())
ds2 = {"một": 1}
dictUni.update(ds2)
print(dictUni)
print(dictUni.pop("một"))
print(dictUni.values())
print(dictUni.setdefault("một"))


