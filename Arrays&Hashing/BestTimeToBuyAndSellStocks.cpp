// 21-07-2025

#include <bits/stdc++.h>
using namespace std;
int maxProfitBruteForce(vector<int>& nums)
{
    int maxDay = 0;
    int maxValue = 0;
    int n = nums.size();

    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            int profit = nums[j] - nums[i];
            if(profit > maxValue){
  maxValue = profit;
            }
          
        }
    }

    return maxValue;
}

int maxProfitOptimal(vector<int>& nums)
{
    int minPrice = INT_MAX; 
        int maxProfit = 0;      

        for (int price : nums) {
            if (price < minPrice) {
                minPrice = price; 
            } else {
                int profit = price - minPrice; 
                maxProfit = max(maxProfit, profit); 
            }
        }

        return maxProfit;
}
int main(int argc, char const *argv[])
{
    vector<int> nums = {1, 2, 3, 4, 5};
    int answer = maxProfitBruteForce(nums);
    cout<<answer;
    return 0;
}
