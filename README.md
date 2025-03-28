##### 历年空气吸收剂量数据分析

- 快速安装第三方库

  ```cmd
  pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
  ```

- 运行 Dppdf.py 爬取数据，保存至Data文件夹
- 运行 Toexcel.py 提取转化数据
- 运行 Tomysql.py 将处理好的数据，导入本地的MySQL服务器，库dosedata--表data中
- 可以自定义main.py，连续执行

