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