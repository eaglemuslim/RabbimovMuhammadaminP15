import sqlite3
import hashlib
from datetime import datetime


def con():
    conn = sqlite3.connect('dtb.db')
    return conn


def create_table_user():
    conn = con()
    cur = conn.cursor()
    cur.execute("""
        create table if not exists user(
            `id` integer not null primary key autoincrement,
            `first_name` varchar(30) not null,
            `last_name` varchar(30) not null,
            `birth_day` date not null,
            `phone` varchar (13) not null,
            `username` varchar(50) not null,
            `password` varchar(150) not null,
            `is_admin` boolean default False
        )
    """)
    conn.commit()
    conn.close()


def insert_user(data: dict):
    conn = con()
    cur = conn.cursor()
    sha256 = hashlib.sha256()
    sha256.update(data['password1'].encode('utf-8'))
    hashed_password = sha256.hexdigest()
    query = """
        insert into user(
            `first_name`,
            `last_name`,
            `birth_day`,
            `phone`,
            `username`,
            `password`,
            `is_admin`
        ) values (?, ?, ?, ?, ?, ?, ?)
    """
    values = (data['first_name'], data['last_name'], data['birth_day'], data['phone'],
              data['username'], hashed_password, False)
    if data['password1'] == data['password2']:
        if is_exist('username', data['username']):
            print('This username is already exists!!!')
            return 405
        cur.execute(query, values)
        conn.commit()
        conn.close()
        return 201
    else:
        print('Passwords are not same!!!')
        return 405


def is_exist(field, field_data):
    query = f"""
        select count(id) from user where {field}=?
    """
    value = (field_data,)
    conn = con()
    cur = conn.cursor()
    cur.execute(query, value)
    return cur.fetchone()[0]


# def delete():
#     conn = con()
#     cursor = conn.cursor()
#     n = input("which id: ")
#     cursor.execute(f"""
#     delete from user where id = {n}
#     """)
#     conn.commit()
#     conn.close()


def update():
    conn = con()
    cursor = conn.cursor()
    n = int(input('choose one of them: '))
    section = """
        1.name     2.is_active     3.user_count 
        """
    data = {
        1: "name",
        2: "is_active",
        3: "user_count",
    }

    answer = 3
    if data.get(answer):
        value = input('Enter new value: ')
        cursor.execute(f"""
                update kurs set {data.get(answer)} = ? where id = ?
            """, (value, n))
    else:
        print('Invalid number try again!!!')
        update()
    conn.commit()
    conn.close()


def login(data: dict):
    username = data['username']
    password = data['password']
    conn = con()
    cur = conn.cursor()
    sha256 = hashlib.sha256()
    sha256.update(password.encode('utf-8'))
    hashed_password = sha256.hexdigest()
    query = """
        select id from user where username=? and password=?
    """
    value = (username, hashed_password)
    cur.execute(query, value)
    dt = cur.fetchone()
    conn.close()
    return bool(dt)


def create_kurs():
    conn = con()
    cur = conn.cursor()
    cur.execute("""
        create table if not exists kurs(
            id integer not null primary key autoincrement,
            name varchar(100) not null,
            is_activ boolean default false,
            user_count int
        )
    """)
    conn.commit()
    conn.close()


def insert_kurs(data: dict):
    conn = con()
    cur = conn.cursor()
    query = """
        insert into kurs(
            name,
            is_activ,
            user_count
        ) values (?,?,? )
    """
    value = (data['name'], True, 0)
    cur.execute(query, value)
    conn.commit()
    conn.close()