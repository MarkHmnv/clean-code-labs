from abc import ABC, abstractmethod


# 1. Common interface for query building
class QueryBuilder(ABC):
    @abstractmethod
    def select(self, table: str, columns: list):
        pass

    @abstractmethod
    def where(self, condition: str):
        pass

    @abstractmethod
    def limit(self, limit: int):
        pass

    @abstractmethod
    def getSQL(self) -> str:
        pass


# 2. PostgreSQL-specific query builder
class PostgresQueryBuilder(QueryBuilder):
    def __init__(self):
        self._query = ''

    def select(self, table: str, columns: list):
        columns_part = ', '.join(columns)
        self._query = f'SELECT {columns_part} FROM {table}'
        return self

    def where(self, condition: str):
        self._query += f' WHERE {condition}'
        return self

    def limit(self, limit: int):
        self._query += f' LIMIT {limit}'
        return self

    def getSQL(self) -> str:
        return self._query


# 3. MySQL-specific query builder
class MySQLQueryBuilder(QueryBuilder):
    def __init__(self):
        self._query = ''

    def select(self, table: str, columns: list):
        columns_part = ', '.join(columns)
        self._query = f'SELECT {columns_part} FROM {table}'
        return self

    def where(self, condition: str):
        self._query += f' WHERE {condition}'
        return self

    def limit(self, limit: int):
        self._query += f' LIMIT {limit}'
        return self

    def getSQL(self) -> str:
        return self._query


if __name__ == '__main__':
    postgres_builder = PostgresQueryBuilder()
    postgres_query = (
        postgres_builder.select('users', ['id', 'name', 'email'])
        .where('age > 18')
        .limit(10)
        .getSQL()
    )
    print('PostgreSQL Query:', postgres_query)

    mysql_builder = MySQLQueryBuilder()
    mysql_query = (
        mysql_builder.select('users', ['id', 'name', 'email'])
        .where('age > 18')
        .limit(10)
        .getSQL()
    )
    print('MySQL Query:', mysql_query)
