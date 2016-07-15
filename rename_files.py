import os
def rename_files():
    #(1)  get file names from a folder
         file_list = os.listdir(r"C:\Python27\prank")
       # print(file_list)
         saved_path= os.getcwd()
         os.chdir("C:\Python27\prank")
    #(2) for each file, rename filename
         for file_name in file_list:
             print("The old name is "+file_name)
             os.rename(file_name,file_name.translate(None,"0123456789"))
             print("The new name is "+(file_name.translate(None,"0123456789")))
         os.chdir(saved_path)
        
rename_files()
