#include <iostream>
using namespace std;
class User {
public:
string name;

User(string n) {
    name = n;
}

};

int main() {
User u("Alex");
cout << u.name;
}