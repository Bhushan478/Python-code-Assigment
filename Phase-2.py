# Advanced Employee Payroll & Tax Management System
# Phase II - Approximately 70% implementation

employees = {}

# Company-defined/demo tax slabs for project implementation.
# These are placeholders and can be replaced by the required tax policy.
TAX_SLABS = [
    (25000, 0.00),
    (50000, 0.05),
    (100000, 0.10),
    (float('inf'), 0.15)
]

PF_RATE = 0.12
PROFESSIONAL_TAX = 200


def calculate_tax(gross):
    """Calculate monthly tax using the project's demo tax slabs."""
    tax = 0
    previous_limit = 0

    for limit, rate in TAX_SLABS:
        taxable_amount = min(gross, limit) - previous_limit
        if taxable_amount > 0:
            tax += taxable_amount * rate
        if gross <= limit:
            break
        previous_limit = limit

    return round(tax, 2)


def calculate_bonus(basic, performance):
    """Return bonus based on performance rating."""
    if performance >= 90:
        return round(basic * 0.15, 2)
    elif performance >= 75:
        return round(basic * 0.10, 2)
    elif performance >= 60:
        return round(basic * 0.05, 2)
    return 0


def calculate_salary(employee):
    """Calculate salary components for one employee."""
    basic = employee["basic"]
    allowances = employee["allowances"]
    bonus = calculate_bonus(basic, employee["performance"])

    gross = basic + allowances + bonus
    pf = basic * PF_RATE
    professional_tax = PROFESSIONAL_TAX if gross > 15000 else 0
    income_tax = calculate_tax(gross)
    total_deductions = pf + professional_tax + income_tax
    net_salary = gross - total_deductions

    return {
        "gross": round(gross, 2),
        "pf": round(pf, 2),
        "professional_tax": round(professional_tax, 2),
        "income_tax": round(income_tax, 2),
        "bonus": round(bonus, 2),
        "total_deductions": round(total_deductions, 2),
        "net_salary": round(net_salary, 2)
    }


def add_employee(emp_id, name, basic, allowances, performance):
    if emp_id in employees:
        print("Employee ID already exists.")
        return

    employees[emp_id] = {
        "name": name,
        "basic": float(basic),
        "allowances": float(allowances),
        "performance": float(performance)
    }
    print("Employee Added Successfully")


def update_employee(emp_id, basic=None, allowances=None, performance=None):
    if emp_id not in employees:
        print("Employee not found.")
        return

    if basic is not None:
        employees[emp_id]["basic"] = float(basic)
    if allowances is not None:
        employees[emp_id]["allowances"] = float(allowances)
    if performance is not None:
        employees[emp_id]["performance"] = float(performance)

    print("Employee Updated Successfully")


def delete_employee(emp_id):
    if emp_id in employees:
        del employees[emp_id]
        print("Employee Record Deleted Successfully")
    else:
        print("Employee not found.")


def generate_salary_slip(emp_id):
    if emp_id not in employees:
        print("Employee not found.")
        return

    employee = employees[emp_id]
    salary = calculate_salary(employee)

    print("\n========== MONTHLY SALARY SLIP ==========")
    print("Employee ID       :", emp_id)
    print("Employee Name     :", employee["name"])
    print("Basic Salary      :", employee["basic"])
    print("Allowances        :", employee["allowances"])
    print("Bonus             :", salary["bonus"])
    print("Gross Salary      :", salary["gross"])
    print("PF (12%)          :", salary["pf"])
    print("Professional Tax  :", salary["professional_tax"])
    print("Income Tax        :", salary["income_tax"])
    print("Total Deductions  :", salary["total_deductions"])
    print("Net Salary        :", salary["net_salary"])
    print("========================================\n")


def search_employee(emp_id):
    if emp_id not in employees:
        print("Employee not found.")
        return

    employee = employees[emp_id]
    print("\nEmployee ID:", emp_id)
    print("Name:", employee["name"])
    print("Basic Salary:", employee["basic"])
    print("Allowances:", employee["allowances"])
    print("Performance:", employee["performance"])
    print("Net Salary:", calculate_salary(employee)["net_salary"])


def payroll_report():
    if not employees:
        print("No employee records available.")
        return

    print("\n=============== PAYROLL REPORT ===============")
    print(f"{'ID':<12}{'Name':<20}{'Gross':>12}{'Net Salary':>15}")
    print("-" * 59)

    for emp_id, employee in employees.items():
        salary = calculate_salary(employee)
        print(f"{emp_id:<12}{employee['name']:<20}"
              f"{salary['gross']:>12.2f}{salary['net_salary']:>15.2f}")


def load_demo_data():
    """Sample records used for demonstration/testing during Phase II."""
    add_employee("EMP1001", "Rahul Sharma", 30000, 8000, 82)
    add_employee("EMP1002", "Priya Deshmukh", 40000, 9000, 91)
    add_employee("EMP1003", "Aman Verma", 26000, 5000, 68)


# -------------------- MAIN PROGRAM --------------------
if __name__ == "__main__":
    load_demo_data()

    while True:
        print("\n===== EMPLOYEE PAYROLL SYSTEM =====")
        print("1. Add Employee")
        print("2. Search Employee")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Generate Salary Slip")
        print("6. Payroll Report")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            emp_id = input("Employee ID: ").strip()
            name = input("Employee Name: ").strip()
            basic = float(input("Basic Salary: "))
            allowances = float(input("Allowances: "))
            performance = float(input("Performance Score (0-100): "))
            add_employee(emp_id, name, basic, allowances, performance)

        elif choice == "2":
            search_employee(input("Enter Employee ID: ").strip())

        elif choice == "3":
            emp_id = input("Employee ID: ").strip()
            basic = input("New Basic (Enter to keep old): ").strip()
            allowances = input("New Allowances (Enter to keep old): ").strip()
            performance = input("New Performance (Enter to keep old): ").strip()
            update_employee(
                emp_id,
                basic=float(basic) if basic else None,
                allowances=float(allowances) if allowances else None,
                performance=float(performance) if performance else None
            )

        elif choice == "4":
            delete_employee(input("Enter Employee ID to delete: ").strip())

        elif choice == "5":
            generate_salary_slip(input("Enter Employee ID: ").strip())

        elif choice == "6":
            payroll_report()

        elif choice == "7":
            print("Thank you for using the Payroll System.")
            break

        else:
            print("Invalid choice. Please try again.")


# Remaining Phase III work:
# 1. Add file/database persistence.
# 2. Add automated test cases and edge-case validation.
# 3. Add stronger exception handling and input validation.
# 4. Refine OOP structure if required by final project design.
# 5. Final deployment and complete documentation/report.
