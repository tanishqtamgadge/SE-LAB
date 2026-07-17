#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

// Define a structure for personal records
struct PersonalRecord {
    string name;
    string dob;  // Date of Birth
    string telephone;

    // Overload the output operator for easy display
    friend ostream& operator<<(ostream& os, const PersonalRecord& record) {
        os << "Name: " << record.name 
           << ", DOB: " << record.dob 
           << ", Telephone: " << record.telephone;
        return os;
    }
};

int main() {
    vector<PersonalRecord> records = {
        {"Alice Johnson", "1990-01-15", "1234567890"},
        {"Bob Smith", "1985-05-20", "9876543210"},
        {"Charlie Brown", "1992-08-30", "5555555555"}
    };

    // Display original records
    cout << "Original Records:\n";
    for (const auto& record : records) {
        cout << record << "\n";
    }

    // Sort records by name
    sort(records.begin(), records.end(), [](const PersonalRecord& a, const PersonalRecord& b) {
        return a.name < b.name;
    });

    // Display sorted records
    cout << "\nSorted Records by Name:\n";
    for (const auto& record : records) {
        cout << record << "\n";
    }

    // Search for a record by name
    string searchName;
    cout << "\nEnter the name to search: ";
    getline(cin, searchName);

    auto it = find_if(records.begin(), records.end(), [&](const PersonalRecord& record) {
        return record.name == searchName;
    });

    if (it != records.end()) {
        cout << "Record found:\n" << *it << "\n";
    } else {
        cout << "Record not found.\n";
    }

    return 0;
}
