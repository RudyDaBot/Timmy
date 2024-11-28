# Timmy
Timmy - Technically Intelligent Miniature Manly Youth 

# Requirements

DISCLAIMER - I can only guarantee Linux support. Some commands have Linux Terminal calls that may not be the same on Windows or MacOS.

Your computer should meet the following (estimated) minimum requirements - 

**Operating system** - Any modern OS that can comprehend the specs given. 

**RAM** - 4GB available for text tasks (10GB available for Vision Tasks).

**CPU** - Dual Core, more than 2 ghz for text, Quad/Hexa Code, atleast 3-4Ghz for vision.

This can work on a Raspberry PI, (4 and 8GB variants, Gen4 or Gen5 recommended.) but vision tasks will most probably fail.

**Dedicated GPU is recommended, follow Ollama's instructions to download AMD and Nvidia CUDA support. This is required for Vision based tasks.**

Ollama does not support NPUs found on modern Copilot+ PCs, AI branded chipsets and Raspberry Pi AI addons (afaik).

# Installation

Install Ollama from its website.

Install Python by following the necessary steps for your operating system.

Install Llama 3.2 (support for vision models and other models in general coming soon)

```
ollama install llama3.2
```

# Welcome to the canary branch! 

This is where i will push each and every update i make to TIMMY.

# Changelog V4C (Version 4 Canary)

Big GigaChad move. Timmy now runs on Llama3.2. This allows for FAR more natural responses. However, audio support is being added later.

# Known Issues 

You must wait for the entire response to be generated. This is because with streaming responsed i.e. seeing the response as its being generated, i cannot, for the life of me, figure out how to add context support (the model remembering the conversation).

# Plans for the future 

1. Compile the program to run on a singe Windows/Linux executable. I do not have the means to compile MacOS executables.
2. Internet Access using a (hopefully) clever solution i am developing.
3. Add support for vision based models. Llama3.2-vision is not being used because, well, my system is not powerful enough to run it.
4. Add Voice recognition and text-to-speech support.
5. Make a nice GUI, but be advised, only expect this feature for wayland for the time being.
