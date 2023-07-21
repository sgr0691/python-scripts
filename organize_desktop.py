import os
import shutil

def organize_desktop():
    desktop_path = os.path.expanduser("~/Desktop")
    if not os.path.exists(desktop_path):
        print("Desktop path does not exist.")
        return

    # Defined categories and their corresponding extensions
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
        "Documents": [".doc", ".docx", ".pdf", ".txt"],
        "Videos": [".mp4", ".mov", ".avi"],
        "Music": [".mp3", ".wav", ".flac"],
        "Other": []  # Any file with an extension not in the above categories
    }

    # Create folders if they don't exist
    for folder in categories.keys():
        folder_path = os.path.join(desktop_path, folder)
        os.makedirs(folder_path, exist_ok=True)

    # Organized files
    for filename in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, filename)
        if os.path.isfile(file_path):  # Skip directories
            _, file_extension = os.path.splitext(filename)
            for category, extensions in categories.items():
                if file_extension.lower() in extensions:
                    new_folder_path = os.path.join(desktop_path, category)
                    shutil.move(file_path, new_folder_path)
                    break
            else:
                # Move to the "Other" folder if no matching category found
                other_folder_path = os.path.join(desktop_path, "Other")
                shutil.move(file_path, other_folder_path)

    print("Desktop organized successfully!")

if __name__ == "__main__":
    organize_desktop()
