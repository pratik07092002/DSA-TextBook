#include<bits/stdc++.h>
using namespace std;
vector<int> RotateArrayBruteForce(vector<int>& nums, int k){
    vector<int> temp;
    for (int i = 0; i < k; i++)
    {
        temp.push_back(nums[i]);
    }
           nums.erase(nums.begin(), nums.begin()  +k);

nums.insert(nums.end(), temp.begin(), temp.end());
return nums;

}

// Optimal Soltion for Right Rotation for left Rotation Process will be exactly reverse 
void reverse(vector<int>& nums, int start, int end) {
    while (start < end) {
        swap(nums[start++], nums[end--]);
    }
}

vector<int> RotateArrayByKOptimal(vector<int> nums , int k){
   int n = nums.size();
    k = k % n;
    reverse(nums, 0, n - 1);

    reverse(nums, k, n - 1);
        reverse(nums, 0, k - 1);

return nums;
}
int main(int argc, char const *argv[])
{
    vector<int> nums = {1,2,3,4,5,6,7};
    vector<int> answer = RotateArrayByKOptimal(nums,3);
    for(int num : answer){
        cout<< " "<<num;
    }
    return 0;
}
