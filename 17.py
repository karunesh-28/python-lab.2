'''Develop a time tracking system for employees with classes for employees,
projects, and time entries. Implement methods for logging hours, generating
timesheets, and calculating overtime.'''

from datetime import datetime, timedelta

class Employee:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def log_hours(self, project, hours, date):
        for proj in self.projects:
            if proj.name == project:
                proj.log_time(self, hours, date)
                return
        print(f"Project '{project}' not found for {self.name}.")

    def generate_timesheet(self, start_date, end_date):
        timesheet = f"\nTimesheet for {self.name} ({start_date} to {end_date}):"
        total_hours = 0

        for project in self.projects:
            project_timesheet, project_total_hours = project.generate_project_timesheet(self, start_date, end_date)
            timesheet += project_timesheet
            total_hours += project_total_hours

        timesheet += f"\nTotal Hours: {total_hours}"
        return timesheet

    def calculate_overtime(self, start_date, end_date, standard_hours_per_week):
        total_hours = 0

        for project in self.projects:
            total_hours += project.calculate_project_hours(self, start_date, end_date)

        total_weeks = (end_date - start_date).days / 7
        standard_hours = total_weeks * standard_hours_per_week
        overtime_hours = max(total_hours - standard_hours, 0)

        return overtime_hours


class Project:
    def __init__(self, name):
        self.name = name
        self.time_entries = []

    def log_time(self, employee, hours, date):
        self.time_entries.append((employee, hours, date))

    def generate_project_timesheet(self, employee, start_date, end_date):
        project_timesheet = f"\nProject: {self.name}"
        project_total_hours = 0

        for entry in self.time_entries:
            employee_entry, hours, entry_date = entry
            if employee_entry == employee and start_date <= entry_date <= end_date:
                project_timesheet += f"\n  Date: {entry_date}, Hours: {hours}"
                project_total_hours += hours

        return project_timesheet, project_total_hours

    def calculate_project_hours(self, employee, start_date, end_date):
        total_hours = 0

        for entry in self.time_entries:
            employee_entry, hours, entry_date = entry
            if employee_entry == employee and start_date <= entry_date <= end_date:
                total_hours += hours

        return total_hours


# Take user input for employee details
employee_id = int(input("Enter employee ID: "))
employee_name = input("Enter employee name: ")
employee = Employee(employee_id, employee_name)

# Take user input for project details
project_name = input("Enter project name: ")
project = Project(project_name)
employee.add_project(project)

# Log hours for employees
hours = float(input("Enter the number of hours worked: "))
log_date = datetime.now()
employee.log_hours(project_name, hours, log_date)

# Generate timesheets for employees
start_date = input("Enter start date for timesheet (YYYY-MM-DD): ")
end_date = input("Enter end date for timesheet (YYYY-MM-DD): ")
timesheet = employee.generate_timesheet(datetime.fromisoformat(start_date), datetime.fromisoformat(end_date))
print(timesheet)

# Calculate overtime for employees
standard_hours_per_week = float(input("Enter standard hours per week: "))
overtime = employee.calculate_overtime(datetime.fromisoformat(start_date), datetime.fromisoformat(end_date), standard_hours_per_week)
print(f"\nOvertime for {employee.name}: {overtime} hours")
