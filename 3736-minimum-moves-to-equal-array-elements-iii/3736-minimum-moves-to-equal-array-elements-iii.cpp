class Solution {
public:
    int minMoves(vector<int>& nums) {
        
        int ans = 0;
        int maxm = *max_element(nums.begin(),nums.end());
        for (int x: nums){
            ans += maxm - x;
        }

        return ans;
    }
};