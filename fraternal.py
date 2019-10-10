import argparse
import colorama
import sys

# from fraternal import __version__
from commands.show import ShowCommand

def main():
    colorama.init()
    
    
    parser = argparse.ArgumentParser(
        description="Compare apks or retrieve information about a single apk.",
        epilog="""example usage:
  Output info about apk:
    \x1b[1mfraternal show -a <apk>\x1b[0m
  For help on a specific command run:
    \x1b[1mfraternal <command> -h\x1b[0m""",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    __version__ = '0.0.1' # temporary, make __init__.py work
    parser.add_argument('--version', action='version', version='fraternal %s' % __version__)

    subparsers = parser.add_subparsers()

    # create the parser for the "rec" command
    parser_show = subparsers.add_parser('show', help='Ouput apk info')
    parser_show.add_argument('-a', '--apk', help='the apk file to analyze')
    parser_show.add_argument('-p', '--perm', help='show the apk permissions only')
    parser_show.add_argument('-s', '--sign', help='show the apk signature details only')
    parser_show.add_argument('-v', '--verbose', help='display detailed information')
    parser_show.set_defaults(cmd=ShowCommand)

    args = parser.parse_args()

    if hasattr(args, 'cmd'):
        command = args.cmd(args)
        code = command.execute()
        sys.exit(code)
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()