
1.  SOURCE CODE Save as file_analyzer.cpp:

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





2.  CREATE  : sample.txt 
4. Hello world C++ reverse engineering Ghidra helps analyze programs

3.  COMPILE AND RUN (LINUX) :
5. g++ -std=c++17 -O0 -g -fno-inline file_analyzer.cpp -o file_analyzer 
6. ./file_analyzer

5.  GHIDRA ANALYSIS

6.  Create a Non-Shared Project.

7.  Import file_analyzer.

8.  Open it and run Auto Analysis.

9.  In Symbol Tree, expand Functions and open main.

10. Read the Decompiler output and compare it with the Listing.

11. Use Window > Defined Strings to inspect embedded strings.

12. WHAT TO FIND

-   The filename “sample.txt”.
-   The message “Could not open file”.
-   The file-open operation.
-   The loop that reads lines.
-   The line and word counters (variable names may differ).
-   The output strings “Lines:” and “Words:”.
-   The branch taken when the file cannot be opened.
