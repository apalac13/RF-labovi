import os
import pandas as pd
import hashlib
import magic
import mimetypes

# specify the directory path where the files are located
dir_path = '.\Lab2_download_1'

# create an empty list to store the file names
file_names = []
file_extension = []
md5s = []
sha1s  = []
sha256s = []
magic_numbers = []
extension_matches = []


hash_print = 'c15e32d27635f248c1c8b66bb012850e5b342119'

obj = magic.Magic(mime = True)


# iterate through all files in the directory
for file in os.listdir(dir_path):
    # check if the file is a regular file (i.e., not a directory)
    if os.path.isfile(os.path.join(dir_path, file)):
        # if so, add the file name to the list
        file_names.append(file)
        name, extension = os.path.splitext(file)
        file_extension.append(extension)
    
        md5s = hashlib.md5(file.encode()).hexdigest()
        sha1s = hashlib.sha1(file.encode()).hexdigest()
        sha256s = hashlib.sha256(file.encode()).hexdigest()


        magic_number = obj.from_file(os.path.join(dir_path, file))
        magic_numbers.append(magic_number)

        
        # check if the magic number contains the file extension
        if extension.lower() == '':
            extension_matches.append(False)
        elif mimetypes.guess_type('test'+extension.lower())[0] in magic_number.lower():
            extension_matches.append(True)
        else:
            extension_matches.append(False)


# create a Pandas dataframe with the file names
df = pd.DataFrame({'file_name': file_names, 'extension': file_extension, 'MD5': md5s, 'SHA1': sha1s, 'SHA256': sha256s, 'magic numbers': magic_numbers, 'extension matches': extension_matches})


# print the dataframe
print(df)

print(df(SHA1))
