# save_a_single_subdirectory_from_github
This function downloads a single sub-directory of a GitHub repository. All sub-folders in that sub-directory will be downloaded as well.
Params:
        repository_url: Shall be in this format: "https://github.com/<username>/<repository>
        subdirectory_of_repository: The subdirectory in the repository that you want to download it.
        local_save_path: The RELATIVE local path in the current folder of project that you want the files to be saved in.
        recursive: is a boolean parameter. If it is True, all the subfloders inside the subdirectory_of_repository will be downloaded. 
                   But if it is False, only the files will be downloaded and floders will be ignored.  

# save_a_single_file_from_github
This function downloads a single file from GitHub repository and save that in a specified folder.
File name will be the same as GitHub file name.

Params:
        url: to get url, browse to file directory in GitHub and right click on the file and click on "copy link address". paste it within "".
        save_folder: The RELATIVE local path in the current folder of project that you want the files to be saved in.
