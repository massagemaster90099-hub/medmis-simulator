import json
import random
from datetime import datetime, timedelta

# --- КОНФИГУРАЦИЯ ---
NUM_PATIENTS = 20  # Количество пациентов

# Синтетические данные (никаких реальных совпадений)
FIRST_NAMES = ["Иван", "Петр", "Сергей", "Алексей", "Дмитрий", 
               "Анна", "Елена", "Ольга", "Наталья", "Мария"]
LAST_NAMES = ["Иванов", "Петров", "Сидоров", "Смирнов", "Кузнецов", 
              "Попов", "Васильев", "Михайлов", "Новиков", "Федоров"]
PATRONYMICS = ["Иванович", "Петрович", "Сергеевич", "Алексеевич", "Дмитриевич", 
               "Ивановна", "Петровна", "Сергеевна", "Алексеевна", "Дмитриевна"]

COMPLAINTS = [
    "Головная боль, головокружение",
    "Боль в грудной клетке при вдохе",
    "Повышение температуры до 38.5°C",
    "Тошнота, рвота, боль в эпигастрии",
    "Одышка при физической нагрузке",
    "Боль в поясничной области",
    "Кашель сухой, навязчивый",
    "Слабость, повышенная утомляемость"
]

DIAGNOSES = [
    "J06.9 - Острая инфекция верхних дыхательных путей",
    "K29.7 - Гастрит неуточнённый",
    "I10 - Эссенциальная гипертензия",
    "J18.9 - Пневмония неуточнённая",
    "M54.5 - Боль в поясничной области",
    "R51 - Головная боль",
    "K35.8 - Острый аппендицит",
    "I20.0 - Нестабильная стенокардия"
]

ALLERGIES = ["Нет", "Пенициллин", "Аспирин", "Латекс", "Йод", "Сульфаниламиды"]
TREATMENTS = [
    "Постельный режим, обильное питьё",
    "Парацетамол 500мг при температуре >38°C",
    "ОАК, ОАМ, ЭКГ",
    "Консультация терапевта",
    "Госпитализация в отделение терапии",
    "Амоксициллин 500мг 3 раза в день 7 дней"
]

def generate_date_of_birth(min_age=18, max_age=80):
    today = datetime.now()
    age = random.randint(min_age, max_age)
    days_offset = random.randint(0, 365)
    dob = today - timedelta(days=age*365 + days_offset)
    return dob.strftime("%d.%m.%Y")

def generate_patient_id(index):
    return f"P{index:04d}"

def main():
    patients = []
    
    for i in range(1, NUM_PATIENTS + 1):
        patient = {
            "id": generate_patient_id(i),
            "last_name": random.choice(LAST_NAMES),
            "first_name": random.choice(FIRST_NAMES),
            "patronymic": random.choice(PATRONYMICS),
            "date_of_birth": generate_date_of_birth(),
            "sex": random.choice(["М", "Ж"]),
            "complaint": random.choice(COMPLAINTS),
            "diagnosis": random.choice(DIAGNOSES),
            "allergy": random.choice(ALLERGIES),
            "treatment": random.choice(TREATMENTS),
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "is_synthetic": True
        }
        patients.append(patient)
    
    with open('patients.json', 'w', encoding='utf-8') as f:
        json.dump(patients, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Готово! Сгенерировано {NUM_PATIENTS} пациентов.")
    print("📄 Файл: patients.json")
    print("🔒 Все данные синтетические (152-ФЗ соблюдён)")

if __name__ == "__main__":
    main()
