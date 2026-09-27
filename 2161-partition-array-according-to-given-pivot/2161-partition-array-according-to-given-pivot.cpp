class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        vector<int> a = {};
        vector<int>b = {};
        vector<int>c = {};

        for (int x:nums){
            if (x>pivot){
                c.push_back(x);
            }
            else if (x<pivot) {
                a.push_back(x);

            }
            else{

                b.push_back(x);
            }


            
        
        }
        a.insert(a.end(),b.begin(),b.end());
        a.insert(a.end(),c.begin(),c.end());
        return a;
    }
};