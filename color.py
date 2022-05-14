#!home/pi/onisi/color.py
class colors:
	black="\033[30m"
	red="\033[31m"
	green="\033[32m"
	yellow="\033[33m"
	blue="\033[34m"
	magenta="\033[35m"
	cyan="\033[36m"
	white="\033[37m"
	default="\033[39m"

	bold="\033[1m"
	u_line="\033[4m"
#	marker="\033[7m"
	invisible="\033[08m"

#	reverce="\033[07m"

	bg_black="\033[40m"
	bg_red="\033[41m"
	bg_green="\033[42m"
	bg_yellow="\033[43m"
	bg_blue="\033[44m"
	bg_magenta="\033[45m"
	bg_cyan="\033[46m"
	bg_white="\033[47m"
	bg_default="\033[49m"

	reset="\033[0m"

	_END="\033[0m"
	@classmethod
	def c_print(text,vis,styles=()):
		colored_text=""
		for style in styles :
			colored_text +=style
		colored_text +=vis
		colored_text +=text._END
		print(colored_text)
#mystyle=[colors.marker,colors.u_line,colors.blue]
#colors.c_print("sample",mystyle
	def c_sample():
		colors.c_print("sample",[colors.bg_green,colors.white,colors.bold])
