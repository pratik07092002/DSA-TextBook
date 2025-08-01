#include<bits/stdc++.h>
using namespace std;

#include <vector>
using namespace std;

vector<int> rearrangeArray(vector<int>& nums) {
    vector<int> positives, negatives;

    for (int num : nums) {
        if (num > 0) positives.push_back(num);
        else negatives.push_back(num);
    }

    vector<int> result;
    int i = 0;
    while (i < positives.size() && i < negatives.size()) {
        result.push_back(positives[i]);
        result.push_back(negatives[i]);
        i++;
    }

    return result;
}


int main(int argc, char const *argv[])
{
    vector<int> nums = {3,1,-2,-5,2,-4};
    vector<int> answer = rearrangeArray(nums);
    
    return 0;
}
