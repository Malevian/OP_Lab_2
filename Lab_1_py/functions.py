def create_array():
    print("Щоб перейти на наступний рядок, нажміть Enter.\nЩоб закінчити текст нажміть Ctrl+S+Enter\nВведіть текст:")
    lines = []
    line = ""
    stop_button = chr(19)
    while line != stop_button:
        line = input()
        lines.append(line)
    lines.pop(-1)
    return lines

def create_text(lines):
    text = ""
    for i in range(len(lines)):
        text += lines[i]
        if i!=len(lines)-1:
            text+='\n'
    return text

def ToFile(file_name, text):
    File = open(file_name, "w")
    File.write(text)
    File.close()

def division(main_file, add_file_1, add_file_2):
    Main = open(main_file,"r")
    first_add = open(add_file_1, "w")
    second_add = open(add_file_2, "w")
    counter = 1
    lines = Main.readlines()
    for i in lines:
        if counter%2==0:
            first_add.write(i)
        else:
            second_add.write(i)
        counter += 1
    second_add.close()
    first_add.close()
    Main.close()

def out_file(File_work):
    File = open(File_work, "r")
    print(File.read())
    File.close()
    
def sort_array(file_work):
    File = open(file_work, "r")
    Lines = File.readlines()
    s = ""
    print("Введіть кількість рядків, які потрібно сортувати(Не більше",len(Lines),"): ")
    size = int(input())
    if size <= len(Lines):
        for i in range(size):
            for j in range(i+1, size):
                if (Lines[i][0].upper() > Lines[j][0].upper() and Lines[j] != "") or Lines[i] == "":
                    s = Lines[i]
                    Lines[i] = Lines[j]
                    Lines[j] = s
                elif Lines[i][0].upper() == Lines[j][0].upper() or Lines[j][0] == ' ':
                    for k in range(1, len(Lines[i])):
                        if Lines[i][k].upper() > Lines[j][k].upper() or (Lines[j][k] != ' ' and Lines[j][k].upper() < Lines[i][0].upper()):
                            break
                    s = Lines[i]
                    Lines[i] = Lines[j]
                    Lines[j] = s
    File.close()
    return Lines

def create_text_for_sorted_file(lines):
    text = ""
    for i in range(len(lines)):
        text += lines[i]
    return text