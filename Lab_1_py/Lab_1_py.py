import functions

main_file = "main_file.txt"
first_file = "new_file_1.txt"
second_file = "new_file_2.txt"

array = functions.create_array()
text = functions.create_text(array)
functions.ToFile(main_file, text)
functions.division(main_file, first_file, second_file)
print("\nГоловний файл")
functions.out_file(main_file)
print("\nПерший додатковий файл")
functions.out_file(first_file)
print("\nДругий додатковий файл")
functions.out_file(second_file)

Lines = functions.sort_array(second_file)
To_Text = functions.create_text_for_sorted_file(Lines)
functions.ToFile(second_file, To_Text)
print("\nДругий змінений додатковий файл")
functions.out_file(second_file)