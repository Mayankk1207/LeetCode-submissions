class Solution {
public:
    bool isValid(string s) {
        stack<char> stc;
        for (char x: s){
            if(x == '[' || x == '(' || x == '{'){
                stc.push(x);
            } else{

                if (stc.empty()){
                    return false;
                }  
                if (x == ']' && stc.top() == '['){
                    stc.pop();
                } else if (x == ')' && stc.top() == '('){
                    stc.pop();
                } else if (x == '}' && stc.top() == '{'){
                    stc.pop();
                } else{
                    return false;
                }


            }
            
        }
        return stc.empty();
    }
};