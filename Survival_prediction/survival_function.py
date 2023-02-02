import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load the data into a pandas DataFrame
df = pd.read_csv('data.csv')

# Define the event of interest and the time variable
event_col = 'death'
time_col = 'time'

# Sort the data by time
df.sort_values(time_col, inplace=True)

# Create an array of unique time points
unique_times = np.unique(df[time_col])

# Initialize arrays to store the cumulative hazard and number of subjects at risk
cumulative_hazard = np.zeros(len(unique_times))
n_at_risk = np.zeros(len(unique_times))

# Loop over each unique time point
for i, t in enumerate(unique_times):
    # Count the number of subjects at risk at this time point
    n_at_risk[i] = sum(df[time_col] >= t)

    # Count the number of events at this time point
    n_events = sum((df[time_col] == t) & (df[event_col] == 1))

    # Calculate the cumulative hazard at this time point
    if i == 0:
        cumulative_hazard[i] = n_events / n_at_risk[i]
    else:
        cumulative_hazard[i] = cumulative_hazard[i - 1] + n_events / n_at_risk[i]

# Load the cumulative hazard values from the previous calculation
cumulative_hazard = ... # Replace with the cumulative hazard values from the previous code
unique_times = ... # Replace with the unique time values from the previous code

# Calculate the survival function
survival_function = np.exp(-cumulative_hazard)

# Plot the survival function
plt.plot(unique_times, survival_function)
plt.xlabel('Time')
plt.ylabel('Survival Function')
plt.show()
