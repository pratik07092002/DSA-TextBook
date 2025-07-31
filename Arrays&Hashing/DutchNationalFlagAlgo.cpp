#include <bits/stdc++.h>
using namespace std;
vector<int> DutchNationalFlag(vector<int>& nums)
{
    int mid = 0;
    int low = 0;
    int high = nums.size() - 1;
    while (mid <= high)
    {
        if (nums[mid] == 0)
        {
            swap(nums[mid], nums[low]);
            mid++;
            low++;
        }
        else if (nums[mid] == 1)
        {
            mid++;
        }
        else
        {
            swap(nums[mid], nums[high]);

        
                high--;
            
        }
    }
    return nums;
}


int main(int argc, char const *argv[])
{
    vector<int> nums = {1, 2, 2, 0, 0, 1};
    vector<int> answer = DutchNationalFlag(nums);
    for(int num : nums){
        cout<<num<< " ";
    }
    return 0;
}
