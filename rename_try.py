import os
def rename_files():
    file_list = os.listdir(r"C:\Python27\prank")
    saved_path= os.getcwd()
    os.chdir("C:\Python27\prank")
    file_name="austin.jpg"
    os.rename(file_name,"athens.jpg")
rename_files()
    
