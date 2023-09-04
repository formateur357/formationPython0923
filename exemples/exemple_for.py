#! /usr/bin/env python3
# -*- coding: utf-8 -*-

months = { 1: "Janvier", 2: "Fevrier", 3: "Mars", 4: "Avril", 5: "Mai", 6: "Juin", 7: "Juillet", 8: "August"}

for month in months.values():
    if month == "Juillet":
        break
    print(f"{month}")
    
print(f"\n{month}")

for m, month in months.items():
    if m > 6:
        break
    print(f"{m}: {month}")
    
print(f"\n{m}: {month}")

for m in months:
    if m > 6:
        break
    print(f"{m}: {months[m]}")
    
print(f"\n{m}: {months[m]}")