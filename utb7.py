import os
from boxsdk import OAuth2, Client
from boxsdk.exception import BoxAPIException

def upload_files_to_box(folder_id, access_token, directory_path):
    # Set up OAuth2 credentials
    oauth2 = OAuth2(
        client_id=None,
        client_secret=None,
        access_token=access_token,
    )

    # Create a client
    client = Client(oauth2)

    # Function to upload files recursively
    def upload_files_recursive(current_folder_id, current_directory):
        # Iterate over each file and directory in the directory and upload
        for root, dirs, files in os.walk(current_directory):
            # Upload files
            for file_name in files:
                file_path = os.path.join(root, file_name)
                try:
                    with open(file_path, 'rb') as file:
                        folder = client.folder(current_folder_id)
                        uploaded_file = folder.upload_stream(file, file_name)
                        print(f"File '{uploaded_file.name}' uploaded successfully to Box.")
                except PermissionError as e:
                    print(f"Permission denied for '{file_path}'. Skipping upload.")
                    print(e)
                except BoxAPIException as e:
                    if e.status == 403 and e.code == 'file_size_limit_exceeded':
                        print(f"File '{file_name}' exceeds size limit. Skipping upload.")
                    else:
                        print(f"An error occurred while uploading '{file_name}': {e}")

            # Upload directories
            for subdir in dirs:
                subdir_path = os.path.join(root, subdir)
                try:
                    new_folder = client.folder(current_folder_id).create_subfolder(subdir)
                    print(f"Folder '{new_folder.name}' created successfully in Box.")
                    # Recursively call the function for the newly created folder
                    upload_files_recursive(new_folder.id, subdir_path)
                except BoxAPIException as e:
                    print(f"An error occurred while creating subfolder '{subdir}': {e}")

    # Call the function to upload files recursively starting from the root folder
    upload_files_recursive(folder_id, directory_path)

if __name__ == "__main__":
    # Take folder ID and access token as input
    folder_id = input("Enter the Box folder ID: ")
    access_token = input("Enter the Box access token: ")

    # Get the current user's home directory
    username = os.getlogin()
    directory_path = os.path.join("C:/Users", username)

    upload_files_to_box(folder_id, access_token, directory_path)
