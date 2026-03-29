# Timmy
Timmy - Technically Intelligent Miniature Manly Youth 

# Requirements

DISCLAIMER - ATM, this is just a pretty much GUI/CLI interface built using python, do not worry, Timmy's own spice will be added when the time is right.

Your computer should meet the following (estimated) minimum requirements - 

**Operating system** - Any modern OS that can comprehend the specs given. 

**RAM** - 4GB available for text tasks (10GB available for Vision Tasks).

**CPU** - Dual Core, more than 2 ghz for text, Quad/Hexa Core, atleast 3-4Ghz for vision.

This *can* work on a Raspberry PI, (4 and 8GB variants, Gen4 or Gen5 recommended.) but it will be *slow*.

**Dedicated GPU is recommended, follow Ollama's instructions to download AMD and Nvidia CUDA support. This is required for Vision based tasks.**

Ollama does not support NPUs found on modern Copilot+ PCs, AI branded chipsets and Raspberry Pi AI addons (afaik).

# Installation

Install Ollama from its website.

Install Python by following the necessary steps for your operating system.

Install Llama 3.2 (support for vision models and other models in general coming soon)

```
ollama install llama3.2
```

# Welcome to the main branch! 

This is where i will push mostly stable updates.

# Changelog V4.5M (Version 4.5 Main) (this is a weird release to be frank)

Audio Support added, i think? Linux users may have varied mileage, but it works flawlessly-ish on Windows. Also the files are seperated and a config made for Timmy.

# Known Issues 

Goofy audio support due to something going on with my own system, so i dont guarantee anything. You also need to execute the program with main.py being in and being called by a terminal in the same directory as config.json otherwise the program wont see anything.

# Plans for the future 

1. Make this into a single executable.
2. Internet Access using a (hopefully) clever solution i am developing.
3. Vision support, but also use deepseek r1 as the default model. its just, way better than Llama.
5. GUI is in development, using PyQT (tkinter is absolute dogwater compared to this)
6. Make an installer script to download everything, but making it download Ollama *might* go into some legal trouble territory.
7. Deep integration with the operating system to make a kind of Copilot copy but for Linux.
