
# PID Controller Simulation for Water Level (C++ & Python GUI)

## 🔧 Сборка и установка | Build & Installation

### 1. Скомпилируйте C++ код | Compile the C++ code:

```bash
g++ main.cpp -o Main
```

### 2. Установите необходимые библиотеки Python | Install required Python libraries:

```bash
pip install matplotlib pyserial
```

---

## 🚀 Использование | Usage

1. Запустите Python GUI | Run the Python GUI:

```bash
python GUI.py
```

2. Введите параметры | Enter simulation parameters:

- **Начальная высота воды** | **Initial water level**
- **Желаемая высота воды** | **Target water level**
- **Коэффициенты ПИД-регулятора** (`Kp`, `Ki`, `Kd`)  
  **PID controller coefficients** (`Kp`, `Ki`, `Kd`)

3. Нажмите **"Start Simulation"** для запуска  
   Click **"Start Simulation"** to begin the simulation.

---

## 📁 Структура проекта | Project Structure

- `mainr.cpp` — C++ код для расчета уровня воды с использованием ПИД-регулятора.  
  C++ code for calculating water level using a PID controller.

- `GUI.py` — Python-код для графического интерфейса и визуализации данных.  
  Python GUI for user input and real-time data visualization.

---

## 📊 Пример вывода | Example Output

- **График**: текущий, начальный и целевой уровни воды.  
  **Graph**: displays current, initial, and target water levels.

- **Текстовые метки**: входящий и исходящий потоки воды.  
  **Text labels**: show incoming and outgoing water flow in real time.

---

## 🤝 Вклад | Contributing

Хотите внести вклад в проект?  
Want to contribute to this project?

1. Создайте форк репозитория. | Fork the repository.  
2. Внесите изменения. | Make your changes.  
3. Отправьте pull request. | Submit a pull request.

Мы приветствуем любые улучшения и исправления!  
All improvements and bugfixes are welcome!

---

## 🌐 Язык интерфейса | Interface Language

Интерфейс на английском языке.  
The GUI is in English by default.

