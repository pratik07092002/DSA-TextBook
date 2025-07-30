#include<bits/stdc++.h>
using namespace std;

int ConsecutiveOnes(vector<int>& nums){
   int total = 0;
   int maxv = 0;
   for (int i = 1; i < nums.size(); i++)
   {
    if(nums[i] == 1 ){
total++;
    }else{
total = 0;
    }
    maxv = max(total,maxv);
   }
   
    return maxv;
}
int main(int argc, char const *argv[])
{
    vector<int> nums = {1,1,0,0,1,1,1,1,1,0};
    int answer = ConsecutiveOnes(nums);
    cout<<answer;



    return 0;
}
