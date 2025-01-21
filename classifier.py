import os
from nudenet import NudeDetector
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
import settings

# Initialize the NudeDetector model once for all threads
detector = NudeDetector()

input_folder = settings.TEMPPATH

# List of nudity classes to check for
nudity_classes = {
    "BUTTOCKS_EXPOSED",
    "FEMALE_BREAST_EXPOSED",
    "FEMALE_GENITALIA_EXPOSED",
    "MALE_BREAST_EXPOSED",
    "ANUS_EXPOSED",
    "MALE_GENITALIA_EXPOSED",
}

image_files = [
    os.path.join(root, filename)
    for root, _, files in os.walk(input_folder)
    for filename in files
    if all(x not in filename for x in (settings.ISNUDE, settings.ISNOTNUDE,settings.ISCORRUPT))
    and filename.lower().endswith(('.png', '.jpg', '.jpeg'))
]

def process_image(image_path):
    filename = os.path.basename(image_path)
    try:
        result = detector.detect(image_path)
        is_nude = any(detection['class'] in nudity_classes and detection['score'] > 0.5 for detection in result)
        
        # Rename based on nudity detection
        if is_nude:
            new_filename = f"{settings.ISNUDE+filename}"
        else:
            new_filename = f"{settings.ISNOTNUDE+filename}"

        # Rename the file
        new_image_path = os.path.join(os.path.dirname(image_path), new_filename)
        if settings.COMMITCHANGES:
            os.rename(image_path, new_image_path)
        return is_nude, filename, new_filename
    except Exception as e:
        #Rename corrupt files
        corrupt_filename = f"{settings.ISCORRUPT+filename}"
        # corrupt_image_path = os.path.join(os.path.dirname(image_path), corrupt_filename)
        # os.rename(image_path, corrupt_image_path) 
        print(f"Error processing '{filename}': {e}") 


total_images = len(image_files)
with ThreadPoolExecutor() as executor:
    futures = {executor.submit(process_image, img): img for img in image_files}
    for i, future in enumerate(as_completed(futures)):
        is_nude, filename, new_filename = future.result()
        percentage = (i + 1) / total_images * 100 
        remaining = total_images - (i + 1) 
        print(f"[{remaining}/{total_images}] | {is_nude} | {percentage:.2f}% | '{filename}' ====> '{new_filename}' [Commit : {settings.COMMITCHANGES}]")
        
print("Nudity detection completed.")