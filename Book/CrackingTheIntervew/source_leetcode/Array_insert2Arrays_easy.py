class Solution:
    def intersection(self, nums1 : list, nums2 : list) -> list:
        lookup_mapper = dict()
        result = []
        for num in nums1:
            if num not in lookup_mapper:
                lookup_mapper[num] = True
        
        for num in nums2:
            if num in lookup_mapper and lookup_mapper[num] is True:
                result.append(num)
                lookup_mapper[num] = False
        return result


solution = Solution()
print(solution.intersection([1,2,3,4,5,6,7,8], [2,3,4,1,23,123,12,1,1]))
