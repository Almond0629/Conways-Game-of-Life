執行方法：
    1. 主程式
        直接執行main.py
    2. 演算法
        執行still.py，裡面的size變數會決定運算範圍（size * size的正方形）

功能：
    1. 主程式
        - 按start/stop可以暫停/繼續遊戲，但如果幀率設定為零，該按鈕功能改為手動推進一回合
        - 按reset會回到遊戲剛開始的模板
        - 可點擊細胞編輯版面，且可以調整編輯方式(editing mode)
            - default（編號為-1）是切換所點細胞的生死狀態
            - 其他情況會顯示當前選取的小模塊，點擊會把小模塊bitwise or到原本的版面上
                - 小模塊來自演算法的輸出py檔
        - 調整規則相關變數
            - 若活細胞周圍的活細胞數小於minimum limitation to live(min_num_alive)，下一回合該細胞死亡
            - 若活細胞周圍的活細胞數大於maximum limitation to live(max_num_alive)，下一回合該細胞死亡
            - 若死細胞周圍的活細胞數等於reproduce condition(num_repro)，下一回合該細胞復活
        - 調整運行幀率（順暢與否與電腦有關，小於10時較為順暢）
        - 播放Rick Astley -- Never Gonna Give You Up（很重要） 音源：https://youtu.be/9NcPvmk4vfo
    2. 演算法
        - 透過爆搜找到在size * size範圍內穩定的狀態
        - 檔案內設有計算2 ** 18個情況的上限(maximum)，避免跑太久
        