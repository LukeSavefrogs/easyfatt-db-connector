import unittest

from easyfatt_db_connector.core.connection import EasyfattFDB
from easyfatt_db_connector.core.exceptions import FirebirdClientError

TEST_DATABASE = "~/Documents/Danea Easyfatt/TestArchivio.eft"

class TestEasyfattFDB(unittest.TestCase):
	def test_wrong_db(self):
		self.assertRaisesRegex(FirebirdClientError, r"The path '.*?TEST.EFT' does not exist.", lambda: EasyfattFDB("tests/TEST.EFT"))

	def test_connection(self):
		with EasyfattFDB(TEST_DATABASE).connect() as connection:
			self.assertIsNotNone(connection)
			self.assertFalse(connection.closed)

			self.assertIsNotNone(connection.cursor())
			tables = connection.cursor().execute("select * from RDB$RELATIONS").fetchall()
			self.assertGreater(len(tables), 10)
			


if __name__ == "__main__":
	unittest.main()