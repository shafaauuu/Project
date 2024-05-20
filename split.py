import pandas as pd

# Read the original Excel file into a DataFrame
original_data = pd.read_excel('E:/Natural Language Processing/Project/ML/dataset/doc_classification.xlsx')

# Shuffle the DataFrame to ensure randomness
shuffled_data = original_data.sample(frac=1, random_state=42)  # Set random_state for reproducibility

# Calculate the index to split the data
split_index = int(0.8 * len(shuffled_data))

# Split the DataFrame into training and testing sets
train_data = shuffled_data[:split_index]
test_data = shuffled_data[split_index:]

# Write the training and testing sets to new Excel files
train_data.to_excel('E:/Natural Language Processing/Project/ML/dataset/train_data.xlsx', index=False)
test_data.to_excel('E:/Natural Language Processing/Project/ML/dataset/test_data.xlsx', index=False)
