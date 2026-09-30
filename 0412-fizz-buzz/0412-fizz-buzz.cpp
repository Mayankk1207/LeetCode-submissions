class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> res;
        string a = "Fizz";
        string b = "Buzz";
        string c = "FizzBuzz";

        for (int i = 1; i <= n; i++){

            if (i%3 == 0 && i%5==0){
                res.push_back(c);
            }
            else if (i%3 == 0){
                res.push_back(a);

            } else if ( i%5==0){
                res.push_back(b);

            } else {
                res.push_back(to_string(i));
            }



        }
        return res;
    }
};