// word_count.cpp
#include <algorithm>
#include <ios>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(void) {
	// ���α׷� ���� ���
	cout << "Enter all words, then EOF: "; // End of File
	vector<string> words;

	// �Է� �ޱ�
	string word;
	while (cin >> word) {
		words.push_back(word);
	}

	// { word: count } ���
	for (int i = 0; i < words.size(); i++) {
		cout << words[i] << ": " <<
			count(words.begin(), words.end(), words[i]) << endl;
	}

	// ������ ���
	cout << "Words: " << words.size();

	return 0;
}