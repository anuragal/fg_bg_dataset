# importing os module 
import os 
import os, sys
from PIL import Image
import numpy as np
  
import io
# Function to rename multiple files 
def main(): 
  
    base_folder = os.path.join("C:\\", "Anurag", "Personal", "ML", "EVA", "github", "fg_bg_dataset")

    img_folder = os.path.join(base_folder, "fg_140")
    for count, filename in enumerate(os.listdir(img_folder)):
        count = count + 1
        a = filename.split('.')
        ext = a[len(a) - 1]
        
        new_filename ="fg_" + str(f'{count:03}') + "." + ext
        # rename() function will 
        # rename all the files 
        src = os.path.join(img_folder, filename)
        dst = os.path.join(base_folder, "fg", new_filename)
        os.rename(src, dst) 
  
def add_image_entries():
    base_folder = "C:\Anurag\Personal\ML\EVA\github\yolo_custom_dataset\data\customdata"
    img_folder = os.path.join(base_folder, "images")

    txt_file = os.path.join(img_folder, "custom.txt")
    with open(txt_file, "w") as f:
        for count, filename in enumerate(os.listdir(img_folder)):
            f.write("./data/customdata/images/" + filename + "\n")
             
# Driver Code 
if __name__ == '__main__': 
     
    print("main claaed")     
    #main()
    # add_image_entries()