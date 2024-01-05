def updateServerConfig(filename, keyword, value):
    #Read the file
    with open(filename,"r") as file:
        lines = file.readlines()

    with open(filename, "w") as file:
        for line in lines:
            if keyword in line:
                #update the exiting the value
                file.write(keyword + "=" + value + "\n")
            else:
                file.write(line)

def fileoperation():
    filedata = None
    try:
        # create the file
        with open("Filepyoperation.txt","w") as file:
            file.write("File is created using 'open' method and write mode")

        #read the file
        with open("Filepyoperation.txt","r") as file:
            filedata = file.read()
            # Replace the target string
            filedata = filedata.replace("is", "was")

        if filedata:
            with open("Filepyoperation.txt", "w") as file:
                file.write(filedata)

        #append the string in existing file
        with open("Filepyoperation.txt", "a") as file:
            file.write("\nNew line appended")
    except IOError:
        print("Exception occured during file operation")

if __name__ == "__main__":
    fileoperation()
    updateServerConfig("serverconf.ini", "MAX_CONNECTIONS", "500")