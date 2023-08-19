from sys import version_info, exit


print("If you see this message, it means Python is installed on your system")
print("Let's see which version you have...")

minimum_version = (3, 11)
major_python_version = version_info.major
minor_python_version = version_info.minor
installed_python_version = (major_python_version, minor_python_version)


if installed_python_version >= minimum_version:
    # Make sure to use old style string formatting as we don't know for sure which Python version we're running on
    print("It seems you have Python version %d.%d which is good enough for this course" % (major_python_version, minor_python_version))
else:
    text = [
        'Sadly, Python tells me its version is %d.%d' % (major_python_version, minor_python_version),
        'You need version %d.%d or better' % minimum_version,
        '',
        'This could mean two things:',
        '* You have only this old version installed',
        "* You have a more recent version installed as well as an old one, and it's the old one that's being used to run this script",
        "If you're convinced you have a recent enough version installed, ask a lecturer for help",
        "Otherwise, download and install a more recent version of Python"
    ]

    for line in text:
        print(line)

    print("FAILURE")
    exit(-1)



import subprocess
import re

print("Let's find out if pip is installed...")


try:
    pip_output = subprocess.check_output(["pip", "--version"]).decode('utf-8')
except OSError as e:
    print("Uh oh... I tried running pip but an error occurred")
    print("This is the error: " + str(e))
    print("FAILURE")
    exit(-2)

match = re.search(r'python (\d+)\.(\d+)', pip_output)
if not match:
    print("I found pip but it answered something I don't understand")
    print("This was its response: " + pip_output)
    print("I think you better ask a lecturer for help, I'm at a loss. Very sorry :-(")
    print("FAILURE")
    exit(-3)

major_python_version_according_to_pip, minor_python_version_according_to_pip = map(int, match.groups())
python_version_according_to_pip = (major_python_version_according_to_pip, minor_python_version_according_to_pip)

print("pip is associated with Python version %d.%d" % (major_python_version_according_to_pip, minor_python_version_according_to_pip))

if python_version_according_to_pip != installed_python_version:
    print("There's a mismatch of versions! %s vs %s" % (installed_python_version, python_version_according_to_pip))
    print("Ask a lecturer for help")
    print("FAILURE")
    exit(-4)


print("Your Python installation has been checked and approved!")
print("You can proceed with the instructions")
print("SUCCESS")
