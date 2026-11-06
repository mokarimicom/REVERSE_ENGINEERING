#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int main() { ifstream file("sample.txt");

    if (!file.is_open()) {
        cout << "Could not open file" << endl;
        return 1;
    }

    string line;
    int lines = 0;
    int words = 0;

    while (getline(file, line)) {
        lines++;
        bool inWord = false;

        for (char ch : line) {
            if (ch == ' ' || ch == '\t') {
                inWord = false;
            } else if (!inWord) {
                words++;
                inWord = true;
            }
        }
    }

    cout << "Lines: " << lines << endl;
    cout << "Words: " << words << endl;
    file.close();
    return 0;

}