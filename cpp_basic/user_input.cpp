#include <iostream>
using namespace std;

int main() {
string username;

cout << "Enter username: ";
// cin >> username;
getline(cin, username);//For full-line input

cout << "Welcome " << username;

return 0;

}