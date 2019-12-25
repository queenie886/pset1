from .hash_str import get_csci_salt, get_user_id, hash_str


def get_user_hash(username, salt=None):
    salt = salt or get_csci_salt()
    return hash_str(username, salt=salt)


if __name__ == "__main__":

    for user in ["gorlins", "<YOUR_GITHUB_USERNAME>"]:
        print("Id for {}: {}".format(user, get_user_id(user)))

    data_source = "data/hashed.xlsx"

    # TODO: read in, save as new parquet file, read back just id column, print
