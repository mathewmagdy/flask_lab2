class Company:
    _id = 4

    def __init__(self, name, location, business, employees_count):
        self.id = Company._id
        Company._id += 1
        self.name = name
        self.location = location
        self.business = business
        self.employees_count = employees_count

class Job:
    def __init__(self, id, title, description, company_id):
        self.id = id
        self.title = title
        self.description = description
        self.company_id = company_id
