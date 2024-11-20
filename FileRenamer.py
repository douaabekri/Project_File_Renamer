import os

class File:
    @staticmethod
    def FileRenamer():
        dir = input("\033[33m "+"Enter Files and Folders Directory: "+"\033[00m")
        if not os.path.isdir(dir):
            print("\033[31m "+"Invalid directory."+"\033[00m")
            return

        items = os.listdir(dir)
        new_name_base = input("\033[33m "+"Enter New Base Name: "+"\033[00m")
        counter = 1

        for item in items:
            item_path = os.path.join(dir, item)
            
           
            if os.path.isfile(item_path):
                file_ext = os.path.splitext(item)[1].lower()
                new_name = f"{new_name_base}_{counter}{file_ext}"
            else:
                
                new_name = f"{new_name_base}_{counter}"
            
            new_item_path = os.path.join(dir, new_name)
            os.rename(item_path, new_item_path)
            counter += 1

        print("\033[34m "+"Renaming Completed."+"\033[00m")
