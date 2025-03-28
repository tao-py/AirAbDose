import pandas as pd
import pymysql
import time
from MyLibrary import GeneralTools as GT

def excel_mysql(excel_file,table_name = "Data" ):
        #  读取 Excel 文件
    df = pd.read_excel(excel_file, sheet_name=0)  # 读取第一个 Sheet
    title_lst = df.columns.tolist()
    print(title_lst)

    # 连接 MySQL 数据库
    conn = pymysql.connect(
        host="127.0.0.1",  
        port=3306,         
        user="root", 
        password="tao@1999", 
        charset="utf8"
    )
    cursor = conn.cursor()

    # 查看已有数据库
    cursor.execute("show databases")
    result = cursor.fetchall()
    print(result) 

    # 创建数据库（新增、删除、修改）
    cursor.execute("CREATE DATABASE IF NOT EXISTS DoseData DEFAULT CHARSET utf8 COLLATE utf8_general_ci")
    # 如果不存在则创建数据库
    conn.commit()
    cursor.execute("show databases")
    result = cursor.fetchall()
    print(result)

    cursor.execute("use DoseData")
    cursor.execute("show tables")
    result = cursor.fetchall()
    print(result)
    
    # 删除重建，不要时注释
    sql='''drop table if EXISTS {0}'''.format(table_name)
    cursor.execute(sql)
    conn.commit()
    
    sql = '''
    CREATE TABLE IF NOT EXISTS {} (
    {} int not null primary key auto_increment,
    {} VARCHAR(32) not null,
    {} varchar(32) not null,
    {} boolean not null,
    {} varchar(32) not null,
    {} int unsigned not null,
    {} FLOAT(6,1) default 0,
    {} FLOAT(6,1) default 0,
    {} FLOAT(6,1) default 0,
    {} varchar(32) not null
    )DEFAULT CHARSET=utf8;
    '''.format(table_name,*title_lst) # *号的作用是将列表拆分成多个参数
    cursor.execute(sql)
    conn.commit()

    cursor.execute("show tables")
    result = cursor.fetchall()  
    print(result)

    # 插入数据
    start = time.perf_counter()
    for _, row in df.iterrows(): # _表示索引
        GT.progress_bar(_, len(df), start,str(row[0]))
        values = "', '".join(map(str, row.fillna("").tolist()))  # 处理空值
        # print(values)
        insert_sql = f"INSERT INTO `{table_name}` VALUES ('{values}');"
        cursor.execute(insert_sql)


    # 提交更改并关闭连接
    conn.commit()
    cursor.close()
    conn.close()

# print("Excel 数据已成功导入 MySQL！")
if __name__ == '__main__':
    excel_mysql('./Out/Tosql.xlsx')