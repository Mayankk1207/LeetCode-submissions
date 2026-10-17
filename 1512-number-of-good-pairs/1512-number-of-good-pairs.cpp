class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int ans = 0;
        unordered_map<int,int> seen;
        for (int x: nums){
            ans += seen[x];
            seen[x] ++;
        }
        
        return ans;
    }
};