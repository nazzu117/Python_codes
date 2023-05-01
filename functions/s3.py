from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Date, DateTime, Enum, Boolean, Table, ForeignKeyConstraint,\
asc, desc
from sqlalchemy import create_engine, engine_from_config, desc
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, scoped_session
SQLALCHEMY_DATABASE_URI= "mysql+pymysql://tapsium_aiml: Tapsium123@tapsiundbinstance.ccpoyzezuqrd.us-east-1.rds.amazonaws.com:6005/Tapsium AIML" engine create engine (SQLALCHEMY DATABASE_URI, pool size 50, max_overflow=100, poot_pre_ping-True, pool recycle=208) = Base declarative_base() Base._session = session
engine=create_engine(SQLALCHEMY_DATABASE_URI, pool_size=50,max_overflow =100,pool_pre_ping=True,pool_recycle=200)
Base=declarative_base()
session= scoped_session (sessionmaker (bind=engine))
print("session", session)
Base._seassion = session

#ORM techinques- 08ject relational mapping

class SKU(Base):
    __tablename__ ='nb_defect_transaction_kibana_training_data'
    id= Column (Integer(), primary_key=True)
    jira_key= Column (String(225))
    e2e_request_id = Column (String(225))
    status_cd= Column(String(225))
    service_name = Column(String(225))
    client_id =Column(String(225))
    response =Column(String(500))
    error_details = Column(String(500))
    error_message =Column(String(225))
    defect_type =Column(String(225))
    jira_root_cause1 =Column(String(225))
    defect_component =Column(String(225))
    update_timestamp = Column (DateTime(timezone True), default-datetime.now)
    reference =Column(String(45))
    user=Column(String(45))
    def _repr_(self):
        return "<Product (id='%s')" % (self.id)

Base.metadata.create_all(engine)

print("final")