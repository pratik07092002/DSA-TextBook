#include <bits/stdc++.h>
using namespace std;
bool ContainsDuplicateBruteForce(vector<int> &nums)
{
    for (int i = 0; i < nums.size(); i++)
    {
        for (int j = 0; j < nums.size(); j++)
        {
            if (i == j)
                continue;
            if (nums[i] == nums[j])
            {
                return true;
            }
        }
    }

    return false;
}

bool ContainsDuplicateHashing(vector<int> &nums)
{
    unordered_set<int> uSet;
    for (int i = 0; i < nums.size(); i++)
    {
        if (uSet.count(nums[i]))
        {
            return true;
        }
        uSet.insert(nums[i]);
    }

    return false;
}

int main(int argc, char const *argv[])
{
    vector<int> nums = {1, 2, 3, 0, 5};
    // Brute Force
 //   bool answer = ContainsDuplicateBruteForce(nums);
    // Hashing
    bool answer = ContainsDuplicateHashing(nums);

    cout << "Vector Contains Boolean " << answer;
    return 0;
}
