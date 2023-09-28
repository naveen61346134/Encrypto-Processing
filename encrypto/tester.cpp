#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

bool verifyNumber() {
	int number;
	srand(time(NULL));
	int randomNumber = rand() % 9000 + 1000;
	number = randomNumber;
    int pair1 = (number / 1000) + ((number / 10) % 10);
    int pair2 = ((number / 100) % 10) + (number % 10);
    
    if (pair1 % 2 != 0 && pair2 % 2 != 0) {
        pair1++;
    }
    
    if (pair1 > pair2) {
        int temp = pair1;
        pair1 = pair2;
        pair2 = temp;
    }
    
    int difference = pair2 - pair1;
    if (difference % 2 != 0) {
        difference++;
    }
    pair1 += difference / 2;
    pair2 -= difference / 2;
    if (pair1 % 2 != 0 || pair2 % 2 != 0) {
        return false;
    }
    if ((pair2 - pair1) % 2 != 0) {
        return false;
        verifyNumber();
    }
    return true;
}

int main() {
    if (verifyNumber()) {
        cout << "Number is valid." << endl;
    } else {
        cout << "Number is invalid." << endl;
        verifyNumber();
    }
    return 0;
}
