from pyfiglet import Figlet
import gettext


def solve(a, b):
    if a == 0:
        return None
    return -b / a

if __name__ == '__main__':
    translation = gettext.translation('solve_line', 'po', fallback=True)
    _ = translation.gettext
    a = float(input())
    b = float(input())
    res = solve(a, b)
    if res is None:
        if b != 0:
            print(Figlet(font='graceful').renderText(_('NO ROOTS')))
        else:
            print(Figlet(font='graceful').renderText(_('(-INF, +INF)')))
    else:
        text = _('Root: {}').format(res)
        print(Figlet(font='graceful').renderText(text))