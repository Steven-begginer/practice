from pyfiglet import Figlet
import sys

if len(sys.argv) == 1:
    x = input("Input: ")
    figlet = Figlet()
    print(figlet.renderText(x))
elif len(sys.argv) == 2:
    sys.exit("Invalid usage")
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        font_name = sys.argv[2]
        figlet = Figlet()
        if font_name not in figlet.getFonts():
            sys.exit("Invalid usage")
        x = input("Input: ")
        figlet.setFont(font=font_name)
        print(figlet.renderText(x))
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Usage: python figlet.py <text> or python figlet.py -f <fontname> <text>")

