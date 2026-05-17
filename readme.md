# Zombie Game

A fast-paced zombie shooter game built with Python and Pygame. Survive waves of increasingly aggressive zombies while managing your health. How long can you last?

## 🎮 Features

- **Fullscreen gameplay** - Immersive full-screen gaming experience
- **Smooth player animations** - Walking animation cycle with directional rotation
- **Mouse-aim targeting** - Point and click to shoot with a crosshair
- **Sound effects** - Satisfying gunshot audio feedback
- **Health system** - Visual health bar that depletes when touched by zombies
- **Score tracking** - Keep track of zombies eliminated
- **Progressive difficulty** - Zombies get faster with each kill
- **Smooth physics** - Vector-based movement and collision detection

## 📋 Requirements

- Python 3.x
- Pygame

## ⚙️ Installation

1. Install Python if you haven't already
2. Install Pygame:
   ```bash
   pip install pygame
   ```
3. Clone or download this repository
4. Ensure all game assets (PNG images and MP3 sound) are in the same directory as `zombiegame.py`

## 🕹️ How to Play

### Starting the Game
- Run the game: `python zombiegame.py`
- Press **SPACE** to start playing
- Press **ESC** to exit at any time

### Controls
- **W** - Move up
- **A** - Move left  
- **S** - Move down
- **D** - Move right
- **Mouse** - Aim and shoot
- **Left Click** - Fire bullets
- **ESC** - Quit game

### Objective
- Shoot zombies to eliminate them and increase your score
- Avoid collision with zombies - they drain your health
- Survive as long as possible and get the highest score!

## 🎯 Game Mechanics

**Zombies**
- Chase the player toward their position
- Rotate to face the player at all times
- Become faster after each kill
- Deal damage on collision

**Player**
- Can move in all directions with animation feedback
- Rotates to face the mouse cursor
- Fires bullets in the direction of the cursor
- Has a health bar that decreases when touched by zombies
- Game ends when health reaches zero

**Bullets**
- Travel toward mouse position when fired
- Have consistent speed
- Remove themselves from play when they hit a zombie

**Health & Scoring**
- Health bar (green) starts full and decreases on zombie contact
- Score increases by 1 for each zombie killed
- Difficulty increases gradually as zombies move faster

## 📁 Project Structure

```
zombiegame/
├── zombiegame.py          # Main game file
├── readme.md              # This file
├── ground.png             # Background texture
├── player.png             # Player walking animation frames
├── player2.png
├── player3.png
├── player4.png
├── player5.png
├── playershoot.png        # Player shooting pose
├── idle0000.png           # Zombie sprite
├── bullet.png             # Bullet sprite
├── crosshair.png          # Mouse cursor crosshair
└── shootsound.mp3         # Gunshot sound effect
```

## 🖼️ Assets

The game requires the following image and sound files:
- Player sprites (5 walking frames + 1 shooting frame)
- Zombie sprite
- Bullet sprite
- Crosshair cursor
- Ground background texture
- Shoot sound effect (MP3)

## 🚀 Future Enhancements

- Multiple zombie types with different behaviors
- Power-ups (health recovery, rapid fire, etc.)
- Weapon variety
- Level progression system
- High score leaderboard
- Game over screen with stats
- Different difficulty modes

## 🐛 Known Issues

- Asset paths are hardcoded with absolute paths (may need adjustment on different systems)
- Fullscreen mode may need adjustment for different screen resolutions

## 📝 License

This project is open source and available for personal use and modification.

---

**Enjoy the game and survive the zombie apocalypse! 🧟**