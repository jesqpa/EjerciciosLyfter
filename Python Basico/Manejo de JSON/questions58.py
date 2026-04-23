import json

def extract_json(path): 
	json_text = ""
	with open(path, 'r', encoding='utf-8' ) as file: 
		for line in file.readlines(): 			
			text = line.strip()	
			json_text += text	
	return json.loads(json_text)

data = extract_json('data.json')

data["city"] = "New York"


def write_to_file(path, text):  
    with open(path, 'a', encoding='utf-8' ) as file: 
        file.write(text+'\n')

write_to_file('data_new.json', json.dumps(data, indent=4))

