import os
import shutil

def delete_content_destination(path: str):

    if not os.path.exists(path):
        raise Exception("path does not exist")
    else:
        print(f"deleting all files in {path}\n")
        shutil.rmtree(path)
        os.mkdir(path)
    


def copy_files(path,destination):
    all_paths = []
    path_content = os.listdir(path)
    for paths in path_content:
        extended_path = os.path.join(path,paths)

        if os.path.isfile(extended_path): 
            all_paths.append(extended_path)
            print(f"copying {extended_path} to {destination}\n")
            shutil.copy(extended_path,destination)

        else:
            new_destination = f"{destination}/{paths}"
            os.mkdir(new_destination)
            print(f"created new directory, path: {new_destination} \n")
            copy_files(extended_path,new_destination)

    print(f"successfully copied all files and directories from {path} to {destination} \n")
    return 


