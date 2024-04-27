from typing import List

# def GetNext(block, nextls):
#     valid={}
#     for i in nextls:
        




class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        print("Starting...")

        def GetIndexAvailable(block):
            indexesav = []
            for i in range(len(grid[0])):
                if block!=i:
                    indexesav.append(i)

            print("blocked:", block, "indexes:",indexesav)
            return(indexesav)

        Posibilities = []
        for index,val in enumerate(grid[0]):
            a = GetIndexAvailable(index)
                    
            for i in a:

                Posibilities.append((index,i))
            

        print(Posibilities)
        actualpaths = []
        
        for i in range(len(Posibilities[0])):
            print(i)
            for x in grid[i]:
                print(x)
            
            

            
                
            
            
        




        # for index,val in enumerate(grid):
        #     print(grid[index])
        #     try:
        #         if grid[index+1]:
        #             for index2,val2 in enumerate(grid[index+1]):
        #                 if index2 != index:
        #                     print("posibilitie:", val[index],val2)
        #             print("There's a next row",grid[index+1])
        #     except:
        #         print("there's no another row")

        
            

        


                
                    

            
        return(grid)


x = Solution().minFallingPathSum([[1,3,2],[2,3,4]])
# y = Solution().minFallingPathSum([[1,3,2],[2,3,4], [6,7,5]])

