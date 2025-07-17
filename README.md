### 🕹️ Atari Pong – Python Edition

A simple recreation of the classic **Atari Pong** game using Python and the Pygame library.

This version allows a single player to compete against a basic AI-controlled paddle. The game features score tracking, collision detection, and smooth paddle and ball animation—all inside a resizable window.

---

### 🎮 Features

- Classic Pong gameplay
- CPU-controlled opponent with basic tracking AI
- Real-time ball physics and paddle collision
- Scorekeeping for both players
- Smooth animations and frame rate control
- Customizable screen dimensions
- Easy-to-understand Python code for beginners

---

### 🛠️ Requirements

- Python 3.x
- Pygame library

Install Pygame with:

```bash
pip install pygame
```
### 🚀 How to Run the Game
Clone this repository or download the Python file.

Make sure you have Python and Pygame installed.

Run the game:

```bash
python pong.py
```
Use the Up and Down arrow keys to control your paddle.

### 🎨 Gameplay Controls
Action	Key
Move Paddle Up	⬆️ Arrow Up
Move Paddle Down	⬇️ Arrow Down
Quit Game	Close Window

### 🧠 How It Works
Ball Movement: The ball moves diagonally and bounces off the top and bottom screen boundaries.

Scoring: Points are awarded when the opponent misses the ball.

Collision Detection: Ball bounces off the paddles on collision.

CPU Movement: The CPU paddle follows the ball’s Y-position using a fixed speed.

### 🧾 Code Structure
reset_ball(): Centers the ball and reverses direction.

point_won(winner): Increments player or CPU score.

animate_ball(): Moves the ball and checks for collision/score.

animate_player(): Updates the player's paddle based on key input.

animate_cpu(): AI logic for following the ball.

Main Game Loop: Handles user input, updates positions, renders the screen, and maintains frame rate.

### 📸 Screenshot

<img width="1919" height="1006" alt="image" src="https://github.com/user-attachments/assets/50722105-c925-44c7-b89c-ab1edbec1684" />





### 🙌 Credits
Inspired by the original Atari Pong (1972)
