class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size()-1;
        int f = -1;
        int ls = -1;

        while(l<=r){
            int mid = l + (r-l)/2;

            if (nums[mid]== target ){
                f = mid;
                r = mid - 1;

            } else if (nums[mid] > target){
                r = mid -1;
            } else{
                l = mid + 1;
            }
        


        }
        l = 0;
        r = nums.size()-1;

        while(l<=r){
            int mid = l + (r-l)/2;

            if (nums[mid]== target ){
                ls = mid;
                l = mid + 1;

            } else if (nums[mid] > target){
                r = mid -1;
            } else{
                l = mid + 1;
            }
        


        }

        vector<int> res = {f,ls};
        return res;
        
    }
};