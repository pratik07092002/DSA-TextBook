#include<bits/stdc++.h>
using namespace std;
int numbersAppearingOnceHashing(vector<int> nums){
    int answer = 0;
        unordered_map<int,int> umap;
    for (int i = 0; i < nums.size(); i++)
    {
        umap[nums[i]]++;

    }
for( const auto& pair : umap){
    if(pair.second == 1){
        return pair.first;
    }
}
   return -1;
}
int optimalSolutionXor(vector<int>& nums){
        int answer = 0;
    for (int num : nums) {
        answer ^= num;
    }
    return answer;
}
int main(int argc, char const *argv[])
{
    vector<int> nums = {1,2,3,4,5,6};
    int answer = numbersAppearingOnceHashing(nums);
    cout<<answer;

    
    return 0;
}
