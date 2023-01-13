import os
import pyperclip

# Prompt user for input
user_input = input("Enter a string to search for in file names: ")

# Find all files in the models directory (recursively) that start with the user input string
matches = set()
for root, dirs, files in os.walk("F:\\ai-art\\_models\\sd"): # replace with your own path
    for file in files:
        if file.startswith(user_input):
            file_name, file_ext = os.path.splitext(file)
            matches.add(user_input + ''.join(c for c in file_name[len(user_input):] if c not in matches))

# Sort the matches by name
matches = sorted(matches)

# Remove the terms "Weighted_sum-merged" and "SmoothStep" from the end of items in the list
terms_to_remove = ["Weighted_sum-merged", "SmoothStep"]
for i, match in enumerate(matches):
    for term in terms_to_remove:
        try:
            last_index = match.rindex(term)
            matches[i] = match[:last_index] + match[last_index+len(term):]
        except ValueError:
            pass

# Remove the last non-alphanumeric character from each item in the list,
#  unless it is a substring of another item in the list
new_list = []
for match in matches:
    if not match[-1].isalnum(): # check if last character is non-alphanumeric
        truncated_match = match[:-1] # remove last characterDBD
        if all(truncated_match not in m for m in new_list): # check if truncated match is not already in list
            new_list.append(truncated_match)
        else: # if so, keep the original match
            new_list.append(match)
    else:
        new_list.append(match)
matches = new_list

# Send the names of the files found as a comma-separated list to the clipboard
if matches:
    pyperclip.copy(', '.join(matches))
    print("File names copied to clipboard.")
else:
    print("No files found.")