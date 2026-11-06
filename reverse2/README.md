1.  SOURCE CODE Save as calculator.cpp:

#include <iostream>
using namespace std;

int add(int a, int b) { return a + b; }

int subtract(int a, int b) { return a - b; }

int main() { int choice, x, y;

    cout << "1 = Add, 2 = Subtract\n";
    cout << "Choice: ";
    cin >> choice;

    cout << "Enter two numbers: ";
    cin >> x >> y;

    if (choice == 1) {
        cout << "Result: " << add(x, y) << endl;
    } else if (choice == 2) {
        cout << "Result: " << subtract(x, y) << endl;
    } else {
        cout << "Invalid choice" << endl;
    }

    return 0;

}


2.  COMPILE AND RUN (LINUX) Compile: 
4. g++ -std=c++17 -O0 -g -fno-inline calculator.cpp -o calculator

Run: 
./calculator

3.  SAMPLE RUNS

Sample A — addition: $ 
./calculator 
1 = Add, 2 = Subtract 
Choice: 1
Enter two numbers: 8 3 Result: 11

Sample B — subtraction: $ 
./calculator 
1 = Add, 2 = Subtract 
Choice: 2
Enter two numbers: 8 3 Result: 5

Sample C — invalid choice: $ 
./calculator 1 = Add, 2 = Subtract 
Choice:9 
Enter two numbers: 8 3 Invalid choice

 = GHIDRA STEPS

 =Open Ghidra and create a new Non-Shared Project.

 = Import the calculator executable.

 = Open it and run Auto Analysis.
(you must on the listing mode click Right ⇒ disassample)
  =In Symbol Tree, inspect main click

 =Select each function and view its Decompiler output.(windows ⇒ decompile)

 =Compare the pseudocode with the source code above.
 ==================================================
 1-extract strings ==>
 on window ==> definded string ==> search ==> Result

<<<<<<< HEAD

 
 extract function ==>
=======
 
 2-extract function ==>
>>>>>>> a1868eb (file_analyzer project added .)
 1- open Symbol tree 
 2- expand function
 3- look for : 
        main    
        add
        subtract

duble click a function to see its decompiled code .
