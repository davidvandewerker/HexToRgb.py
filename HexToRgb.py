import argparse
from argparse import RawTextHelpFormatter
from colors import rgb, hex

parser = argparse.ArgumentParser(
    prog='HexToRgb.py',
    description='Convert Hexadecimal values to RGB values',
    epilog='Related Commands:' + '\n' + 'RgbToHex.py',
    formatter_class=RawTextHelpFormatter
)

parser.add_argument(
    'hex_input',
    help='Hexadecimal value to be converted to RGB'
)

args = parser.parse_args()
hexString = args.hex_input

hexValue = str(hexString).upper()

rgbOutput = tuple(hex(hexString).rgb)
rgbValue = str(rgbOutput)

print('\n' + 'Hex Value: #' + hexValue)
print('RGB Value: rgb'+ rgbValue + '\n')
