#include<bits/stdc++.h>
using namespace std;
vector<int> movingzeros(vector<int>& nums){
    int currentposition = 0;
    for (int i = 0; i <nums.size(); i++)
    {
    if(nums[i] != 0){
        nums[currentposition] = nums[i];
        currentposition++;
    }
    }

    while(currentposition < nums.size()){
        nums[currentposition] = 0;
        currentposition++;
    }
    return nums;
}
int main(int argc, char const *argv[])
{
    

    vector<int> nums = {1,3,0,5,0,0,1,4,5,78};
    vector<int> answer = movingzeros(nums);
    for(int num : answer){
        cout<<" "<<num;
    }
    return 0;
}
