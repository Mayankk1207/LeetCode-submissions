class Solution {
public:
    int longestValidParentheses(string s) {
        
        stack<int> stc;
        stc.push(-1);
        int ans = 0;
        for(int i = 0; i < s.size(); i++){
            if (s[i] == ')'){
                stc.pop();
                if(stc.empty()){
                    stc.push(i);
                } else{
                    ans = max(ans,i-stc.top());
                }
            } else{
                stc.push(i);
            }

        }
        return ans;
    }
};