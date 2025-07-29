#include<bits/stdc++.h>
using namespace std;
int removeDuplicate(vector<int>& nums){
set<int> mySet;
    for (int i = 0; i < nums.size(); i++)
{
    mySet.insert(nums[i]);
}
return mySet.size();
}
int main(int argc, char const *argv[])
{
    vector<int> nums = {1,1,2,3,4};
    
    int answer = removeDuplicate(nums);
    cout<<answer;
    return 0;
}
