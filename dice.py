# Rolling a die 1000 times and give results in tabular form

import random
import numpy as np
import pandas as pd

# Number of times to roll the die
roll_times = np.arange(1,1001)

# List comprehension to represent the faces of the die
die_faces = [i for i in range(1,7)]

# Dictionary to store the frequency of each face
frequency_dict = {face: 0 for face in die_faces}


for roll in roll_times:
    result = random.choice(die_faces)
    frequency_dict[result] += 1

# Getting the percentage
percentage_list = []
for key in frequency_dict.keys():
    value = frequency_dict[key] / len(roll_times)
    percentage_list.append(value)

# Converting the dictionary to a pandas dataframe
df = pd.DataFrame(list(frequency_dict.items()),columns=['Face','Frequency'])

# Adding the percentage column
df['Percentage'] = percentage_list

print(df)


