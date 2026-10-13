class Solution {
public:
    int minEatingSpeed(vector<int>& p, int h) {
        int i = 1, j = *max_element(p.begin(),p.end());
        while(i<=j){
            long long hr = 0;
            int mid = i + (j-i)/2;
            for (int x : p){
                hr = hr + ceil(static_cast<double>(x)/mid);
            }
            if (hr <= h){
                j = mid-1;
            } else {
                i = mid +1;
            }
        }
        return i ;
    }
};