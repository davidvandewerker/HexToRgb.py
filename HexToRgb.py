import argparse
from colors import rgb, hex
from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(
    prog='HexToRgb.py',
    description='convert hexadecimal values to rgb values',
    epilog='related programs: RgbToHex.py',
    formatter_class=RawTextHelpFormatter
)

parser.add_argument(
    'hex_color',
    type=str,
    help='hexadecimal value to be converted to rgb'
)

args = parser.parse_args()

hex_color = args.hex_color.upper()
rgb_color = tuple(hex(hex_color).rgb)

print('\n' + 'hex value:', '\n #' + hex_color + '\n')
print('rgb value:', '\n', 'rgb'+ str(rgb_color), '\n')
