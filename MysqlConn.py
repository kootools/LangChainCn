import pymysql
class UsingMysql(object):
    def __init__(self,conn, commit=True):
        self._commit = commit
        self._conn = conn

    def __enter__(self):
        cursor = self._conn.cursor()
        self._conn.autocommit = False

        self._cursor = cursor
        return self

    def __exit__(self, *exc_info):
        # 提交事务
        if self._commit:
            self._conn.commit()
        # 在退出的时候自动关闭连接和cursor
        self._cursor.close()
        self._conn.close()

    @property
    def cursor(self):
        return self._cursor