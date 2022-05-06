import zipfile
with zipfile.ZipFile("/home/ragu/Training.zip", 'r') as zip_ref:
    zip_ref.extractall("/home/ragu")