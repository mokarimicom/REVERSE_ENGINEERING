#include <iostream>
using namespace std;

int main() {
int score = 85;

if (score >= 90) {
cout << "Excellent";
}
else if (score >= 70) {
cout << "Good";
}
else {
cout << "Try again";
}
return 0;
}