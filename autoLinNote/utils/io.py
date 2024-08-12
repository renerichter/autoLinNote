from os import path, walk


def get_file_list(file_path)->list:
    if path.exists(file_path):
        if path.isdir(file_path):
            file_list = [path.join(dirpath,f) for (dirpath,dirnames,filenames) in walk(file_path) for f in filenames]
            return file_list
        else: 
            return file_path
    else: 
        raise IOError(f"Path {file_path} not existing")