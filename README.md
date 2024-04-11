# 資料庫系統專題-選課系統

## 環境準備
1. 下載 [XAMPP](https://www.apachefriends.org/zh_tw/index.html)，並安裝
2. 以系統管理員身分執行 `XAMPP Control Panel`
3. 按下 `Apache` 和 `MySQL` 的 `Start`
4. 按下 `MySQL` 的 `Admin` 開啟 phpMyAdmin 介面
5. 進入資料庫 `testdb` 並匯入 `db/01_init.sql`
6. 進入資料庫 `testdb` 並匯入 `db/02_data.sql`
7. 進入資料庫 `testdb` 並匯入 `db/03_preselection.sql`

## 選課系統
1. 開啟指令界面，並切換至 `選課系統` 資料夾
2. 安裝所需套件
    ```bash
    pip3 install -r requirements.txt
    ```
3. 若安裝 `mysqlclient` 時出現錯誤 `error: Microsoft Visual C++ 14.0 is required.`，請根據 Python 版本與位元數手動安裝對應套件檔案。
    ```bash
    pip3 install mysqlclient/mysqlclient-1.4.6-cp37-cp37m-win32.whl
    ```
    若無對應版本之 whl 檔案，可於 [這裡](https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python) 下載使用
4. 使用 Flask 啟動服務
    ```bash
    flask run
    ```
    或
    ```bash
    python3 -m flask run
    ```
5. 使用瀏覽器訪問 [http://localhost:5000/](http://localhost:5000/)
