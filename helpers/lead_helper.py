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
