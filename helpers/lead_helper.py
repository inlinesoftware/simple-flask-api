from connection.db_connection import DBConnection

class LeadHelper:
	def __init__(self):
		self.db = DBConnection()
		self.connection = self.db.get_connection()

	def insert_lead(self, name, email, origin):
		cursor = self.connection.cursor()
		sql    = "INSERT INTO lead (name, email, origin) VALUES (%s, %s, %s)"
		val    = (name, email, origin)
		cursor.execute(sql, val)
		self.connection.commit()
		print(cursor.rowcount, "lead inserted.")
		return "200"

	def compute_access(self, origin):
		cursor = self.connection.cursor()
		sql    = "SELECT amount FROM campaing WHERE origin = '%s'" % origin
		cursor.execute(sql)
		amount = cursor.fetchall()
		amount = amount[0][0]
		new_amount = int(amount) + 1
		self.update_acess(origin, new_amount)

		return str(new_amount)

	def update_acess(self, origin, amount):
		cursor = self.connection.cursor()
		sql = "UPDATE campaing SET amount = '%s' WHERE origin = '%s'" % (amount, origin)
		cursor.execute(sql)
		self.connection.commit()