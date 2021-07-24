"""
131. The Skyline Problem
中文
English

Given N buildings in a x-axis，each building is a rectangle and can be represented by a triple (start, end, height)，where start is the start position on x-axis, end is the end position on x-axis and height is the height of the building. Buildings may overlap if you see them from far away，find the outline of them。

An outline can be represented by a triple, (start, end, height), where start is the start position on x-axis of the outline, end is the end position on x-axis and height is the height of the outline.

Building Outline
Example

Example 1

Input:
[
    [1, 3, 3],
    [2, 4, 4],
    [5, 6, 1]
]
Output:
[
    [1, 2, 3],
    [2, 4, 4],
    [5, 6, 1]
]
Explanation:
The buildings are look like this in the picture. The yellow part is buildings.

图片

Example 2

Input:
[
    [1, 4, 3],
    [6, 9, 5]
]
Output:
[
    [1, 4, 3],
    [6, 9, 5]
]
Explanation:
The buildings are look like this in the picture. The yellow part is buildings.

图片
Notice

Please merge the adjacent outlines if they have the same height and make sure different outlines cant overlap on x-axis.
"""

class Solution:
    """
    @param buildings: A list of lists of integers
    @return: Find the outline of those buildings
    """
    def buildingOutline(self, buildings):
        buildings.sort()
        i = 0
        while i < len(buildings) - 1:
            current = buildings[i]
            next_building = buildings[i+1]
            popped = False
            if current[1] >= next_building[0]:
                if current[2] > next_building[2]:
                    next_building[0] = current[1]
                    if next_building[1] <= next_building[0]:
                        buildings.pop(i+1)
                        popped = True
                else:
                    current[1] = next_building[0]
                    if current[0] >= current[1]:
                        buildings.pop(i)
                        popped = True
            if not popped:
                i += 1
        return buildings

if __name__ == "__main__":
    s = Solution()
    assert(s.buildingOutline([[1, 20, 3]]) == [[1, 20, 3]])
    print(s.buildingOutline([
    [1, 3, 3],
    [2, 4, 4],
    [5, 6, 1]]))
    assert(s.buildingOutline([
    [1, 3, 3],
    [2, 4, 4],
    [5, 6, 1]]
)== [
    [1, 2, 3],
    [2, 4, 4],
    [5, 6, 1]
])
    assert(s.buildingOutline([
    [1, 4, 3],
    [6, 9, 5]])
 == [
    [1, 4, 3],
    [6, 9, 5]
])