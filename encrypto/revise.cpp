#include <algorithm>
#include <iostream>
#include <unistd.h>
#include <fstream>
#include <cstring>
#include <vector>
#include <limits>
#include <cstdio>
#include <string>
#include <ctime>

using namespace std;

string script_key_gen(string main_key){
	int key_len = main_key.length();
	string key_array_string;

	for (int i = 0; i < key_len; ++i){
		key_array_string += main_key[i];
		if (i != key_len - 1){
			key_array_string += "-";
		}
	}
	key_array_string += "-";
	for (int i = key_len - 1; i >= 0; --i)
	{
		key_array_string += main_key[i];
	}
	return key_array_string;
}

string key_gen() {
    string charSet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    string randomString;
    srand(time(NULL));
    for(int i = 0; i < 5; i++) {
        int randomCharIndex = rand() % charSet.size();
        randomString += charSet[randomCharIndex];
    }
    return randomString;
}

string script_key_gen_auth() {
    string charSet = "acegikmoqsuwyACEGIKMOQSUWY02468";
    string randomString;
    srand(time(NULL));
    for(int i = 0; i < 6; i++) {
        int randomCharIndex = rand() % charSet.size();
        randomString += charSet[randomCharIndex];
    }
    return randomString;
}

string handshake_code_gen() {
    string charSet = "2468";
    string randomString;
    srand(time(NULL));
    for(int i = 0; i < 4; i++) {
        int randomCharIndex = rand() % charSet.size();
        randomString += charSet[randomCharIndex];
    }
    return randomString;
}

bool username(string id)
{
	string inp_id;
	for (int i = 1; i <= 5; ++i)
	{
		cout << "Enter Username: ";
		cin >> inp_id;
		cin.ignore(numeric_limits<streamsize>::max(), '\n');
		if (inp_id == id){
			return true;
		}
		else{
			cout << inp_id << "\nTRY AGAIN!!\n" << endl;
		}
	}
	return false;
}

bool password(int pass)
{
	int inp_psk;
	for (int i = 1; i <= 5; ++i)
    {
        cout << "Enter Password: ";
        cin >> inp_psk;
        if (cin.fail() || cin.peek() != '\n') {
    	cin.clear();
    	cin.ignore(numeric_limits<streamsize>::max(), '\n');
    	cout << "Invalid input. Please enter an integer.\n" << endl;
    	continue;
		}
        if (inp_psk == pass){
            return true;
        }
        else if (typeid(inp_psk) != typeid(pass) || inp_psk != pass){
            cout << inp_psk << "\nTRY AGAIN!!\n" << endl;
        }
    }
    return false;
}

string handshake_init(){
	string code = handshake_code_gen();
	string half = "handshake-";

	string full;
	full = half + code;
	return full;
}

bool handshake_file_write(bool mem_val) {
	ofstream outfile("C:\\Users\\willi\\LocalMem\\sharmem");
	if (outfile.is_open()){
		outfile << mem_val;
		cout << "\tHandshake Written" << endl;
		outfile.close();
		return true;
	} else if (outfile.fail()) {
		cout << "Unable to create handshake file" << endl;
		return false;
	}
	return false;
}


string handshake(){
    char handshake_buffer[555];
    string output;
    string handshake_code = handshake_init();

    FILE *fp = popen(("python main.py " + handshake_code).c_str(), "r");
    if (fp == NULL) {
        cout << "File doesnt contain handshake exiting now... \n" << endl;
        sleep(5);
        return "false";
    }

    FILE *outFile = fopen("output.txt", "w");

    while (fgets(handshake_buffer, sizeof(handshake_buffer), fp) != NULL) {
        output += handshake_buffer;
        fprintf(outFile, "%s", handshake_buffer);
    }

    fclose(fp);
    fclose(outFile);
    remove("output.txt");
    return output;
}

string trim(const std::string& str){
    auto first = std::find_if_not(str.begin(), str.end(), (int(*)(int))std::isspace);
    auto last = std::find_if_not(str.rbegin(), str.rend(), (int(*)(int))std::isspace).base();
    return (first == last ? "" : std::string(first, last));
}

bool handshake_rx_test(string handshake_py) {
    size_t pos = handshake_py.find("-");
    string first = handshake_py.substr(0, pos);

    string second = handshake_py.substr(pos + 1);
    size_t second_pos = second.find("-");
    string Second = second.substr(0, second_pos);
    string py_hand_code = second.substr(second_pos + 1);

    bool mem_write;
    bool status;
    string reversed_second;
    for (int i = Second.length() - 1; i >= 0; --i) {
        reversed_second += Second[i];
    }
    string word = "rxtron";
    reversed_second = trim(reversed_second);
   	status = (reversed_second == "rxtron");
   	if (status == true or status == 1){
   		mem_write = handshake_file_write(status);
   	}else{
   		cout << "Handshake Failed\nExiting now..." << endl;
   		sleep(2);
   		exit(1);
   	}

   	vector<int> arr;
   	for (int i = 0; i < py_hand_code.length(); i++){
   		arr.push_back(py_hand_code[i] - '0');
   	}
   	int n1 = arr[0];
   	int n2 = arr[1];
   	int n3 = arr[2];
   	int n4 = arr[3];

   	int p1 = n1 + n3;
   	int p2 = n2 + n4;

   	bool test1 = (p2 + p1) % 2 == 0;
   	bool test2 = p2 > p1;

   	if (mem_write == true && test1 == true && test2 == true){
   		return status;
   	}else {
   		return false;
   	}
}

int loader(string name, int psk){
	bool hand;
	bool psk_auth;
	char buffer[456];
	string script_ver_key;
	string hashed_key;
	string main_key;
	string command;
	string key;
	string ho;

	ho = handshake();
	hand = handshake_rx_test(ho);
	if (hand == false || hand == 0){
		cout << "\tHandshake Failed\nRetry Again\nExiting Now......!\n" << endl;
		sleep(5);
		exit(0);
	}
	else if (hand == true || hand == 1){
		cout << "\tHandshake Verified\n" << endl;
		sleep(2);
	} else {
		exit(0);
	}
	bool id_auth = username(name);
	if (id_auth == true){
		psk_auth = password(psk);
		if (psk_auth == true){

			key = script_key_gen_auth();
			main_key = key_gen();

			script_ver_key = script_key_gen(main_key);
			sprintf(buffer, "start cmd /c python main.py %s %s", key.c_str(), script_ver_key.c_str());
			command = buffer;
			system(command.c_str());

			cout << "KEY: " << key << endl;
			sleep(5);
			remove("C:\\Users\\willi\\LocalMem\\sharmem");
			sleep(5);
			return 0;
		}
	}
	else {
		return 0;
	}
	return 0;
}


int main()
{
	const string name = "Naveen";
	const int psk = 123;
	loader(name, psk);
	return 0;
}