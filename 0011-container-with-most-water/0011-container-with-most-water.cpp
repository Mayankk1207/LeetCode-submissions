class Solution {
public:
    int maxArea(vector<int>& h) {
        int i = 0;
        int j = h.size()-1;
        int a = 0;

        while (i<j){
            a = max(a,min(h[i],h[j])*(j-i));
            if (h[i]>h[j]){
                j--;
            }
            else{
                i++;
            }
           
        }
        return a;
    }
};