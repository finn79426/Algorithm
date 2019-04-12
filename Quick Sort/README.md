# Quick Sort 快速排序法

![](quick-sort.gif)

- 簡介
    - 將問題分解成較小的子問題，用相同的解決程序一一解決後，再將子問題的結果整合成原問題的答案。
    - 快速排序法的效率和**基準值(Pivot)的選擇**息息相關，
        - 所以每次選擇的**基準值(Pivot)**愈接近數列的平均值或中位數愈好

- 作法
    1. 選定一個**基準值(Pivot)**，通常一開始會選擇陣列頭或陣列尾的元素
    2. 比基準值(Pivot)小的數值移到基準值左邊，形成**左子串列**
    3. 將比基準值(Pivot)大的數值移到基準值右邊，形成**右子串列**
    4. 分別對**左子串列**、**右子串列**作上述三個步驟 ⇒ 遞迴(Recursive)
        - 直到左子串列或右子串列只剩一個數值或沒有數值

- 時間複雜度(Time Complexity)
    - Best Case: ![](https://latex.codecogs.com/gif.latex?O%5Cleft%28%20n%5Clog%20n%5Cright%29)
    - Worst Case: ![](https://latex.codecogs.com/gif.latex?O%5Cleft%28%20n%5E%7B2%7D%5Cright%29)
    - Average Case: ![](https://latex.codecogs.com/gif.latex?O%5Cleft%28%20n%5Clog%20n%5Cright%29)
- 空間複雜度(Space Complexity)：![](https://latex.codecogs.com/gif.latex?%5Ctheta%20%5Cleft%28%20%5Clog%20n%5Cright%29) ~ ![](\theta \left( n\right) )
- 穩定性(Stable/Unstable)：不穩定(Unstable)
