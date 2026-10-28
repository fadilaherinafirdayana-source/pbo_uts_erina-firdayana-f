import json


class Sensor:
    def _init_(self, sensor_id, location, temperature, status, operator_id):
        self.sensor_id = sensor_id
        self.location = location
        self.temperature = temperature
        self.status = status
        self.operator_id = operator_id

    def cek_status(self):
        return self.status

    def tampilkan_data(self):
        print(f"\nID Sensor   : {self.sensor_id}")
        print(f"Lokasi      : {self.location}")
        print(f"Suhu        : {self.temperature} °C")
        print(f"Status      : {self.cek_status()}")
        print(f"Operator ID : {self.operator_id}")


class TemperatureSensor(Sensor):
    def cek_status(self):
        if self.temperature >= 85:
            return "DANGER"
        elif self.temperature >= 65:
            return "WARNING"
        else:
            return "NORMAL"


def main():
    with open("sensor_logs.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    print("=== DATA SENSOR SUHU ===")

    for item in data["sensor_logs"]:
        sensor = TemperatureSensor(
            item["sensor_id"],
            item["location"],
            item["temperature"],
            item["status"],
            item["operator_id"]
        )

        sensor.tampilkan_data()


if __name__ == "__main__":
    main()