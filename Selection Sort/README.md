# Selection Sort 選擇排序法

![](selection-sort.gif)

- 簡介
    - 反覆從未排序的數列中取出最小的元素，加入到另一個的數列，結果即為已排序的數列。
- 作法
    1. 將資料分成**已排序**、**未排序**兩部份
    2. 依序由**未排序**中找**最小/大值**，加入到已排序部份的末端
- 時間複雜度(Time Complexity)
    - Best Case: ![](https://latex.codecogs.com/gif.latex?O%5Cleft%28%20n%5E%7B2%7D%5Cright%29)
    - Worst Case: ![](https://latex.codecogs.com/gif.latex?O%5Cleft%28%20n%5E%7B2%7D%5Cright%29)
    - Average Case: ![](https://latex.codecogs.com/gif.latex?O%5Cleft%28%20n%5E%7B2%7D%5Cright%29)
- 空間複雜度(Space Complexity)：![](https://latex.codecogs.com/gif.latex?%5Ctheta%20%5Cleft%28%201%5Cright%29)
- 穩定性(Stable/Unstable)：不穩定(Unstable)
