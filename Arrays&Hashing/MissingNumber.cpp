#include <bits/stdc++.h>
using namespace std;
int missingNumberBruteForce(vector<int>& nums){
int n = nums.size();
int m = 0;
for (int i = 0; i < n; i++)
{
    for (int j = 0; j < n - i - 1; j++)
    {
        if(nums[j] > nums[j+1]){
            swap(nums[j],nums[j+1]);
        }
    }  
}
  for (int i = 0; i < n; i++)
    {
        if(nums[i]+1 != nums[i+1]){
            m = nums[i]+1;
        break;
        }
    }


    return m;

}

int missingNumber(vector<int>& nums){
    int n = nums.size();
    int sum = n*(n+1)/2;
    int total = 0;
    for (int i = 0; i < n; i++)
    {
        total = total + nums[i];
    }
    int answer =  sum - total;
    return answer;
}
int main(int argc, char const *argv[])
{
    vector<int> nums = {1,0,3};
    int number = missingNumberBruteForce(nums);
    cout<<"Missing "<< number;
    return 0;
}
