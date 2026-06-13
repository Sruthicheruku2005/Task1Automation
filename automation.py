import os
import shutil
folder_path = input("Enter folder name: ")
def write_log(message):
    with open("logs.txt", "a") as log:
        log.write(message + "\n")
try:
    files = os.listdir(folder_path)
    text_count = 1
    image_count = 1
    pdf_count = 1
    for file in files:
        source = os.path.join(folder_path, file)
        if os.path.isfile(source):
            if file.endswith(".txt"):
                new_name = f"text_{text_count}.txt"
                destination = os.path.join(
                    folder_path,
                    "Text",
                    new_name
                )
                shutil.move(source, destination)
                write_log(f"{file} moved to Text as {new_name}")
                text_count += 1
            elif file.endswith(".jpg"):
                new_name = f"image_{image_count}.jpg"
                destination = os.path.join(
                    folder_path,
                    "Images",
                    new_name
                )
                shutil.move(source, destination)
                write_log(f"{file} moved to Images as {new_name}")
                image_count += 1
            elif file.endswith(".pdf"):
                new_name = f"pdf_{pdf_count}.pdf"
                destination = os.path.join(
                    folder_path,
                    "PDF",
                    new_name
                )
                shutil.move(source, destination)
                write_log(f"{file} moved to PDF as {new_name}")
                pdf_count += 1
    print("Files organized successfully!")
except Exception as e:
    print("Error:", e)
    write_log(f"ERROR: {e}")