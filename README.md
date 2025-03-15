# N-Queens Solver using Simulated Annealing

This project provides a Python implementation of the **N-Queens problem** solved using the **Simulated Annealing** algorithm. It includes an interactive GUI built with **Tkinter** that allows you to visualize the solving process in real-time, adjust the speed of the algorithm, and pause/resume the solver at any point.

![flowchart](https://github.com/user-attachments/assets/50cb96bc-341a-4d8a-8360-e5e193de2f29)

---

## Features
- **Simulated Annealing Algorithm**: Efficiently solves the N-Queens problem using a probabilistic optimization approach.
- **Interactive GUI**: Real-time visualization of the board and algorithm progress.
- **Speed Control**: Adjust the speed of the solver using a slider.
- **Pause/Resume Functionality**: Pause the solver at any time and resume from where it left off.
- **Dynamic Board Size**: Solve the N-Queens problem for any value of N.

---

## How to Use
1. Enter the value of **N** (e.g., 8 for the classic 8-Queens problem).
2. Click **Solve** to start the solver.
3. Use the **Speed Slider** to control the speed of the algorithm.
4. Use the **Pause** and **Resume** buttons to control the solver.

---

## Requirements
- Python 3.x
- Tkinter (usually comes pre-installed with Python)

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/N-Queens-Simulated-Annealing.git


2.Navigate to the project directory:

```bash
  cd N-Queens-Simulated-Annealing
```
3. Run the script:

```bash
python NQueen.py
```

---

## Screenshots

![image](https://github.com/user-attachments/assets/75b38afe-f769-4e76-b94a-450845074c51)
> Simulation with 8 Queens

---

## How It Works
1. Simulated Annealing: The algorithm starts with a random board configuration and iteratively improves it by swapping queens. It accepts worse solutions with a certain probability to avoid getting stuck in local optima.

2. Energy Calculation: The "energy" of a board is calculated based on the number of conflicts (queens attacking each other diagonally). The goal is to reduce this energy to zero.

3. Cooling Schedule: The temperature decreases over time, reducing the probability of accepting worse solutions as the algorithm progresses.

---

## Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments
1. Simulated Annealing: Inspired by the optimization algorithm used in various problem-solving domains.

2. Tkinter: Used for creating the interactive GUI.


---

[RezaGooner](https://github.com/RezaGooner)
> Best regard
