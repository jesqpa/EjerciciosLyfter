import csv

def extract_csv(path): 
	csvText = ""
	with open(path, 'r', encoding='utf-8' ) as file: 
		reader = csv.DictReader(file)		
		for row in reader:			
			csvText = str(row)
			keys = row.keys()
			for key in keys:
				print( key.capitalize() + ": " + row[key] )
					
		
	return csvText


extract_csv('video_games.csv')

