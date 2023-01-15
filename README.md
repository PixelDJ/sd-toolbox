# sd-toolbox
Tools for working with stable diffusion. Eventually this will be one program, but for now it is mostly a collection of scripts.

## xy_plot_helpers
These are scripts to quickly copy information to use in the xy plot script in the stable diffusion webui.

## copy_chckpoints.py

This script searches for files in a specified directory (recursively) that start with a user-provided string, and sends the names of the files found as a comma-separated list to the clipboard. 

1. The script will search the specified directory (F:\\ai-art\\_models\\sd by default) and its subdirectories for files that start with the entered string.
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

## copy_samplers.py

This script allows you to extract the names of the samplers from the sd_samplers.py file located inside the stable-diffusion folder. It will then copy the names of the samplers as a comma-separated list to your clipboard.

### Usage

1. Run the script
2. Input the location of the 'stable diffusion' folder. If the folder is located at the default location 'F:\ai-art\stable-diffusion-local', you can just press enter.
3. The script will parse the sd_samplers.py file and extract the names of the samplers
4. The names will be copied to your clipboard

### Requirements
- Python 3
- pyperclip library

### Note
- Make sure to check the file path and location of the sd_samplers.py file in the script before running it.

### License

These scripts are available under the [MIT License](https://opensource.org/licenses/MIT).

### How to contribute

If you would like to contribute to this project, feel free to fork the repository and submit a pull request.

### How to report issues

If you encounter any issues while using this, feel free to open an issue on the [Github repository](https://github.com/PixelDJ/sd-toolbox)

#### Note

This script is for demonstration purposes only, and should be modified to fit the specific use case before use.
