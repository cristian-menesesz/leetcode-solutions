int repeatedNTimes(int* nums, int numsSize) {
    
    int seen[10001] = {0};
    
    for (int i = 0; i < numsSize; i++) {
        if (seen[nums[i]]) {
            return nums[i];
        }
        seen[nums[i]] = 1;
    }
    
    return -1;
}