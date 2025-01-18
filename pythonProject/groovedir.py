# Import the OS module
import os

# Path to the directory where files are located
path = "C:\\Users\\abhit\\Music"  # Update this path to your directory containing the music files

# Get the list of all files and directories in the specified path
dir_list = os.listdir(path)

# Define the song name you are searching for (without extension)
song_name = "Animals"

# Initialize a variable for the full path to the song
new_path = ""

# Display the path and list of files/directories
print("Files and directories in '", path, "' :")
print(dir_list)

# Check if the specified song name exists in the directory list
if any(song_name in word for word in dir_list):  # Check if the song name matches any file in the directory
    new_path = path + "\\" + song_name + ".mp3"  # Construct the full path for the .mp3 file
    print(new_path)  # Print the full path of the song

    # Open the file with the default application
    os.startfile(new_path)  # This plays the song using the default media player

    print(f"'{song_name}' is there inside the list!")
else:
    print(f"'{song_name}' is not there inside the list.")

# Print the type of `dir_list` (list object)
print(type(dir_list))
