#include<bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    //Pre---compute
    map<int, int> mp; // we take long, long also but it depends on the size of array
    for (int i = 0; i < n; i++) {
        mp[arr[i]]++;
    }

    // Iterate in the given map
    for (auto it : mp) {
        cout << it.first << "->" << it.second << endl;
    }

    int q;
    cin >> q;
    while (q--) {
        int number;
        cin >> number;
        // Fetch
        cout << mp[number] << endl;
    }

    return 0;
}
