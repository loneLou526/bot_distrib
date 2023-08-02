import sqlite3 as sl

class Data_base():
    def __init__(self) -> None:
        self.name = None
        self.id = None
        self.time = None
        self.mes = None
    

    def select(self):
        try:
            con = sl.connect('test.db')
            cursor = con.cursor()
            cursor.execute(f"""SELECT group_name, id_bot, send_time, mes_text FROM test""")
            ret = cursor.fetchall()
            self.name = [x[0] for x in ret]
            self.id = [x[1] for x in ret]
            self.time = [x[2] for x in ret]
            self.mes = [x[3] for x in ret]

        except sl.Error as ex:
            print('Ошибка в SQLite', ex)

        finally:
            if con:
                cursor.close()
                con.close()
    
    # ВОЗМОЖНО НЕНУЖНАЯ 
    def update_db(self, name, time, mes):
        try:
            con = sl.connect('test.db')
            cursor = con.cursor()
            cursor.execute(f"""SELECT id FROM test WHERE group_name = ?""", (name, ))
            if cursor.fetchone():
                cursor.execute(f"""
                UPDATE test SET send_time = ?, mes_text = ? WHERE group_name = ?""", (time, mes, name))
                con.commit()
                cursor.close()
                return f'Сообщение {mes} будет отправлено в группу {name} в {time}'
            else:
                cursor.close()
                return 'Такой группы нет в моей базе.'
                
        except sl.Error as ex:
            print('Ошибка в SQLite', ex)

        finally:
            if con:
                con.close()
        
    
    def insert_db(self, gr_name, id_bot):
        try:
            con = sl.connect('test.db')
            cursor = con.cursor()
            cursor.execute("""SELECT group_name FROM test WHERE id_bot = ?""", (id_bot, ))
            if cursor.fetchone() is None:
                cursor.execute(f"""INSERT INTO test (group_name, id_bot, send_time, mes_text) VALUES (?, ?, ?, ?)""", (gr_name, id_bot, None, None))
                con.commit()
                cursor.close()
                return ('Ваша группа добавлена в базу данных.')
             
            return 'Ваша группа уже есть в базе данных.'

        except sl.Error as ex:
            print('Ошибка в SQLite', ex)

        finally:
            if con:
                con.close()


# a = Data_base()
# a = a.insert_db('Test 1', ':50:00')
# print(a)