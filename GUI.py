import tkinter as tk
from tkinter import ttk
import subprocess
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import threading
import queue

def run_cpp_program(initial_height, desired_height, kp, ki, kd):
    process = subprocess.Popen(
        ['./Main', str(initial_height), str(desired_height), str(kp), str(ki), str(kd)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return process

def update_plot(frame, lines, q, initial_height, desired_height):
    while not q.empty():
        time, height, inflow, outflow = q.get()
        data.append((time, height, inflow, outflow))
    if data:
        times, heights, inflows, outflows = zip(*data)
        lines[0].set_data(times, heights)
        lines[1].set_data(times, [initial_height] * len(times))
        lines[2].set_data(times, [desired_height] * len(times))
        ax.relim()
        ax.autoscale_view()
        ax.set_xlim(0, max(times))
        ax.set_ylim(0, max(max(heights), desired_height) * 1.1)
        
        # Обновление текста для входящего и выходящего потока воды
        inflow_text.set(f"Inflow: {inflows[-1]:.2f} L/s")
        outflow_text.set(f"Outflow: {outflows[-1]:.2f} L/s")
    return lines

def start_simulation():
    initial_height = float(entry_initial_height.get())
    desired_height = float(entry_desired_height.get())
    kp = float(entry_kp.get())
    ki = float(entry_ki.get())
    kd = float(entry_kd.get())

    process = run_cpp_program(initial_height, desired_height, kp, ki, kd)
    q = queue.Queue()

    def read_output():
        time = 0
        while True:
            output = process.stdout.readline().decode().strip()
            if output:
                try:
                    values = output.split()
                    if len(values) == 3:
                        height, inflow, outflow = map(float, values)
                        q.put((time, height, inflow, outflow))
                        time += 0.1  # Увеличение интервала времени
                    else:
                        print(f"Unexpected output format: {output}")
                except ValueError as e:
                    print(f"Error converting output: {e}")

    threading.Thread(target=read_output, daemon=True).start()
    ani = FuncAnimation(fig, update_plot, fargs=(lines, q, initial_height, desired_height), interval=500, cache_frame_data=False)  # Увеличение интервала обновления
    plt.show()

# Создание GUI
root = tk.Tk()
root.title("PID Controller GUI")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Initial Height:").grid(row=0, column=0, sticky=tk.W)
entry_initial_height = ttk.Entry(frame)
entry_initial_height.grid(row=0, column=1)

ttk.Label(frame, text="Desired Height:").grid(row=1, column=0, sticky=tk.W)
entry_desired_height = ttk.Entry(frame)
entry_desired_height.grid(row=1, column=1)

ttk.Label(frame, text="Kp:").grid(row=2, column=0, sticky=tk.W)
entry_kp = ttk.Entry(frame)
entry_kp.grid(row=2, column=1)

ttk.Label(frame, text="Ki:").grid(row=3, column=0, sticky=tk.W)
entry_ki = ttk.Entry(frame)
entry_ki.grid(row=3, column=1)

ttk.Label(frame, text="Kd:").grid(row=4, column=0, sticky=tk.W)
entry_kd = ttk.Entry(frame)
entry_kd.grid(row=4, column=1)

ttk.Button(frame, text="Start Simulation", command=start_simulation).grid(row=5, column=0, columnspan=2)

# Настройка графика
fig, ax = plt.subplots()
lines = [
    ax.plot([], [], lw=2, label='Current Height')[0],
    ax.plot([], [], lw=2, label='Initial Height')[0],
    ax.plot([], [], lw=2, label='Desired Height')[0]
]
ax.set_xlabel('Time (s)')
ax.set_ylabel('Water Level (m)')
ax.legend()

data = []

# Текстовые метки для отображения входящего и выходящего потока воды
inflow_text = tk.StringVar()
outflow_text = tk.StringVar()
ttk.Label(root, textvariable=inflow_text).grid(row=6, column=0, columnspan=2)
ttk.Label(root, textvariable=outflow_text).grid(row=7, column=0, columnspan=2)

root.mainloop()
