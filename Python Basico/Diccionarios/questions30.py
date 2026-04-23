employees = [ 
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"}, 
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"}, 
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"}, 
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"}, 
] 
departments = {}
for employee in employees:     
    name = employee.get("name")
    email = employee.get("email")
    department = employee.get("department")

    if department not in departments:
        departments[department] = []

    departments[department].append({
        "name": name, "email": email
    })

print(departments)

