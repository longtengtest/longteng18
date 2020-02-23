import pymysql

DB_CONF = {
    'host': '115.28.108.130',
    'port': 3306,
    'user': 'test',
    'password': 'abc123456',
    'db': 'longtengserver'
}


class DB(object):  # 数据库基础操作，适用于任何数据库
    def __init__(self, db_conf):
        print(f'建立数据库连接: {db_conf}')  # todo 信息敏感，注掉
        self.conn = pymysql.connect(**db_conf, autocommit=True)
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)

    def query_db(self, sql):
        print(f"查询sql: {sql}", end=" ")
        self.cur.execute(sql)
        result = self.cur.fetchall()
        print(f"查询结果: {result}")
        return result

    def change_db(self, sql):
        print(f"执行sql: {sql}")
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception:
            self.conn.rollback()

    def close(self):
        self.cur.close()
        self.conn.close()


class LongTengServer(DB):
    def __init__(self, db_conf=DB_CONF):
        super().__init__(db_conf)

    def check_card(self, card_number):
        print(f'查询卡是否存在: {card_number}')
        sql = f'SELECT id FROM cardinfo WHERE cardNumber="{card_number}";'
        result = self.query_db(sql)
        if len(result) > 0:
            return True
        else:
            return False

    def delete_card(self, card_number):
        print(f'删除卡: {card_number}')
        sql = f'DELETE FROM cardinfo WHERE cardNumber="{card_number}";'
        self.change_db(sql)


if __name__ == '__main__':
    # db = DB(DB_CONF)
    # r = db.query_db('SELECT * FROM cardinfo WHERE cardNumber="245829";')
    # print(r)
    ldb = LongTengServer()
    ldb.check_card('54353')
    ldb.delete_card('54353')
    ldb.check_card('54353')
