import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='rename_images.log')

def rename_images(root_dir):
    for root, _, files in os.walk(root_dir):
        images = [f for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        for count, image in enumerate(images, 1):
            try:
                # Extract the relative path and remove the root directory part
                relative_path = os.path.relpath(root, root_dir)
                # Split the relative path into parts and join with '_'
                new_name = '_'.join(relative_path.split(os.sep)) + f'_{count}'
                # Get the file extension
                ext = os.path.splitext(image)[1]
                # Full new name with extension
                new_name_with_ext = new_name + ext
                # Full old and new file paths
                old_file = os.path.join(root, image)
                new_file = os.path.join(root, new_name_with_ext)
                # Rename the file
                os.rename(old_file, new_file)
                # Log and print success message
                message = f'Renamed: {old_file} to {new_file}'
                logging.info(message)
                print(message)
            except Exception as e:
                # Log and print error message
                error_message = f'Error renaming {old_file} to {new_file}: {e}'
                logging.error(error_message)
                print(error_message)

# Example usage
root_directory = r'C:\Users\Rozakos_Home\Desktop\Eshop_Photos\Dungeons_And_Dragons'
print(f"Starting to rename images in {root_directory}")
rename_images(root_directory)
print("Finished renaming images.")
