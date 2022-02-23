#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

vector<string> create_lines() {
	char stop_button = 19; //Комбінація клавіш Ctrl+S
	//Записуємо введений текст у вектор
	vector<string>lines;
	string text = "";
	while (text[0] != stop_button) {
		getline(cin, text);
		lines.push_back(text);
	}
	lines.pop_back(); //Видаляємо елемент, яка створила комбінація клавіш
	return lines;
}
string create_text(vector<string>lines) {
	//Записуємо вектор в string
	string text = "";
	for (int i = 0; i < lines.size(); i++) {
		text += lines[i];
		if (i != lines.size() - 1) {
			text += "\n";
		}
	}
	return text;
}
void input_file(string File, string text) {
	// Призначаємо файлу текст
	ofstream file;
	file.open(File);
	file << text;
	file.close();
}
void give(string main_file, string first_file, string second_file) {
	ifstream main(main_file);
	ofstream first(first_file);
	ofstream second(second_file);
	string s;
	int counter = 1; //Лічильник
	while (!main.eof()) {
		getline(main, s);
		//Умови розподілення рядків
		if (counter % 2 == 0) {
			first << s << "\n";
		}
		else {
			second << s << "\n";
		}
		counter++;
	}
	second.close();
	first.close();
	main.close();
}
void output_file(string file_name) {
	ifstream file(file_name);
	string s;
	while (!file.eof()) {
		getline(file, s);
		cout << s << endl;
	}
	file.close();
}
vector<string> sort_file_lines(string second_file) {
	vector<string> lines;
	ifstream file(second_file);
	string s;
	while (!file.eof()) {
		getline(file, s);
		lines.push_back(s);
	}
	int size;
	cout << "Enter the amount of lines that you want to sort(less then " << lines.size()-1<< "): ";
	cin >> size;
	if (size <= lines.size()) {
		for (int i = 0; i < size; i++) {
			for (int j = i + 1; j < size; j++) {
				if ((toupper(lines[i][0]) > toupper(lines[j][0]) && lines[j] != "") || lines[i] == "") {
					s = lines[i];
					lines[i] = lines[j];
					lines[j] = s;
				}
				else if (toupper(lines[i][0]) == toupper(lines[j][0]) || lines[j][0] == ' ') {
					for (int k = 1; k < lines[i].size(); k++) {
						if (toupper(lines[i][k]) > toupper(lines[j][k]) || (lines[j][k] != ' ' && toupper(lines[j][k]) < toupper(lines[i][0]))) {
							break;
						}
					}
					s = lines[i];
					lines[i] = lines[j];
					lines[j] = s;
				}
			}
		}
	}
	return lines;
}