class Solution {
public:
    int rotatedDigits(int n) {
        int count = 0;
        for (int i = 1; i <= n; i++) {
            string s = to_string(i);
            bool possible = true, changed = false;
            for (char c : s) {
                if (c == '3' || c == '4' || c == '7') { possible = false; break; }
                if (c == '2' || c == '5' || c == '6' || c == '9') changed = true;
            }
            if (possible && changed) count++;
        }
        return count;
    }
};
