import utils
import sys
text = sys.argv[1:]
text_new = "".join(sys.argv[1:])

print(utils.currency_rate(text_new))