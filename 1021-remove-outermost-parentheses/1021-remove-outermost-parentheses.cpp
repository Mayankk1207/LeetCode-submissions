class Solution {
public:
    string removeOuterParentheses(string s) {
        string res;
        int d = 0;
        for(char x:s){
            if (x == '('){
                if (d>0){
                    res += '(';
                }
                d++;
            } else{
                d--;
                if (d>0){
                    res += ')';
                }
            }
        }
        return res;

        
    }
};