class Solution(object):

    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        while True:
            extended = False
            counter = 0
            temp = []
            for i in range(len(nestedList)):
                if (type(nestedList[i]) == list):
                    temp.extend(nestedList[i])
                    extended = True
                else:
                    temp.append(nestedList[i])
            if (not(extended)):
                return nestedList
            nestedList = temp
