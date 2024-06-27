# BailandoConLasAbejas Animations

![Logo](assets/github/bailandoconlasabejas.jpg)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Software](#software-requirements)
- [Project Structure](#project-structure)
- [License](#license)

## Introduction
This repository aims to provide a foundation for anyone interested in what I call "mathnimations" (mathematical animations madee with python) to learn and adopt my best practices. 

It uses Python and takes advantage of the Manim community animation engine.

## Features
- My own manim SubScene structure.
- ManimVoiceover for testing and recording voiceovers.
- ManimML for machine learning animations (Modified by me for full windows compatibility).
- Some custom utilities for producing assets.

## Software Requirements
- Python 3.11 or higher
- Manim Community
- FFMPEG
- LaTeX
- SoX
- CUDA
- All python dependencies in "requirements.txt" (run `pip install -r requirements.txt` to install all) 
(Note: Some dependencies like pytorch require CUDA 12.1. Install them manually if you have another version installed.)
- And a lot of patience :)

## Project Structure
```
BailandoConLasAbejas/
├── assets/
│   ├── github/
│   └── scene1/
├── media/
│   ├── images/
│   └── videos/
├── scenes/
│   ├── scene1.py
│   └── scene2.py
├── utils/
│   ├── bee_extractor.py
│   └── subscene.py
├── .gitignore
├── LICENSE
├── main.py
├── manim.cfg
├── README.md
└── requirements.txt
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---