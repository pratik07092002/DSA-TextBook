
// 20-07-25
#include <bits/stdc++.h>
using namespace std;

int majorityElementBruteForce(vector<int> &nums)
{
    int n = nums.size();
    for (int i = 0; i < n; i++)
    {
        int answer = 0;

        for (int j = 0; j < n; j++)
        {
            if (nums[i] == nums[j])
            {
                answer++;
            }
            if (answer > (n / 2))
            {
                return nums[i];
            }
        }
    }

    return -1;
}

int majorityElementOptimal(vector<int> &nums)
{
    int count = 0;
    int element = -1;
 for(int num : nums){
if(count == 0){
    element = num;
}
count += (num == element) ? 1 : -1;
 }

    return element;
}
int main(int argc, char const *argv[])
{
    vector<int> nums = {3, 1, 3};
    // Brute Force
  //  int answer = majorityElementBruteForce(nums);
    // Optimal 
    int answer = majorityElementOptimal(nums);
cout<<answer;
    return 0;
}
