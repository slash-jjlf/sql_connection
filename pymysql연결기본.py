import pymysql

# 연결 기본
con = pymysql.connect(  
    user = 'root',
    passwd = '1234',
    host = '127.0.0.1',
    db = 'shop',
    charset = 'utf8'
    )

mycursor = con.cursor()

query = """
select * from goods;
"""

mycursor.execute(query) # 쿼리 실행
data = mycursor.fetchall() # 쿼리 실행한 데이터를 서버로부터 받아옴
con.close() # 작업 이후에는 반드시 테이터베이스와의 연결을 종료

data

# 데이터의 입력, 수정, 삭제 등
con = pymysql.connect(  
    user = 'root',
    passwd = '1234',
    host = '127.0.0.1',
    db = 'shop',
    charset = 'utf8'
    )

mycursor = con.cursor()

query = """
    insert into goods(goods_id, goods_name, goods_classify, sell_price, buy_price, register_date)
    values('0009', '스테이플러', '사무용품', '2000', '1500', '2020-12-30')
"""

mycursor.execute(query) # 쿼리 실행
con.commit() # 반드시 확정 갱신 필요
con.close()




