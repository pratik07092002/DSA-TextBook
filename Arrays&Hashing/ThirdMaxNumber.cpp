
// 22-07-2025
#include<bits/stdc++.h>
using namespace std;

int thirdMaxNumberBruteForce(vector<int>& nums){
 set<int> s(nums.begin(), nums.end()); 
        vector<int> uniqueNums(s.begin(), s.end());
        sort(uniqueNums.rbegin(), uniqueNums.rend());

if(uniqueNums.size() > 2){
    return uniqueNums[2];
}
return uniqueNums[0];
}
int main(int argc, char const *argv[])
{
    vector<int> nums = {1,4,9,5,6};
    int answer = thirdMaxNumberBruteForce(nums);
    cout<<answer;
    return 0;
}
