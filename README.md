# sd-toolbox
Tools for working with stable diffusion

## get_model_checkpoints.py

This script searches for files in a specified directory (recursively) that start with a user-provided string, and sends the names of the files found as a comma-separated list to the clipboard. 

1. The script will search the specified directory (F:\\ai-art\\_models\\sd) and its subdirectories for files that start with the entered string.
2. The script will remove "Weighted_sum-merged" and "SmoothStep" from the end of the file names.
3. The script will remove the last non-alphanumeric character from each file name, unless it is a substring of another file name.

### Usage

1. Clone or download the script to your local machine.
2. Run the script with python.
3. You will be prompted to enter a string to search for in file names.
4. The script will sort the file names and copy them to the clipboard as a comma-separated list.

### Configuration

You can change the directory that the script searches by modifying the `path` variable.
You can also add, remove, or modify the file extensions that the script accepts by modifying the `file_extensions` variable.

### Dependencies

This script requires the `pyperclip` module. Make sure it is installed before running the script.

### License

This script is available under the [MIT License](https://opensource.org/licenses/MIT).

### How to contribute

If you would like to contribute to this script, feel free to fork the repository and submit a pull request.

### How to report issues

If you encounter any issues while using this script, please open an issue on the [Github repository](https://github.com/PixelDJ/sd-toolbox)

#### Note

This script is for demonstration purposes only, and should be modified to fit the specific use case before use.
