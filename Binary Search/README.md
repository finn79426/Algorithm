# Binary Search 二分搜尋法

![](binary-search.gif)

- 簡介
    - 利用**已排序**的特性來加快搜尋速度，每輪可以砍掉一半**已經確定不是搜尋結果**的資料，直到找到搜尋值
- 特性
    1. 資料必需事先排序
    2. 支援隨機存取(Random Access)機制
- 時間複雜度(Time Complexity)
    - ![](https://latex.codecogs.com/gif.latex?O%5Cleft%28%20%5Clog%20n%5Cright%29)