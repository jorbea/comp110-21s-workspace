"""Utility functions for wrangling data."""

__author__ = "730151647"

from csv import DictReader
from os import confstr_names
from typing import KeysView


def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    rows: list[dict[str, str]] = []
    
    file_handle = open(csv_file)
    csv_reader = DictReader(file_handle)

    for row_by_row in csv_reader:
        rows.append(row_by_row)
    file_handle.close()
    return rows


def column_values(rows: list[dict[str, str]], row_name: str) -> list[str]:
    """Takes a list of dictionaries and returns a list of values that share a key."""
    column: list[str] = []

    for section in rows:
        column.append(section[row_name])
    return column


def columnar(list_of_rows: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transforms a list of rows into a dictionary of columns."""
    table: dict[str, list[str]] = {}
    
    first_row = list_of_rows[0]

    for column_name in first_row:
        table[column_name] = column_values(list_of_rows, column_name)
    return table


def head(column_table: dict[str, list[str]], number_of_rows: int) -> dict[str, list[str]]:
    return_table: dict[str, list[str]] = {}
    
    first_row = column_table.keys()
    first_value = column_table.values()
    i: int = 0

    for key in first_row:
        n_values: list[str] = []
        for value in first_value:
            while i < number_of_rows:
                n_values.append(value[i])
                return_table[key] = n_values
                i += 1
    return return_table