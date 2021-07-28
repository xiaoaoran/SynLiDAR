# pip install pyDataverse (supports Python 3.6–3.8)

from pyDataverse.api import NativeApi, DataAccessApi

base_url = 'https://researchdata.ntu.edu.sg/'
api = NativeApi(base_url)
data_api = DataAccessApi(base_url)

DOI = "doi:10.21979/N9/BSKUOE"
dataset = api.get_dataset(DOI)

files_list = dataset.json()['data']['latestVersion']['files']

for file in files_list:
    filename = file["dataFile"]["filename"]
    file_id = file["dataFile"]["id"]
    print("Start downloading file name {} (id {}), please wait...".format(filename, file_id))

    response = data_api.get_datafile(file_id)
    with open(filename, "wb") as f:
        f.write(response.content)
    print("Finished\n")

print("Thank you for using synlidar. Wish you healthy and happy. --VIL@NTU")