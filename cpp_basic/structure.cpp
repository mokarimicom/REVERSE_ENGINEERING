#include <iostream>
using namespace std;

struct User {
string name;
int age;
};

int main() {
User hacker;

hacker.name = "Alex";
hacker.age = 25;

cout << hacker.name;

return 0;

}