

// 20-07-25

#include <bits/stdc++.h>
using namespace std;
// Brute Force
vector<int> twoSumBruteForce(vector<int> &nums, int target)
{
    for (int i = 0; i < nums.size(); i++)
    {
        for (int j = 0; j < nums.size(); j++)
        {
            if (i == j)
                continue;
            if (nums[i] + nums[j] == target)
            {
                return {i, j};
            }
        }
    }

    return {};
}

vector<int> twoSumHashing(vector<int> &nums, int target)
{
    unordered_map<int, int> uMap;
    for (int i = 0; i < nums.size(); i++)
    {
        int remaining = target - nums[i];
        if (uMap.find(remaining) != uMap.end())
        {
            return {uMap[remaining], i};
        }
        uMap[nums[i]] = i;
    }

    return {};
}
int main()
{
    vector<int> nums = {3, 7, 2, 15};
    int target = 9; 
    // Brute Force
    vector<int> result = twoSumBruteForce(nums, target);
    // Hashing
    vector<int> result = twoSumHashing(nums, target);

    for (int x : result)
        cout << " " << x;
    return 0;
}
