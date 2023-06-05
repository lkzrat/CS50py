import pyfiglet as fig
import sys

def main():
    print('Output:\n', txtfig(str(input('Input: '))))

def txtfig(string):
    if len(sys.argv) > 1:
        if bool(sys.argv[1] in ('-f', '--font')) == False:
            sys.exit('Invalid command')
        else:
            try:
                return fig.figlet_format(string, font = str(sys.argv[2]))
            except IndexError:
                sys.exit('Missing font')
            except Exception:
                sys.exit('Invalid font')
    else:
        return fig.figlet_format(string)

txtfig('test')
main()