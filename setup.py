import pip

def install(package):
	pip.main(['install', package])

install('sys')
install('pyperclip')
install('youtube-dl')