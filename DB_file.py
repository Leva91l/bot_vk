import vk_api
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, insert
from vk_api.longpoll import VkLongPoll

with open('Token_VKinder', 'r') as f:
    token = str(f.readline())

vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)

with open('DB_conn_info.txt', 'r') as f:
    DSN = f.readline()

engine = create_engine(
    DSN,
    echo=True,
    # если True, то в консоль(print) будут сыпаться все запросы к бд, то есть все что алхимия делает по порядку
    pool_size=5,  # количество возможных соединений
    max_overflow=10  # количество максимальных доп соединений
)

metadata_obj = MetaData()  # метадата хранит данные обо всех таблицах на стороне приложения Python

men = Table(
    'men',
    metadata_obj,
    Column('vk_id', Integer),
    Column('name', String),
    Column('age', String),
    Column('sex', String),
    Column('city', String),
    Column('objective', String),
    Column('intention', String),
    Column("partner's age", String)
)

women = Table(
    'women',
    metadata_obj,
    Column('vk_id', Integer),
    Column('name', String),
    Column('age', String),
    Column('sex', String),
    Column('city', String),
    Column('objective', String),
    Column('intention', String),
    Column("partner's age", String)
)

metadata_obj.create_all(engine)


def insert_data(table, user_id, name, age, sex, city, objective, intention, partners_age):
    with engine.connect() as conn:
        stmt = insert(table).values(
            [
                {'vk_id': user_id,
                 'name': name,
                 'age': age,
                 'sex': sex,
                 'city': city,
                 'objective': objective,
                 'intention': intention,
                 "partner's age": partners_age},

            ]
        )
        conn.execute(stmt)
        conn.commit()

# def select_partner():
