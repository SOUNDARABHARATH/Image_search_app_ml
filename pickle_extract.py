import pickle
import os
from PIL import Image
import shutil

# Path to your pickle file
pickle_file_path = "D:/Placement projects/ImageSearcher/out1/stored_embeddings.pickle"
output_folder = os.path.dirname(pickle_file_path)  # Use the same folder where the pickle file is

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Load the pickle file
with open(pickle_file_path, 'rb') as f:
    stored_embeddings = pickle.load(f)

# Check if the embeddings contain image paths (assuming they do)
for key, value in stored_embeddings.items():
    image_path = value.get("image_path")  # Assuming the pickle file contains image paths

    if image_path and os.path.exists(image_path):
        # Extract the image filename
        image_filename = os.path.basename(image_path)

        # Define the target save path (in the same folder as pickle file)
        target_save_path = os.path.join(output_folder, image_filename)

        # Copy or save the image to the target folder
        try:
            # Use shutil to copy the image to the output folder
            shutil.copy(image_path, target_save_path)
            print(f"Copied {image_filename} to {output_folder}")
        except Exception as e:
            print(f"Failed to copy {image_filename}: {e}")
    else:
        print(f"Image path not found or invalid for key: {key}")
