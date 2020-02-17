#! -*- coding:utf-8 -*-

import pymysql



First_Value=1000000
Now_total_Value="1050000"
Holding_value="526920"


def remove_douhao(num):
    num1 = "".join(num.split(","))
    f_num = int(num1)
    return f_num


def CountProfit():
    big_list= []
    r_ntv = remove_douhao(Now_total_Value)
    r_hv = remove_douhao(Holding_value)

    PL = (r_ntv-First_Value) /First_Value *100
    f_PL = round(PL,2)

    H_P = (r_hv/r_ntv) * 100
    f_HP = round(H_P,2)
    big_list.append((f_PL,f_HP))

    return big_list




def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
                                 db='IB',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:
        cursor.executemany('insert into Demo_IB_trading (f_PL,f_HP) values (%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except StopIteration:
        pass


if __name__=="__main__":
    content = CountProfit()
    insertDB(content)




# # # (f_PL,f_HP)


# create table Demo_IB_trading(
# id int not null primary key auto_increment,
# f_PL varchar(10),
# f_HP varchar(10),
# LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
# ) engine=InnoDB  charset=utf8;


# drop  table Demo_IB_trading;
