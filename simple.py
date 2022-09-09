import random
import pandas as pd

def get_num_lines(fname):
    with open(fname) as f:
        for i, _ in enumerate(f):
            pass
    return i + 1

num_lines = get_num_lines("no_nan.csv") - 1

# How many randomn rows do you want?
sample_size = 400
rows_to_skip = random.sample(range(1,num_lines), num_lines-sample_size)

df = pd.read_csv("no_nan.csv", skiprows=rows_to_skip)
df.to_csv('survey_2.csv', index=False, header = None)
