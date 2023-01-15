import os
import pyperclip

class GetCheckpoints:
    def __init__(self, user_input, path):
        self.user_input = user_input
        self.path = path
        self.file_extensions = file_extensions
        self.matches = set()
    
    def search_files(self):
        """Find all files in the models directory (recursively) that start with the user input string"""
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file.startswith(self.user_input):
                    file_name, file_ext = os.path.splitext(file)
                    if file_ext in self.file_extensions:
                        self.matches.add(self.user_input + ''.join(c for c in file_name[len(self.user_input):] if c not in self.matches))
        self.matches = sorted(self.matches)

    def remove_terms(self, terms_to_remove):
        """Remove extra terms from the end of items in the list"""
        for i, match in enumerate(self.matches):
            for term in terms_to_remove:
                try:
                    last_index = match.rindex(term)
                    self.matches[i] = match[:last_index] + match[last_index+len(term):]
                except ValueError:
                    pass
    
    def remove_non_alphanumeric(self):
        """Remove the last non-alphanumeric character from each item in the list, unless it is a substring of another item in the list"""
        new_list = []
        for match in self.matches:
            if not match[-1].isalnum():
                truncated_match = match[:-1]
                if all(truncated_match not in m for m in new_list):
                    new_list.append(truncated_match)
                else:
                    new_list.append(match)
            else:
                new_list.append(match)
        self.matches = new_list
    
    def get_model_checkpoints(self):
        self.search_files()
        self.remove_terms(["Weighted_sum-merged", "SmoothStep"])
        self.remove_non_alphanumeric()
        if self.matches:
            pyperclip.copy(', '.join(self.matches))
            print("File names copied to clipboard.")
        else:
            print("No files found.")

if __name__ == "__main__":
    user_input = input("Enter a string to search for in file names: ")
    path = "F:\\ai-art\\_models\\sd"  # replace with your own path
    file_extensions = ['.ckpt', '.safetensors']
    model_checkpoints = GetCheckpoints(user_input, path)
    model_checkpoints.get_model_checkpoints()
