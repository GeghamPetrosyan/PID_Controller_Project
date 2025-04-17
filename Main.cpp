#include <iostream>
#include <cmath>
#include <cstdlib> // Для atof
#include <thread> // Для std::this_thread::sleep_for
#include <chrono> // Для std::chrono::milliseconds

// Функция для расчета расхода через слив в зависимости от высоты уровня воды
double calculateOutflow(double height) {
    return std::sqrt(height);
    
}

// Класс для ПИД-регулятора
class PIDController {
public:
    PIDController(double kp, double ki, double kd)
        : kp(kp), ki(ki), kd(kd), prevError(0), integral(0) {}

    double calculate(double setpoint, double measuredValue, double dt) {
        double error = setpoint - measuredValue;
        integral += error * dt;
        double derivative = (error - prevError) / dt;
        prevError = error;
        return kp * error + ki * integral + kd * derivative;
    }

private:
    double kp, ki, kd;
    double prevError;
    double integral;
};

int main(int argc, char* argv[]) {
    if (argc != 6) {
        std::cerr << "Usage: " << argv[0] << " initialHeight desiredHeight kp ki kd" << std::endl;
        return 1;
    }

    double initialHeight = atof(argv[1]);
    double desiredHeight = atof(argv[2]);
    double kp = atof(argv[3]);
    double ki = atof(argv[4]);
    double kd = atof(argv[5]);

    PIDController pid(kp, ki, kd);

    double currentHeight = initialHeight;
    double dt = 0.1;
    double inflow = 0.0;

    while (true) { // Бесконечный цикл
        double outflow = calculateOutflow(currentHeight);
        double controlSignal = pid.calculate(desiredHeight, currentHeight, dt);

        inflow = std::max(0.0, std::min(100.0, controlSignal));

        currentHeight += (inflow - outflow) * dt;

        std::cout << currentHeight << " " << inflow << " " << outflow << std::endl;

        // Задержка для симуляции реального времени
        std::this_thread::sleep_for(std::chrono::milliseconds(10)); // Увеличение задержки
    }

    return 0;
}
