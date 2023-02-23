# class HeapSort:
#     def __init__(self, arr) -> None:
#         self.buildHeap(arr)

#     def buildHeap(self,arr):
#         self.heap = arr
#         for index in range(self.parent(len(self.heap) - 1), -1, -1):
#             self.heapifyDown(index)

#     def heapifyDown(self,currIdx):
#         endIdx = len(self.heap) - 1
#         leftIdx = self.lchild(currIdx)
#         while leftIdx <= endIdx:
#             rightIdx = self.rchild(currIdx)
#             if rightIdx <= endIdx and self.heap[rightIdx] > self.heap[leftIdx] :
#                 idxToChg = rightIdx
#             else:
#                 idxToChg = leftIdx
            
#             if self.heap[idxToChg] > self.heap[currIdx]:
#                 self.swap(idxToChg,currIdx)
#                 currIdx = idxToChg
#                 leftIdx = self.lchild(currIdx)
#             else:
#                 return

#     def heapifyUp(self):
#         pass

#     def parent(self, curr):
#         return (curr - 1) // 2
    
#     def lchild(self,curr):
#         return (2 * curr) + 1

#     def rchild(self,curr):
#         return (2 * curr) + 2
    
#     def swap(self,first,second):
#         self.heap[first], self.heap[second] = self.heap[second], self.heap[first]
#         return
    
#     def display(self):
#         for data in self.heap:
#             print(data,end='-->')
    


# maxHeap = HeapSort([1,6,2,5,4])
# maxHeap.display()


class HeapSort:
    def __init__(self, arr) -> None:
        self._sort(arr)

    def buildHeap(self,arr):
        self.heap = arr
        for index in range(self.parent(len(self.heap) - 1), -1, -1):
            self.heapifyDown(index)

    def heapifyDown(self,currIdx,endIdx,arr):
        leftIdx = self.lchild(currIdx)
        while leftIdx <= endIdx:
            rightIdx = self.rchild(currIdx)
            if rightIdx <= endIdx and arr[rightIdx] > arr[leftIdx] :
                idxToChg = rightIdx
            else:
                idxToChg = leftIdx
            
            if arr[idxToChg] > arr[currIdx]:
                self.swap(arr,idxToChg,currIdx)
                currIdx = idxToChg
                leftIdx = self.lchild(currIdx)
            else:
                return

    def heapifyUp(self):
        pass

    def parent(self, curr):
        return (curr - 1) // 2
    
    def lchild(self,curr):
        return (2 * curr) + 1

    def rchild(self,curr):
        return (2 * curr) + 2
    
    def swap(self,arr,first,second):
        arr[first], arr[second] = arr[second], arr[first]
        return
    
    def display(self):
        for data in self.heap:
            print(data,end='-->')
    
    def _sort(self,array):
        arr = array
        length_of_array = len(arr) - 1
        for i in range(self.parent(length_of_array), -1, -1):
            self.heapifyDown(i,length_of_array,arr)
        print(arr)
        for i in range(len(array) - 1, 0, -1):
            self.swap(arr,0,i)
            self.heapifyDown(0,i-1,arr)
arr = [1,6,2,5,4,7,3]
maxHeap = HeapSort(arr)
# maxHeap.display()
