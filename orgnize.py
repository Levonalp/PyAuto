import os
import shutil


def organize_files_by_extension(src_dir):
    # Iterate over all the entries
    for filename in os.listdir(src_dir):
        # If the entry is a file
        if os.path.isfile(os.path.join(src_dir, filename)):
            # Get file extension
            file_ext = filename.split('.')[-1]

            # Create a new directory if it doesn't exist
            new_dir = os.path.join(src_dir, file_ext)
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)

            # Move the file
            shutil.move(os.path.join(src_dir, filename),
                        os.path.join(new_dir, filename))


src_dir = '/path/to/your/directory'  # Specify your source directory
organize_files_by_extension(src_dir)
