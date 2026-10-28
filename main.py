import json


class Employee:
    def __init__(self, emp_id, name, base_salary, bonus_code):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary
        self.bonus_code = bonus_code

    def hitung_gaji(self):
        return self.base_salary


class KaryawanTetap(Employee):
    def __init__(self, emp_id, name, base_salary, bonus_code):
        super().__init__(emp_id, name, base_salary, bonus_code)

    def hitung_gaji(self):
        return self.base_salary


class KaryawanKontrak(Employee):
    def __init__(self, emp_id, name, base_salary, bonus_code):
        super().__init__(emp_id, name, base_salary, bonus_code)

    def hitung_gaji(self):
        return self.base_salary


def main():
    with open("employee.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    print("=== DATA GAJI KARYAWAN ===")

    for item in data["employees"]:
        if item["is_permanent"]:
            karyawan = KaryawanTetap(
                item["emp_id"],
                item["name"],
                item["base_salary"],
                item["bonus_code"]
            )
            status = "Tetap"
        else:
            karyawan = KaryawanKontrak(
                item["emp_id"],
                item["name"],
                item["base_salary"],
                item["bonus_code"]
            )
            status = "Kontrak"

        gaji = karyawan.hitung_gaji()

        print(f"\nID     : {karyawan.emp_id}")
        print(f"Nama   : {karyawan.name}")
        print(f"Status : {status}")
        print(f"Gaji   : Rp{gaji:,.0f}")


if __name__ == "__main__":
    main()