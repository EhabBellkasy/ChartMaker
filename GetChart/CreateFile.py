








import os

def fun (   directory = "TikerName", # Directory Name
            parent_dir = r'D:\Python Tools\ChartMaker\SourceDocuments\OutPut_jpg' # Parent Directory path
        
        ):
    # Help link :- https://www.geeksforgeeks.org/create-a-directory-in-python/                
    # Path
        path = os.path.join(parent_dir, directory)
    # Create the directory
        os.mkdir(path)
    # Return the Path of Direvtory
        return path
















