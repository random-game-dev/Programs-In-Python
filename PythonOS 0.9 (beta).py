import os
import time
import sys

def boot_sequence():
    print("🐾 Initializing PythonOS v0.9...")
    time.sleep(1)
    print("🔒 Loading ToeBean Kernel...")
    time.sleep(1)
    print("🌐 Connecting to MeowNet...")
    time.sleep(1)
    print(r"""
    ╔═════════════════════════╗
    ║  Welcome to PythonOS!   ║
    ║     😺 ASCII Mode       ║
    ║     🐢 Colotful Mode    ║
    ╚═════════════════════════╝
    """)
    time.sleep(1)

def ascii_mode():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("🐱 Entering ASCII Interface...\n")
    time.sleep(1)
    print(r"""
    (\__/)
    ( •ㅅ•)
    / 　 づ     [PYTHONOS TERMINAL]

    Type 'help', 'launch meowware', or 'exit'
    """)
    while True:
        cmd = input(">:3~$ ").strip().lower()
        if cmd == "exit":
            print("Goodbye, Catministrator.")
            break
        elif cmd == "help":
            print("Available commands: meowloop, snacklog, exit")
        elif cmd == "launch meowware":
            print("Injecting toe beans into memory...")
            time.sleep(1)
            print("Meowware deployed. Corruption level: 99%")
        else:
            print(f"'{cmd}' is not recognized in PythonOS ASCII.")

def colotful_mode():
    try:
        import turtle
        screen = turtle.Screen()
        screen.title("🐢 PythonOS Colotful Mode")
        screen.bgcolor("pink")
        artist = turtle.Turtle()
        artist.shape("turtle")
        artist.color("purple")
        artist.speed(0)

        for _ in range(36):
            artist.circle(100)
            artist.right(10)

        screen.mainloop()
    except ImportError:
        print("Turtle module not available. Try ASCII mode instead.")

boot_sequence()

choice = input("Select mode [ascii/colotful]: ").strip().lower()
if choice == "ascii":
    ascii_mode()
elif choice == "colotful":
    colotful_mode()
else:
    print("Invalid mode selected. Defaulting to ASCII.")
    ascii_mode()