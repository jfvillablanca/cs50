file_name = input("File name: ").strip().lower()
file_extension = file_name.split(sep=".")[-1:][0]
match file_extension:
    case "gif" | "png":
        print(f"image/{file_extension}")
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "pdf" | "zip":
        print(f"application/{file_extension}")
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")
