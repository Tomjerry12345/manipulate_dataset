import os

# Get the list of all files and directories
base_path = "C://Users//Andri//3D Objects//luffy-dev//project//Web//React " \
       "js//klasifikasi-daun-react-js//public//dataset//"
path_daun_cengkeh = base_path + "cacar_daun_cengkeh//"
path_embun_jelaga = base_path + "embun_jelaga//"
path_kutu_daun = base_path + "kutu_daun//"

dir_list = os.listdir(path_kutu_daun)

# prints all files
print(dir_list)

for i in range(0, len(dir_list)):
    # print(dir_list[i])
    new_name = path_kutu_daun + str(i + 1) + ".jpg"
    old_name = path_kutu_daun + dir_list[i]
    if os.path.isfile(new_name):
        print("The file already exists")
    else:
        # Rename the file
        os.rename(old_name, new_name)
        print("Succes change name")


