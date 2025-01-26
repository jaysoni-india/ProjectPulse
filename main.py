import os
import pandas as pd

# Define the path to the CSV file
csv_path = 'inputs/members.csv'

# Check if the CSV file exists
if not os.path.exists(csv_path):
    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    
    # Create a DataFrame with the specified columns
    df = pd.DataFrame(columns=['name', 'email', 'jira_user_name', 'gitlab_user_name'])
    
    # Save the DataFrame to a CSV file
    df.to_csv(csv_path, index=False)
    print(f"CSV file created at {csv_path} with columns: name, email, jira_user_name, gitlab_user_name")
else:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_path)
    print(f"CSV file loaded from {csv_path}")

# Display the DataFrame
print(df)