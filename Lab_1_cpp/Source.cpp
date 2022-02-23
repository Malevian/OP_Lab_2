#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include "functions.h"

using namespace std;

int main() {
	//Назви файлів
	string File_1 = "main_file.txt";
	string File_2 = "new_file_1.txt";
	string File_3 = "new_file_2.txt";
	//Підказки
	cout << "<Press Enter to enter the new line>\n";
	cout << "<Press Ctrl+S+Enter to end the text>\n";
	cout << "Enter the text:\n";

	vector<string> lines_message = create_lines(); //Рядки
	string text_message = create_text(lines_message); //Текст
	input_file(File_1, text_message); //Переніс у файл
	give(File_1, File_2, File_3);	  //Розподіляємо в інші файли
	//Виводимо на консоль вміст файлів
	cout << "\nMain file" << endl; output_file(File_1);
	cout << "\nFirst additional file" << endl; output_file(File_2);
	cout << "Second additional file" << endl; output_file(File_3);

	vector<string> sorted_lines = sort_file_lines(File_3); //Сортуємо файл із непарними рядками
	string new_text = create_text(sorted_lines);
	input_file(File_3, new_text);
	//Виводимо на консоль вміст зміненого файлу
	cout << "Second changed additional file" << endl; output_file(File_3);
}