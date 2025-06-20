class StaffManager:
    def __init__(self):
        self.staff_list = []

    def add_staff(self, staff_id, staff_name, staff_salary):
        self.staff_list.append({"id": staff_id, "name": staff_name, "salary": staff_salary})
        print(f"Staff {staff_name} added.")

    def get_staff(self, staff_id):
        for staff in self.staff_list:
            if staff["id"] == staff_id:
                return staff
        return f"No staff found with ID {staff_id}"

    def get_high_earners(self, salary_limit):
        return [s for s in self.staff_list if s["salary"] > salary_limit]

# Usage
manager = StaffManager()
manager.add_staff(1, "dhivya", 50000)
manager.add_staff(2, "Bala", 60000)
manager.add_staff(3, "Vishnu", 40000)

print(manager.get_staff(2))
print(manager.get_high_earners(45000))
