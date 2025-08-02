import pandas as pd
from sqlalchemy import create_engine

# engine = create_engine('mysql+pymysql://[사용자명]:[비밀번호]@[호스트:포트]/[사용할 데이터베이스]')
engine = create_engine('mysql+pymysql://root:1234@127.0.0.1:3306/shop')

query = "select * from goods;"
goods = pd.read_sql(query, con=engine)
engine.dispose() # 연결해제


# 데이터프레임을 sql데이터베이스에 저장

import seaborn as sns
iris = sns.load_dataset('iris')
iris.head()

engine = create_engine('mysql+pymysql://root:1234@127.0.0.1:3306/shop')
iris.to_sql(name='iris', con=engine, index=False, if_exists = 'replace')
engine.dispose()
