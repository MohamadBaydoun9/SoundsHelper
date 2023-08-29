import os

def generate_slide_text(folder_path):

    files = os.listdir(folder_path)
    output_file="Result.txt"
    current_slide=1
    file = open(output_file, "w")
    for file_name in sorted(files):
        if file_name.startswith("Slide"):
            slide_number = file_name.split("_")[0]
            slide_number = slide_number.split(" ")[1]  
            if slide_number != current_slide:
               
                file.write(f"**Slide {slide_number}**\n")
                current_slide=slide_number
            file.write("     "+file_name.replace(" ","_")+"\n")

    print(f"Slide-text mapping has been saved to {output_file}")
    file.close()  

def extractor(datafile,foldersfile,preword):
    # Read the data file and create a dictionary of file names and links
    data_file_path = datafile

    file_data = {}
    current_file = None

    with open(data_file_path, 'r') as f:
        counter=0
        for line in f:
            line = line.strip()
            if counter %2==0:
                current_file = line.replace(preword,"")
            else :
                file_data[current_file] = line
            counter=counter+1

    # Read the file with the structure and extract links
    structure_file_path = foldersfile
    output_lines = []

    with open(structure_file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line.startswith("**"):
                file_name = line
                link=file_data.get(file_name)
                output_lines.append(f"\t {file_name} : {link}")
            else:
                output_lines.append(line)


    # Write the links to the output file
    output_file_path = 'Result.txt'

    with open(output_file_path, 'w') as f:
        f.write('\n'.join(output_lines))

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    datafile=input("Enter the data file path: ")
    preword=input("Enter if there any preword for file names: ")
    generate_slide_text(folder_path)
    extractor(datafile,"Result.txt",preword)

    


