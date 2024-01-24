import os

def download_data(url, data_dir="./fits"):
    """
    Download a dataset via wget

    Parameters
    ----------
    url: str
        web address of file to be retrieved
    dir: str
        Directory where the dataset will be stored

    """

    data_dir = os.path.expanduser(data_dir)
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    data_file = url.split("/")[-1]
    
    if os.path.exists(os.path.join(data_dir, data_file)):
        print(data_file, "already downloaded")
    else:
        print("\nDownloading data...\n", data_file)
        try:
            cmd = 'wget '+url+'; mv '+data_file+' '+data_dir
            os.system(cmd)
        except:
            cmd = 'curl -O'+url+'; mv '+data_file+' '+data_dir
            os.system(cmd)
        print(cmd)
        
        
    return os.path.join(data_dir, data_file)

# return subscript number or text as a string
def sub(Input):
    return r'$_{'+str(Input)+'}$'

# return superscript number or text as a string
def sup(Input):
    return r'$^{'+str(Input)+'}$'