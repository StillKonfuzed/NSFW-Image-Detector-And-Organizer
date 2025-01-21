import os
import settings

# Define the substrings to remove
SUBSTRINGS_TO_REMOVE = [settings.ISNUDE, settings.ISNOTNUDE, settings.ISCORRUPT, settings.ISLOWRES, settings.ISHIGHRES]

input_folder = settings.TEMPPATH 

for root, dirs, files in os.walk(input_folder):
    for filename in files:
        # Check if the file name contains any of the substrings
        if any(substring in filename for substring in SUBSTRINGS_TO_REMOVE):
            # Remove all specified substrings from the filename
            new_filename = filename
            for substring in SUBSTRINGS_TO_REMOVE:
                new_filename = new_filename.replace(substring, '')
            
            old_file_path = os.path.join(root, filename)
            new_file_path = os.path.join(root, new_filename)
            
            # Check if the target file already exists
            if os.path.exists(new_file_path):
                print(f"File already exists: '{new_file_path}'. Deleting existing file.")
                if settings.COMMITCHANGES:
                    os.remove(new_file_path)  # Delete existing file
            
            # Rename the file
            if settings.COMMITCHANGES:
                os.rename(old_file_path, new_file_path)
            
            print(f"Reset : '{os.path.basename(old_file_path)}' -> '{os.path.basename(new_file_path)}' [Commit: {settings.COMMITCHANGES}]")
