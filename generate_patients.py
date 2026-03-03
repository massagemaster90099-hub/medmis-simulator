import json
import random
from datetime import datetime, timedelta

# === КОНФИГУРАЦИЯ ===
NUM_PATIENTS = 20

# ⚠️ РАЗДЕЛЕНО ПО ПОЛУ — НЕ МЕНЯТЬ!
MALE_FIRST_NAMES = ["Иван", "Петр", "Сергей", "Алексей", "Дмитрий", "Андрей", "Николай", "Владимир", "Александр", "Михаил"]
FEMALE_FIRST_NAMES = ["Анна", "Елена", "Ольга", "Наталья", "Мария", "Екатерина", "Татьяна", "Светлана", "Ирина", "Юлия"]

MALE_PATRONYMICS = ["Иванович", "Петрович", "Сергеевич", "Алексеевич", "Дмитриевич", "Андреевич", "Николаевич", "Владимирович", "Александрович", "Михайлович"]
FEMALE_PATRONYMICS = ["Ивановна", "Петровна", "Сергеевна", "Алексеевна", "Дмитриевна", "Андреевна", "Николаевна", "Владимировна", "Александровна", "Михайловна"]

LAST_NAMES_MALE = ["Иванов", "Петров", "Сидоров", "Смирнов", "Кузнецов", "Попов", "Васильев", "Михайлов", "Новиков", "Федоров"]
LAST_NAMES_FEMALE = ["Иванова", "Петрова", "Сидорова", "Смирнова", "Кузнецова", "Попова", "Васильева", "Михайлова", "Новикова", "Федорова"]

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

def generate_patient(index, sex):
    """Генерирует пациента с корректным согласованием пола"""
    
    # ⚠️ КЛЮЧЕВОЙ МОМЕНТ — ВЫБОР ПО ПОЛУ
    if sex == "М":
        first_name = random.choice(MALE_FIRST_NAMES)
        patronymic = random.choice(MALE_PATRONYMICS)
        last_name = random.choice(LAST_NAMES_MALE)
    else:  # sex == "Ж"
        first_name = random.choice(FEMALE_FIRST_NAMES)
        patronymic = random.choice(FEMALE_PATRONYMICS)
        last_name = random.choice(LAST_NAMES_FEMALE)
    
    return {
        "id": generate_patient_id(index),
        "last_name": last_name,
        "first_name": first_name,
        "patronymic": patronymic,
        "date_of_birth": generate_date_of_birth(),
        "sex": sex,
        "complaint": random.choice(COMPLAINTS),
        "diagnosis": random.choice(DIAGNOSES),
        "allergy": random.choice(ALLERGIES),
        "treatment": random.choice(TREATMENTS),
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "is_synthetic": True
    }

def main():
    patients = []
    
    for i in range(1, NUM_PATIENTS + 1):
        sex = random.choice(["М", "Ж"])
        patient = generate_patient(i, sex)
        patients.append(patient)
    
    with open('patients.json', 'w', encoding='utf-8') as f:
        json.dump(patients, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Готово! Сгенерировано {NUM_PATIENTS} пациентов.")
    print("📄 Файл: patients.json")
    print("🔒 Все данные синтетические (152-ФЗ соблюдён)")
    print("⚠️ Пол согласован с фамилией и отчеством")
    
    # === ПРОВЕРКА ПЕРВЫХ 5 ПАЦИЕНТОВ ===
    print("\n📋 Проверка первых 5 пациентов:")
    for p in patients[:5]:
        print(f"  {p['last_name']} {p['first_name']} {p['patronymic']} | Пол: {p['sex']}")

if __name__ == "__main__":
    main()