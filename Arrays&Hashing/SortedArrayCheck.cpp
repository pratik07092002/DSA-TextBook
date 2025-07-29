#include<bits/stdc++.h>
using namespace std;

bool isArraySorted(vector<int>& nums){
    int ele = 0;
for (int i = 1; i < nums.size(); i++)
{
if(nums[i] < nums[i-1]){
    return false;
}
}
return true;
}

int main(int argc, char const *argv[])
{
    vector<int> nums = {1,2,20,4,5};
    bool isSorted = isArraySorted(nums);
    cout<<isSorted;
    return 0;
}
