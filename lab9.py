from abc import ABC, abstractmethod


# Visitor Interface
class Visitor(ABC):
    @abstractmethod
    def visit_company(self, company: 'Company') -> dict[str, float]: ...

    @abstractmethod
    def visit_department(self, department: 'Department') -> dict[str, float]: ...

    @abstractmethod
    def visit_employee(self, employee: 'Employee') -> dict[str, float]: ...


# Element Interface
class Element(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor) -> dict[str, float]: ...


# Employee class
class Employee(Element):
    def __init__(self, name: str, position: str, salary: float):
        self.name = name
        self.position = position
        self.salary = salary

    def accept(self, visitor: Visitor) -> dict[str, float]:
        return visitor.visit_employee(self)


# Department class
class Department(Element):
    def __init__(self, name: str, employees: list[Employee]):
        self.name = name
        self.employees = employees

    def accept(self, visitor: Visitor) -> dict[str, float]:
        return visitor.visit_department(self)


# Company class
class Company(Element):
    def __init__(self, name: str, departments: list[Department]):
        self.name = name
        self.departments = departments

    def accept(self, visitor: Visitor) -> dict[str, float]:
        return visitor.visit_company(self)


# Concrete Visitor class to generate the Salary Statement Report
class SalaryReportVisitor(Visitor):
    def visit_company(self, company: Company) -> dict[str, float]:
        report = {}
        total_salary = 0
        for department in company.departments:
            dept_report = department.accept(self)
            total_salary += sum(dept_report.values())
            report.update(dept_report)
        report['Total Company Salary'] = total_salary
        return report

    def visit_department(self, department: Department) -> dict[str, float]:
        report = {}
        total_salary = 0
        for employee in department.employees:
            emp_report = employee.accept(self)
            total_salary += emp_report[employee.name]
            report.update(emp_report)
        report[f'Total Salary for Department {department.name}'] = total_salary
        return report

    def visit_employee(self, employee: Employee) -> dict[str, float]:
        return {employee.name: employee.salary}


if __name__ == '__main__':
    emp1 = Employee('Alice', 'Engineer', 70000)
    emp2 = Employee('Bob', 'Manager', 80000)
    emp3 = Employee('Charlie', 'Technician', 50000)

    dept1 = Department('Engineering', [emp1])
    dept2 = Department('Management', [emp2, emp3])

    company = Company('TechCorp', [dept1, dept2])

    salary_report_visitor = SalaryReportVisitor()

    print('Company Salary Report:')
    company_report = company.accept(salary_report_visitor)
    print(company_report)

    print('\nDepartment Salary Report (Engineering):')
    dept_report = dept1.accept(salary_report_visitor)
    print(dept_report)

    print('\nDepartment Salary Report (Management):')
    dept_report = dept2.accept(salary_report_visitor)
    print(dept_report)
