# Merge Sort 合併排序法

![](merge-sort.gif)

- 簡介
    - 將**2個**已排序的陣列**合併(Merge)**，只需要N次比對的**線性時間(Linear Time)**
    - 將數列分成左、右子數列，分別對其作排序及合併
        - 比對次數最多為：左邊子數列長度 + 右邊子數列長度 - 1
- 作法
    - 合併排序作法:
        1. 將數列對分成**左子數列**、**右子數列**
        2. 分別對**左子數列**、**右子數列**作上一個步驟 ⇒ 遞迴(Recursive)
        3. 直到左子數列、右子數列被分割成只剩一個元素為止
            - 將僅剩的一個元素作為遞迴的結果回傳
        4. 對回傳的左子數列、右子數列依大小排列**合併**
        5. 將合併的結果作為遞迴的結果回傳
    - 合併作法:
        1. 將左子數列及右子數列依大小合併成一個新的數列
        2. 將左子數列及右子數列中，未填過的最小值填到新的數列
            - 若左子數列的數值都已填到新的數列 ⇒ 將右子數列中未填過的最小值填入新數列
            - 若右子數列的數值都已填到新的數列 ⇒ 將左子數列中未填過的最小值填入新數列
- 時間複雜度(Time Complexity)
    - Best Case: ![](https://latex.codecogs.com/gif.latex?O%5Cleft%28%20n%5Clog%20n%5Cright%29)
    - Worst Case: ![](https://latex.codecogs.com/gif.latex?O%5Cleft%28%20n%5Clog%20n%5Cright%29)
    - Average Case: ![](https://latex.codecogs.com/gif.latex?O%5Cleft%28%20n%5Clog%20n%5Cright%29)
- 空間複雜度(Space Complexity)：![](https://latex.codecogs.com/gif.latex?%5Ctheta%5Cleft%28%20n%5Cright%29)
- 穩定性(Stable/Unstable)：穩定(Stable)
