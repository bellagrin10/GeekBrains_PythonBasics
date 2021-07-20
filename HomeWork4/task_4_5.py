import utils
import argparse

from task_4_3 import print_info

parser = argparse.ArgumentParser()
parser.add_argument('--currency_code', type=str, default=None)
args = parser.parse_args()
if args.currency_code:
    print_info(utils.currency_rates(args.currency_code))
else:
    print_info(utils.currency_rates('USD'))
    print_info(utils.currency_rates('usd'))
    print_info(utils.currency_rates('EUR'))
    print_info(utils.currency_rates('YYY'))
