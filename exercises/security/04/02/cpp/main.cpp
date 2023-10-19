#include <iostream>
#include <string>

using namespace std;

string replaceSpecialCharacters(const string& input) {
    string output;
    for (char c : input) {
        if (c == '&') {
            output.append("&amp;");
        } else if (c == '<') {
            output.append("&lt;");
        } else if (c == '>') {
            output.append("&gt;");
        } else {
            output.push_back(c);
        }
    }
    return output;
}

int main() {
    string s;
    cout << "Enter string: " << endl;
    getline(cin, s);
    s = replaceSpecialCharacters(s);

    cout << s << endl;

    return 0;
}
