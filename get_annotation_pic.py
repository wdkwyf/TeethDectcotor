import os
import shutil
import string
list_dirs = os.walk('./eval_data/images')
for root,dir,files in list_dirs:
        for file in files:
            if file.find('new_images') != -1:
                newname=file.split('new_images')[-1]
                os.rename('./eval_data/images/'+file,'./eval_data/images/'+newname)