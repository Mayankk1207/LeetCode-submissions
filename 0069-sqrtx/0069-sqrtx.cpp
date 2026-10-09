class Solution {
public:
    int mySqrt(int x) {
        long long i = 0;
        long long j = x;
        long long m = 0;
        long long z = 0;

        while (i <= j) {
            m = i + (j-i) /2;
            z = m*m;
            if (z == x){
                return m;
            } 
            if (z<x){
                i = m + 1;
            } else{
                j = m  - 1;
            }
        }
        return j;
    }
};