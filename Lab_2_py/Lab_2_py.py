import functions

#Ім'я бінарних файлів
BinaryFileName = "BinaryFile.txt"
newBinaryFile = "newBinaryFile.txt"

#Список студентів
list_of_students = functions.create_info()
print("\nAll of the students:")
functions.output_students(list_of_students)

#Передача інформації в бінарний файл
AmountOfStudents = functions.CreateBinaryFile(BinaryFileName, list_of_students)

#Розшифровуємо інформацію
Readable = functions.FromByteToReadable(BinaryFileName)
print("\nAll of the students 2:")
functions.output_students(Readable)

#Студенти із найнижчими балами
Lowest = functions.LowLevelStudents(Readable)
print("Lowest mark students:")
functions.output_students(Lowest)

#Відсортований список студентів 4-го курсу
newList = functions.Identify(Lowest)
print("4-th grade students:")
functions.output_students(newList)
Stud = functions.CreateBinaryFile(newBinaryFile, newList)