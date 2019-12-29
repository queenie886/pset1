from .hash_str import get_csci_salt, get_user_id, hash_str
from .io import atomic_write
import pandas as pd
import os


def get_user_hash(username, salt=None):
    """Converts username string to hash digest

    :param username: string to hash
    :param salt: add randomness to the hashing
    :return: hash digest of input
    """
    # get salt if provided else retrieve it from environment variables
    salt = salt or get_csci_salt()
    return hash_str(username, salt=salt)


def convert_excel_to_parquet(data_source):
    """Converts an excel file to an equivalent parquet file that gets saved

    :param data_source: path to input excel file
    :return: the path to the newly created parquet file
    """
    # read excel file
    df = pd.read_excel(data_source, index_col=0)

    # save dataframe to parquet file
    parquet_file = os.path.splitext(data_source)[0] + ".parquet"
    with atomic_write(parquet_file, as_file=False) as f:
        df.to_parquet(f, engine="pyarrow")

    # return parquet file path
    return parquet_file


def read_parquet_columns(parquet_file, columns):
    """Converts an excel file to an equivalent parquet file that gets saved

    :param parquet_file: path to parquet file
    :param columns: list of columns
    :return: dataframe containing requested columns only
    """
    # read only specified columns and return them
    data = pd.read_parquet(parquet_file, engine="pyarrow", columns=columns)
    return data


if __name__ == "__main__":
    # compute and display hash for each user id provided
    for user in ["gorlins", "jsaikali"]:
        print("Id for {}: {}".format(user, get_user_id(user)))

    # path to data file
    data_source = "data/hashed.xlsx"

    # convert xlsx file to parquet file
    parquet_file = convert_excel_to_parquet(data_source)

    # read back just the hashed_id column and display it
    print(read_parquet_columns(parquet_file, ["hashed_id"]))


