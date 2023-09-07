#! /usr/bin/env python3

import pandas as pd

data = pd.read_json('/Users/morganguy/Formation_Workspace/formationPython0923/exercices/meteo.json')

print(data)

df = pd.DataFrame(data['results'])

print(df)