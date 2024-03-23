from os import getenv
from typing import Union, Dict, List

import mysql.connector

from utils.app_error import AppError


class MySQL:
    def __init__(self) -> None:
        config = {
            "user": getenv("MYSQL_DATABASE_USER"),
            "password": getenv("MYSQL_DATABASE_PASSWORD"),
            "database": getenv("MYSQL_DATABASE_NAME"),
            "host": getenv("MYSQL_DATABASE_HOST"),
            "raise_on_warnings": True,
        }

        try:
            self.__connection = mysql.connector.connect(**config)
            self.__database = self.__connection.cursor(dictionary=True)

        except mysql.connector.Error as error:
            raise AppError(
                f"Failed to create a database connection. Error: {error}",
                should_abort=False,
            ) from error

    def query(self, sql: str, params: List, is_single=True) -> Union[Dict, None]:
        try:
            self.__database.execute(sql, params)

            if is_single:
                return self.__database.fetchone()

            return self.__database.fetchall()

        except mysql.connector.Error as error:
            self.__connection.close()
            self.__database.close()

            return AppError(
                f"Failed to execute a query on the database. Error: {error}",
            )

    def mutate(self, sql: str, params: List) -> Dict:
        try:
            self.__database.execute(sql, params)
            self.__database.commit()

        except mysql.connector.Error as error:
            print(
                f"Failed to execute a mutation on the database. Error: {error}",
                flush=True,
            )
            self.__connection.close()
            self.__database.close()