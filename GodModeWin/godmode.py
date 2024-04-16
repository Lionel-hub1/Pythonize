import os


def create_godmode_folder():
    # Get the user's Desktop path
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    # Create the GodMode folder
    godmode_folder_path = os.path.join(
        desktop_path, "GodMode.{ED7BA470-8E54-465E-825C-99712043E01C}")
    os.makedirs(godmode_folder_path, exist_ok=True)

    print("GodMode folder created successfully!")


if __name__ == "__main__":
    create_godmode_folder()
