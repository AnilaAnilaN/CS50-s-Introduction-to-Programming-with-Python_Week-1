def main():

    #get input from the user
    file_name = input("Please enter a valid file name along with it's extension to get it's media type: ")

    #1. remove any extra spaces using stript() before and after the user input
    #2. convert the input to lower case to deal with case sensitivity
    file_name = file_name.strip().lower()


    #check for the file extension in the user input and output the respective media type
    if file_name.endswith(".gif") :
        print("image/gif")
    elif file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
        print("image/jpeg")
    elif file_name.endswith(".png"):
        print("image/png")
    elif file_name.endswith(".pdf"):
        print("application/pdf")
    elif file_name.endswith(".txt"):
        print("text/plain")
    elif file_name.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")




main()
