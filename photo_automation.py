import os

# Specify the path to the directory containing the folders
directory_path = r'C:\Users\Rozakos_Home\Desktop\Eshop_Photos\Dungeons_And_Dragons\Miniatures\Rescale_Miniatures'

# List of common image file extensions
image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')

# Walk through all folders and subfolders
for root, dirs, files in os.walk(directory_path):
    # Filter out image files
    image_files = [file for file in files if file.lower().endswith(image_extensions)]

    if image_files:  # Check if there are any image files
        print(f"\nFolder: {root}")
        for image in image_files:
            print(f"  {image}")

print("\nDone listing all images.")
