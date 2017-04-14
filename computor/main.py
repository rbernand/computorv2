from prompt_toolkit import prompt
from computor.parser import Parser


def prompt_command():
    print('>>> ', end='')
    return prompt()


def main():
    parser = Parser()
    try:
        for line in iter(prompt_command, ''):
            root = parser.parse_line(line)
            root.print_tree()
    except (EOFError, KeyboardInterrupt):
        print('exit')


if __name__ == '__main__':
    main()
