class Solution {
public:
    bool searchMatrix(vector<vector<int>>& mat, int val) {
        int row = mat.size(), cols = mat[0].size();
        int i = 0, j = (row*cols) -1;
        while(i<=j){
            int mid = i + (j-i)/2;
            int test = mat[mid/cols][mid%cols];
            if (test == val){
                return true;
            } 
            if (test < val){
                i = mid + 1;
            } else {
                j = mid - 1;
            }
        }
        return false;
    }
};