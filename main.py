from sqlalchemy import create_engine, MetaData, text
from sqlalchemy import Table, Column, Integer, String, ForeignKey, DATE
metadata = MetaData()

engine = create_engine("mysql+mysqlconnector://root:1234@localhost:3306")

connection = engine.connect()

connection.execute(text("DROP DATABASE IF EXISTS sklad"))
connection.execute(text("CREATE DATABASE IF NOT EXISTS sklad"))

metadata = MetaData()

class_t = Table('class', metadata,
    Column('id_class', Integer, primary_key=True),
    Column('name', String(50), nullable=False)
)

staff_t = Table('staff', metadata,
    Column('id_staff', Integer, primary_key=True),
    Column('surname', String(32), nullable=False),
    Column('name', String(32), nullable=False),
    Column('phone', String(32), nullable=False)
)

rooms_t = Table('rooms', metadata,
    Column('id_room', Integer, primary_key=True),
    Column('class_id', Integer, ForeignKey("class.id_class")),
    Column('price', Integer, nullable=False),
    Column('number_of_places', Integer, nullable=False),
    Column('status', String(32), nullable=False)
)


room_service_t = Table('room_service', metadata,
    Column('id_room_service', Integer, primary_key=True),
    Column('staff_id', Integer, ForeignKey("staff.id_staff")),
    Column('room_id', Integer, ForeignKey("rooms.id_room"))
)


guests_t = Table('guests', metadata,
    Column('id_guests', Integer, primary_key=True),
    Column('surname', String(32), unique=True, nullable=False),
    Column('name', String(32), nullable=False),
    Column('quantity', Integer, nullable=False),
    Column('check_in', DATE, nullable=False),
    Column('check_out', DATE, nullable=False),
    Column('room_id', Integer, ForeignKey("rooms.id_room"))
)


engine = create_engine("mysql+mysqlconnector://root:1234@localhost/hostel", echo=True)
metadata.create_all(engine)
connection = engine.connect()


ins_staff_t1 = staff_t.insert().values(id_staff=1, surname='Varinova', name='Natasha', phone='+799566781')
ins_staff_t2 = staff_t.insert().values(id_staff=2, surname='Fortunov', name='Georgiy', phone='+798756222')
ins_staff_t3 = staff_t.insert().values(id_staff=3, surname='Postanov', name='Oleg', phone='+799399993')
ins_staff_t4 = staff_t.insert().values(id_staff=4, surname='Gatin', name='Dima', phone='+799490094')
ins_staff_t5 = staff_t.insert().values(id_staff=5, surname='Bulatov', name='Yana', phone='+799955695')
ins_staff_t6 = staff_t.insert().values(id_staff=6, surname='Agmalova', name='Renata', phone='+799699996')
ins_staff_t7 = staff_t.insert().values(id_staff=7, surname='Dudkin', name='Denis', phone='+796789997')
ins_staff_t8 = staff_t.insert().values(id_staff=8, surname='Gavrilina', name='Julia', phone='+799236798')
ins_staff_t9 = staff_t.insert().values(id_staff=9, surname='Stanislavovna', name='Karina', phone='+799178999')
ins_staff_t10 = staff_t.insert().values(id_staff=10, surname='Djenner', name='Stormi', phone='+79999004310')
connection.execute(ins_staff_t1)
connection.execute(ins_staff_t2)
connection.execute(ins_staff_t3)
connection.execute(ins_staff_t4)
connection.execute(ins_staff_t5)
connection.execute(ins_staff_t6)
connection.execute(ins_staff_t7)
connection.execute(ins_staff_t8)
connection.execute(ins_staff_t9)
connection.execute(ins_staff_t10)
connection.commit()

