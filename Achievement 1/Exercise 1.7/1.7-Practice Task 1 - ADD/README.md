# 📘 Exercise 1.7 – Practice Task 1

✅ Step‑by‑Step Workflow for Task Screenshots

1. Activate My Virtual Environment
   In Command Prompt:
   workon cf-python-base
   📸 Screenshot: the activated environment (cf-python-base).

2. Open IPython and Define ORM Model
   ipython
   In IPython:
   from sqlalchemy.orm import declarative_base
   from sqlalchemy import Column
   from sqlalchemy.types import Integer, String

Base = declarative_base()

class Recipe(Base):
**tablename** = "practice_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return f"<Recipe ID: {self.id} - {self.name}>"

📸 Screenshot: the class definition.

3. Create Engine and Table
   from sqlalchemy import create_engine
   engine = create_engine("mysql+pymysql://cf-python:password@localhost/my_database")

Base.metadata.create_all(engine)

📸 Screenshot: successful execution.

4. Create Session
   from sqlalchemy.orm import sessionmaker
   Session = sessionmaker(bind=engine)
   session = Session()

📸 Screenshot: session creation.

5. Add Entries with ORM
   tea = Recipe(name="Tea", ingredients="Tea Leaves, Water, Sugar", cooking_time=5)
   coffee = Recipe(name="Coffee", ingredients="Coffee Powder, Sugar, Water", cooking_time=5)
   cake = Recipe(name="Cake", ingredients="Sugar, Butter, Eggs, Vanilla Essence, Flour, Baking Powder, Milk", cooking_time=50)
   smoothie = Recipe(name="Banana Smoothie", ingredients="Bananas, Milk, Peanut Butter, Sugar, Ice Cubes", cooking_time=5)

session.add_all([tea, coffee, cake, smoothie])
session.commit()

📸 Screenshot: code block adding entries.

6. Verify in MySQL CLI
   Exit IPython (exit()), then in Command Prompt:
   cd "C:\Program Files\MySQL\MySQL Server 8.0\bin"
   mysql -u root -p

Enter root password, then at mysql> prompt:
USE my_database;
SELECT \* FROM practice_recipes;

📸 Screenshot: tabular output showing Tea, Coffee, Cake, Banana Smoothie.

✅ Folder Structure for GitHub

- Exercise 1.7/
- 1.7-Practice Task 1/
- step 1-5.png:-
- 1: Environment activation
- 2: ORM class definition
- 3: Table creation
- 4: Session creation
- 5: Adding entries
- step 6-1.png:-
- 1: MySQL CLI output

👉 This gives you a complete narrative: from environment setup → ORM class → session → adding entries → verifying in MySQL.

👉 In short:

- IPython → shows the update in your Python object.
- MySQL CLI → shows the update persisted in the database after session.commit().
