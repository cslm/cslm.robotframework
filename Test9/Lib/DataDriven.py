import csv
import xlrd
import os

class DataDriven(object):

	def read_csv_file(self, filename):
		csv_dict = csv.DictReader(open(filename))
		return csv_dict
		
	def xls_to_csv(self, filename, wsheet):
		wb = xlrd.open_workbook(filename)
		sh = wb.sheet_by_name(wsheet)
		curr_dir =  os.getcwd()
		csvfile = curr_dir + '\\test_data\\tmp.csv'
		a = open(csvfile, 'wb')
		wr = csv.writer(a, quoting=csv.QUOTE_ALL)
		for rownum in xrange(sh.nrows):
			wr.writerow(sh.row_values(rownum))
		a.close()

	def read_xls_file(self,filename,worksheet):
		self.xls_to_csv(filename, worksheet)
		curr_dir =  os.getcwd()
		cf = curr_dir + '\\test_data\\tmp.csv'
		xls_data = self.read_csv_file(cf)
		return xls_data