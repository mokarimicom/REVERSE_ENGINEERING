#include <iostream>
using namespace std;
class Hacker {
public:
string name;

void introduce() {
    cout << "I am " << name;
}

};

int main() {
Hacker h;

h.name = "Alex";
h.introduce();

return 0;

}