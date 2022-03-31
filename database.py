class Student(Base):
_tablename_ = "Students"
id = Column(Integer, primary_key=True)
name = Column(String(50))
class = Column(Integer)