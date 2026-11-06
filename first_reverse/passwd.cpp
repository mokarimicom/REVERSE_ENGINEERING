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