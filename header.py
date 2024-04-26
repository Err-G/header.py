import os
import re
import sys
import time

asciiart = [
"        :::      ::::::::",
"      :+:      :+:    :+:",
"    +:+ +:+         +:+  ",
"  +#+  +:+       +#+     ",
"+#+#+#+#+#+   +#+        ",
"     #+#    #+#          ",
"    ###   ########.fr    "]

start = '#'
end = '#'
fill = '*'
length = 80
margin = 5

types = {
'.c$|.h$|.cc$|.hh$|.cpp$|.hpp$|.php': ['/*', '*/', '*'],
'.htm$|.html$|.xml$': ['<!--', '-->', '*'],
'.js$': ['//', '//', '*'],
'.tex$': ['%', '%', '*'],
'.ml$|.mli$|.mll$|.mly$': ['(*', '*)', '*'],
'.vim$|vimrc$': ['"', '"', '*'],
'.el$|emacs$': [';', ';', '*'],
'.f90$|.f95$|.f03$|.f$|.for$': ['!', '!', '/']}

def filetype(filename):
    global start, end, fill
    start, end, fill = '#', '#', '*'
    for type, values in types.items():
        if re.search(type, filename):
            start, end, fill = values
            break

def ascii(n):
    return asciiart[n - 3]

def textline(left, right):
    left = left[:length - margin * 2 - len(right)]
    return start + ' ' * (margin - len(start)) + left + ' ' * (length - margin * 2 - len(left) - len(right)) + right + ' ' * (margin - len(end)) + end

def line(n):
    if n == 1 or n == 11:  # top and bottom line
        return start + ' ' + fill * (length - len(start) - len(end) - 2) + ' ' + end
    elif n == 2 or n == 10:  # blank line
        return textline('', '')
    elif n in [3, 5, 7]:  # empty with ascii
        return textline('', ascii(n))
    elif n == 4:  # filename
        return textline(filename(), ascii(n))
    elif n == 6:  # author
        return textline("By: " + user() + " <" + mail() + ">", ascii(n))
    elif n == 8:  # created
        return textline("Created: " + date() + " by " + user(), ascii(n))
    elif n == 9:  # updated
        return textline("Updated: " + date() + " by " + user(), ascii(n))

def user():
    return os.getenv('USER', 'marvin')

def mail():
    return os.getenv('MAIL', 'marvin@42.fr')

def filename():
    return sys.argv[1] if len(sys.argv) > 1 else os.path.basename(__file__)
#    return os.path.basename(__file__)

def date():
    return time.strftime("%Y/%m/%d %H:%M:%S")

def insert():
    lines = []
    for i in range(1, 12):
        lines.append(line(i))
    return lines

def update():
    filetype(filename())
    return insert()

if __name__ == "__main__":
    print("\n".join(update()))
