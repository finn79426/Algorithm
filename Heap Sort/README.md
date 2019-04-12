# Heap Sort 堆積排序法

![](heap-sort.gif)

- 簡介
    - 二元樹的一種 ⇒ 每個父節點最多兩個子節點
    - 堆積樹為**完全二元樹(Complete Binary Tree)**的一種
    - 從小到大的排序為**最大堆積(Max Heap)**：父節點的值大於子節點 (根節點一定是所有節點的最大值)
    - 從大到小的排序為**最小堆積(Min Heap)**：父節點的值小於子節點 (根節點一定是所有節點的最小值)
    - 兄弟節點(旁系節點)的大小並不重要

- 作法 (由小到大排序)
    1. 將一維數列映射成二元樹(Binary tree)
    2. 將二元樹調整為**最大堆積樹(Max Heap)**
        - 二元樹有 (n/2) 個**內部節點**
        - 依陣列由後到前以每個內部節點作為根(Root)節點，作**堆積化(Heapify)**
    3. 將**樹根(最大值)**與**排序前最後一個節點**調換，將最後一個節點(原樹根)**取出**，並加入已排序數列
        - 相當於對 Max Heap Tree 作 Delete MaxNode
    4. 對整棵樹重新調整為最大堆積樹 ⇒ 調整後樹根為 Max Node
    5. 重複步驟 3、4

- 堆積化作法
    1. 令Root、左子元素、右子元素3個元素中，最大者為MaxNode
    2. 若Root = MaxNode ⇒ 結束
    3. 若左子元素或右子元素 = MaxNode ⇒ 將Root與MaxNode作對調(Swap)
        - 若對調完的Root有子節點 ⇒ 對原來的Root作Heapify (往下遞歸)



- 時間複雜度(Time Complexity)
    - Best Case: ![](https://latex.codecogs.com/gif.latex?O%5Cleft%28%20n%5Clog%20n%5Cright%29)
    - Worst Case: ![](https://latex.codecogs.com/gif.latex?O%5Cleft%28%20n%5Clog%20n%5Cright%29)
    - Average Case: ![](https://latex.codecogs.com/gif.latex?O%5Cleft%28%20n%5Clog%20n%5Cright%29)
- 空間複雜度(Space Complexity)：![](https://latex.codecogs.com/gif.latex?%5Ctheta%20%5Cleft%28%201%5Cright%29)
- 穩定性(Stable/Unstable)：不穩定(Unstable)
