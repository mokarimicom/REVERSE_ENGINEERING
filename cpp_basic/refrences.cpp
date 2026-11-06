
#include <iostream>
using namespace std;

int main() {
int number = 50;

int& reference = number;

reference = 100;

cout << number;
return 0;
}
// A reference is another name for an existing variable.