#include<bits/stdc++.h>
using namespace std;

int maxSubArray(vector<int>& nums){
    int maxSum =nums[0];
    int currentSum = nums[0];
  
    for (int i = 0; i < nums.size(); i++)
    {
      currentSum = max(nums[i], currentSum + nums[i]);
        maxSum = max(maxSum, currentSum);
    }
     return maxSum;
}

int main(int argc, char const *argv[])
{
    vector<int> nums = {-2,1,-3,4,-1,2,1,-5,4};
    int answer  = maxSubArray(nums);
  cout<<answer;
    return 0;
}
