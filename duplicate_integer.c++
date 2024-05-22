class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> unique_values;
        for (int num:nums){
            if (unique_values.count(num)){
                return true;
            }
            else {
                unique_values.insert(num);
            }
        }
        return false;
    }
};
