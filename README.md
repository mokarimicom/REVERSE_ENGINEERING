1.  SOURCE CODE Save as file.cpp:

#include <iostream>
using namespace std;

int main() { int password;

    cout << "Enter password: ";
    cin >> password;

    if (password == 1234) {
        cout << "Correct password!\n";
    } else {
        cout << "Wrong password!\n";
    }

    return 0;

}



2.  COMPILE AND RUN (LINUX) Install a compiler if needed: sudo apt
    update sudo apt install g++

Compile: g++ -O0 -g main.cpp -o program

Run: 
./program

Try 1234, then try 1111.

3.  INSPECT THE EXECUTABLE View file information: 
4. file program

Find readable strings: 
strings program

Disassemble: 
objdump -d -M intel program

4.  ANALYZE WITH GHIDRA

5.  Start Ghidra and create a Non-Shared Project.

6.  Choose File > Import File and select program.

7.  Open the imported executable.

8.  Accept the analysis prompt and click Analyze.

9.  In Symbol Tree, open Functions and select main.

10. Look at both the Listing (assembly) and Decompiler (C-like code).

11. WHAT TO FIND [ ] The number 1234 (hexadecimal: 0x4D2). [ ] The
    comparison that checks the entered password. [ ] The strings
    “Correct password!” and “Wrong password!”. [ ] The conditional
    branch that selects success or failure.

