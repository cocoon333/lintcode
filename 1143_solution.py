"""
1143. Minimum Index Sum of Two Lists
中文
English

Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.
Example

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".

Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

Notice

1.The length of both lists will be in the range of [1, 1000].
2.The length of strings in both lists will be in the range of [1, 30].
3.The index is starting from 0 to the list length minus 1.
4.No duplicates in both lists.
"""

class Solution:
    """
    @param list1: a list of strings
    @param list2: a list of strings
    @return: the common interest with the least list index sum
    """
    def findRestaurant(self, list1, list2):
        minimum = 9999999
        res = []
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    if i + j < minimum:
                        minimum = i + j
                        res = [list1[i]]
                    elif i + j == minimum:
                        res.append(list1[i])
        return res

if __name__ == "__main__":
    s = Solution()
    assert(s.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]) == ['Shogun'])
    assert(s.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["KFC", "Shogun", "Burger King"]) == ['Shogun'])
