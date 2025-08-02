# 데이터베이스에 새로운 테이블을 만들고, 데이터프레임 올리기

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database

create_database('mysql+pymysql://root:1234@127.0.0.1:3306/exam')
    

# 데이터베이스에 들어갈 데이터프레임(예) 만들기
price = pd.DataFrame({
    "날짜":['2021-01-02', '2021-01-03'],
    "티커":['000001', '000001'],
    "종가":[1340, 1315],
    "거래량":[1000, 2000]
})

price

# 데이터베이스에 데이터프레임 올리기
engine = create_engine('mysql+pymysql://root:1234@127.0.0.1:3306/exam')
price.to_sql(name='price', con=engine, if_exists="append", index=False)
engine.dispose()

# 새로운 시계열 데이터가 추가될 경우(기존 데이터 이후에 그대로 데이터가 쌓여버리는 문제가 발생)
new = pd.DataFrame({
    "날짜":['2021-01-04'],
    "티커":['000001'],
    "종가":[1320],
    "거래량":[1500]
})
price = pd.concat([price, new]) # concat함수를 이용 두데이터 프레임을 합침
engine = create_engine('mysql+pymysql://root:1234@127.0.0.1:3306/exam')
price.to_sql(name='price', con=engine, if_exists="append", index=False)
engine.dispose() # 아까 입력했던 데이터 이후, 그대로 데이터가 쌓여버림: 중복된 데이터가 발생해버림
# append 대신 replace를 쓰면, 기존 데이터는 삭제되어버리는 문제 역시 발생

# 새로 추가되는 2021-01-04 데이터만 추가하려면 upsert를 사용해야함.

# upsert 사용방법(pymysql을 사용해야함)

import pymysql

price = pd.DataFrame({
    "날짜":['2021-01-04','2021-01-04'],
    "티커":['000001','000002'],
    "종가":[1320, 1315],
    "거래량":[2100, 1500]
})

args = price.values.tolist() # 밸류값을 리스트로 전환
args

con = pymysql.connect(
    user = 'root',
    passwd = '1234',
    host = '127.0.0.1',
    db= 'exam',
    charset = 'utf8')

query = """
insert into price_2 (날짜, 티커, 종가, 거래량)
values (%s,%s,%s,%s) as new
on duplicate key update
종가 = new.종가, 거래량 = new.거래량;    # 쿼리가 중요
"""

mycursor = con.cursor()
mycursor.executemany(query, args)
con.commit()
con.close()












