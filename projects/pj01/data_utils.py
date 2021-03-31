"""Utility functions for wrangling data."""

__author__ = "730151647"

from csv import DictReader
# from os import confstr_names
# from typing import KeysView

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
    """Produces a table with the first N rows of data for each column."""
    head_table: dict[str, list[str]] = {}
    
    for key in column_table:
        head_table[key] = column_table[key][:number_of_rows]
    return head_table


def select(col_table: dict[str, list[str]], col_names: list[str]) -> dict[str, list[str]]:
    """Produces a table with only a specific subset of the original columns."""
    select_table: dict[str, list[str]] = {}
    
    for name in col_names:
        select_table[name] = col_table[name]
    return select_table


def count(list_values: list[str]) -> dict[str, int]:
    """Produces a dictionary of values within a column and their frequencies expressed as an integer."""
    count_table: dict[str, int] = {}

    for value in list_values:
        if value in count_table:
            count_table[value] += 1
        else:
            count_table[value] = 1
    return count_table