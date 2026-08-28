class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> record;
        record.reserve(nums.size());

        for (int x : nums) {
            if (record.contains(x)) {
                return true;
            }
            record.insert(x);
        }

        return false;
    }
};