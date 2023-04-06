import requests
import os

def save_a_single_subdirectory_from_github(repository_url: str, subdirectory_of_repository: str, local_save_path: str, recursive:bool = True):
    """
    This function downloads a single sub-directory of a GitHub repository
    All sub-folders in that sub-directory will be downloaded as well.

    Params:
        repository_url: Shall be in this format: "https://github.com/<username>/<repository>
        subdirectory_of_repository: The subdirectory in the repository that you want to download it.
        local_save_path: The RELATIVE local path in the current folder of project that you want the files to be saved in.
        recursive: is a boolean parameter. If it is True, all the subfloders inside the subdirectory_of_repository will be downloaded. But if it is False, only the files will be downloaded and floders will be ignored.  
    """
    # Extract the 'username/repository' from url
    main_repo_address = repository_url[19:]

    api_url = f"https://api.github.com/repos/{main_repo_address}/contents/{subdirectory_of_repository}?ref=main"
    # url = "https://api.github.com/repos/mrdbourke/pytorch-deep-learning/contents/going_modular?ref=main"

    os.makedirs(local_save_path,exist_ok=True)

    # Send a GET request to the API endpoint to get the contents of the folder
    response = requests.get(api_url)

    # Iterate over the contents of the folder in the API response
    for file in response.json():
        # Skip the file if it's a subdirectory
        try:
            if file["type"] == "dir" and recursive == True:
                save_a_single_subdirectory_from_github(repository_url,file["path"], os.path.join(local_save_path, file["name"]))
                print(f'{os.path.join(local_save_path, file["name"])}, copied!')
            # Get the download URL of the file
            download_url = file["download_url"]
            # Define the path and filename of the file you want to save on your local machine
            filename = file["name"]
            file_path = os.path.join(local_save_path, filename)
            # Send a GET request to the download URL to download the file contents
            file_response = requests.get(download_url)
            # Write the contents of the response to a file on your local machine
            with open(file_path, "wb") as f:
                f.write(file_response.content)
        except:
            pass


def save_a_single_file_from_github(url:str, save_folder:str=""):
    """
    This function downloads a single file from GitHub repository and save that in a specified folder.
    File name will be the same as GitHub file name.

    Params:
        url: to get url, browse to file directory in GitHub and right click on the file and click on "copy link address". paste it within "".
        save_folder: The RELATIVE local path in the current folder of project that you want the files to be saved in.
    """
    
    raw_url = url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
    filename = os.path.basename(url)
    response = requests.get(raw_url)
    save_address = os.path.join(save_folder, filename)
    if save_folder != "":
        os.makedirs(save_folder, exist_ok=True)

    if response.status_code == 200:
        content = response.content
        with open(save_address, "wb") as f:
            f.write(content)
    else:
        print("Error: could not download file")
