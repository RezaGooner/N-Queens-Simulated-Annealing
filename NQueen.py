import tkinter as tk
import random
import math
import time  


# -------------------------------
# Simulated Annealing Algorithm
# -------------------------------

class SimulatedAnnealingSolver:
    def __init__(self, n, canvas, speed_var, pause_var):
        self.n = n
        self.canvas = canvas
        self.speed_var = speed_var  # Speed variable for adjustable delay
        self.pause_var = pause_var  # Pause flag to control pausing and resuming
        self.board = list(range(n))
        random.shuffle(self.board)
        self.current_energy = self.calculate_energy(self.board)
        self.T = 100  # Initial temperature
        self.T_min = 0.01  # Minimum temperature
        self.alpha = 0.95  # Cooling rate
        self.iterations = 100  # Attempts per temperature
        self.step = 0
        self.start_time = time.time()  # set start time


    def calculate_energy(self, board):
        conflicts = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if abs(board[i] - board[j]) == abs(i - j):  # Check diagonal conflicts
                    conflicts += 1
        return conflicts

    def generate_new_state(self, board):
        new_board = board[:]
        row1, row2 = random.sample(range(self.n), 2)
        new_board[row1], new_board[row2] = new_board[row2], new_board[row1]
        return new_board

    def solve_step(self):
        # Pause the algorithm if pause flag is set
        if self.pause_var.get():
            return

        if self.T <= self.T_min:
            print("Solution Found:", self.board)
            elapsed_time = time.time() - self.start_time  #elapsed time
            print(f"Time Taken: {elapsed_time:.2f} seconds")
            return  # Finish the process

        if self.step == self.iterations:
            self.T *= self.alpha  # Reduce temperature
            self.step = 0

        new_board = self.generate_new_state(self.board)
        new_energy = self.calculate_energy(new_board)

        if new_energy < self.current_energy or random.random() < math.exp(-(new_energy - self.current_energy) / self.T):
            self.board = new_board
            self.current_energy = new_energy

        self.step += 1

        # Update GUI board
        draw_board(self.canvas, self.board, self.n)
        self.canvas.update()

        if self.current_energy == 0:
            print("Solution Found:", self.board)
            elapsed_time = time.time() - self.start_time  # elapsed time
            print(f"Time Taken: {elapsed_time:.2f} seconds")
            return  # Finish the process

        # Schedule the next step with adjustable delay based on slider value
        delay = self.speed_var.get()  # Get the current delay value from slider
        self.canvas.after(delay, self.solve_step)


# -------------------------------
# GUI Functions
# -------------------------------
def draw_board(canvas, board, n):
    canvas.delete("all")
    cell_size = 40
    for i in range(n):
        for j in range(n):
            color = "white" if (i + j) % 2 == 0 else "gray"
            canvas.create_rectangle(j * cell_size, i * cell_size, (j + 1) * cell_size, (i + 1) * cell_size, fill=color)

    for row, col in enumerate(board):
        x = col * cell_size + cell_size // 2
        y = row * cell_size + cell_size // 2
        canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="red")

def start_solver():
    global solver  # Declare solver as a global variable to access it in other functions
    n = int(entry_n.get())
    canvas.config(width=n * 40, height=n * 40)
    solver = SimulatedAnnealingSolver(n, canvas, speed_slider, pause_var)  # Initialize solver
    solver.solve_step()

def pause_solver():
    pause_var.set(True)  # Set the pause flag to True to stop the algorithm

def resume_solver():
    if solver:  # Check if solver is initialized
        pause_var.set(False)  # Set the pause flag to False to resume the algorithm
        solver.solve_step()  # Continue solving from where it was paused

# -------------------------------
# Main GUI
# -------------------------------
root = tk.Tk()
root.title("N-Queens(Simulated Annealing)")

frame = tk.Frame(root)
frame.pack()

label_n = tk.Label(frame, text="Enter N:")
label_n.pack(side=tk.LEFT)

entry_n = tk.Entry(frame, width=5)
entry_n.pack(side=tk.LEFT)

button_solve = tk.Button(frame, text="Solve", command=start_solver)
button_solve.pack(side=tk.LEFT)

# Add a Slider for Speed Adjustment
label_speed = tk.Label(frame, text="Speed (ms per step):")
label_speed.pack(side=tk.LEFT)

speed_slider = tk.Scale(frame, from_=10, to_=3000, orient=tk.HORIZONTAL)
speed_slider.set(100)  # Default value for speed
speed_slider.pack(side=tk.LEFT)

# Pause and Resume functionality
pause_var = tk.BooleanVar(value=False)  # Pause flag

button_pause = tk.Button(frame, text="Pause", command=pause_solver)
button_pause.pack(side=tk.LEFT)

button_resume = tk.Button(frame, text="Resume", command=resume_solver)
button_resume.pack(side=tk.LEFT)

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

root.mainloop()
