from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("url_connexion_bdd")


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    
# Create the database and tables
Base.metadata.create_all(engine)

# Create session connected to database
Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name='John', age=30)

# add user entry to table USER
session.add(new_user)
session.commit()

# Query the user over 25 years.
users_over_25 = session.query(User).filter(User.age > 25).all()

for user in users_over_25:
    print(f"Nom: {user.name}, Age: {user.age}")


