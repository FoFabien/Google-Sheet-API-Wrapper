# -*- coding: utf-8 -*-
import Google

sheet = Google("https://www.googleapis.com/auth/spreadsheets") # read-write, use 'spreadsheets.readonly' if you lack the authorizations

sheet.open('My Sheet', '<GOOGLE SHEET ID>') # store the id in memory for easier use. replace '<GOOGLE SHEET ID>' with the sheet id (easily found in the url=
print(sheet.read('My Sheet', 'Page1!A3:C200')) # example, reading the cells A3 to C200 from the sub sheet 'Page 1'
sheet.write('My Sheet', 'Page2!A2:C3', [['test1', 'test2', 'test3'], ['test4', 'test5', 'test6']]) # write 2 rows with these test strings in the specified range

sheet.close('My Sheet') # remove from memory