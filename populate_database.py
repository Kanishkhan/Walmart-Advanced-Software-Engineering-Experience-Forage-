import csv
import sqlite3

class ShipmentDatabaseHandler:
    """
    Handles connections and data insertion into the shipment database.
    """

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def populate_database(self, data_folder):
        """
        Read shipping data from CSV files and populate the SQLite database.
        """
        with open(f"{data_folder}/shipping_data_0.csv", "r") as file0, \
             open(f"{data_folder}/shipping_data_1.csv", "r") as file1, \
             open(f"{data_folder}/shipping_data_2.csv", "r") as file2:

            reader0 = csv.reader(file0)
            reader1 = csv.reader(file1)
            reader2 = csv.reader(file2)

            self._insert_data_from_file_0(reader0)
            self._insert_data_from_files_1_and_2(reader1, reader2)

    def _insert_data_from_file_0(self, reader):
        """
        Process shipping_data_0.csv and insert records into the database.
        """
        for i, row in enumerate(reader):
            if i == 0:
                continue  # skip header

            origin, destination = row[0], row[1]
            product_name = row[2]
            quantity = row[4]

            self._insert_product_if_missing(product_name)
            self._insert_shipment(product_name, quantity, origin, destination)
            print(f"Inserted row {i} from shipping_data_0")

    def _insert_data_from_files_1_and_2(self, reader1, reader2):
        """
        Combine and insert data from shipping_data_1.csv and shipping_data_2.csv
        based on shipment identifiers.
        """
        shipment_data = {}

        for i, row in enumerate(reader2):
            if i == 0:
                continue
            shipment_id, origin, destination = row[0], row[1], row[2]
            shipment_data[shipment_id] = {
                "origin": origin,
                "destination": destination,
                "products": {}
            }

        for i, row in enumerate(reader1):
            if i == 0:
                continue
            shipment_id = row[0]
            product = row[1]

            products = shipment_data[shipment_id]["products"]
            products[product] = products.get(product, 0) + 1

        count = 0
        for shipment_id, data in shipment_data.items():
            origin = data["origin"]
            destination = data["destination"]
            for product, qty in data["products"].items():
                self._insert_product_if_missing(product)
                self._insert_shipment(product, qty, origin, destination)
                print(f"Inserted shipment {count} from shipping_data_1/2")
                count += 1

    def _insert_product_if_missing(self, name):
        """
        Insert a product only if it doesn't already exist.
        """
        self.cursor.execute("""
            INSERT OR IGNORE INTO product (name) VALUES (?);
        """, (name,))
        self.conn.commit()

    def _insert_shipment(self, product_name, qty, origin, destination):
        """
        Insert a shipment linked to a product by foreign key.
        """
        self.cursor.execute("""
            SELECT id FROM product WHERE name = ?;
        """, (product_name,))
        product_id = self.cursor.fetchone()[0]

        self.cursor.execute("""
            INSERT OR IGNORE INTO shipment (product_id, quantity, origin, destination)
            VALUES (?, ?, ?, ?);
        """, (product_id, qty, origin, destination))
        self.conn.commit()

    def close(self):
        self.conn.close()


if __name__ == "__main__":
    handler = ShipmentDatabaseHandler("shipment_database.db")
    handler.populate_database("./data")
    handler.close()
