import os
import settings

def rename_low_size_images():
    directory = settings.TEMPPATH 
    # Define the size threshold (in bytes)
    size_threshold = settings.LOWRESMB * 1024 * 1024  # Convert MB to bytes
    
    for root, _, files in os.walk(directory):
        for filename in files:
            # Get the full path of the file
            file_path = os.path.join(root, filename)
            
            if os.path.isfile(file_path):
                resolution = ''
                file_size = os.path.getsize(file_path)
                file_name, file_extension = os.path.splitext(filename)
                readable_size = round(file_size / 1024 / 1024, 2)
                
                # Check if the filename already contains ISLOWRES or ISHIGHRES
                if settings.ISLOWRES in file_name or settings.ISHIGHRES in file_name:
                    print(f"Skipping: {filename} (already tagged with {settings.ISLOWRES} or {settings.ISHIGHRES})")
                    continue
                
                if file_size < size_threshold:
                    new_filename = f"{file_name}{settings.ISLOWRES}{file_extension}"
                    resolution = settings.ISLOWRES
                else:
                    new_filename = f"{file_name}{settings.ISHIGHRES}{file_extension}"
                    resolution = settings.ISHIGHRES
                
                new_file_path = os.path.join(root, new_filename)
                
                if settings.COMMITCHANGES:
                    os.rename(file_path, new_file_path)
                
                print(f"[{readable_size} Mb][{resolution}] {os.path.basename(file_path)} | ---> | {os.path.basename(new_file_path)} [Commit: {settings.COMMITCHANGES}]")

rename_low_size_images()
