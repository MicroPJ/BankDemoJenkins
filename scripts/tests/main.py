#
# 3270 screen scraping using py3270 library
#
import time, datetime, sys
from py3270 import Emulator

delayt = 2	# In sec, slowing down to be able to see the screen update
mylogin = 'SYSAD'
mypass = 'SYSAD'
myhost = '127.0.0.1:5001'
screenrows = []
filename = 'App_Functional_Test_Results_'+datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+'.html'

# use x3270 so you can see what is going on
my3270 = Emulator(visible=True)

# or not (uses s3270)
#my3270 = Emulator()

try:
	# Connect
	print("Connecting to 3270...")
	my3270.connect(myhost)
	my3270.wait_for_field()
	my3270.save_screen(filename)
	time.sleep(delayt)
	print("[TEST #1] my3270.string_found(1,2,'Scrn: BANK10')")
	if not my3270.string_found(1,2,'Scrn: BANK10'):
		sys.exit('Error: '+ print(my3270.string_get(1,2,20)))
	print("[TEST #1] PASSED")
	print("Login...")
	# Login
	my3270.fill_field(10,44,'B0001',5)
	my3270.fill_field(11,44,'123',5)
	my3270.save_screen(filename)
	my3270.send_enter()
	time.sleep(delayt)
	print("[TEST #1] my3270.string_found(1,2,'Scrn: BANK20')")
	if not my3270.string_found(1,2,'zScrn: BANK20'):
		sys.exit('Error: '+ print(my3270.string_get(1,2,20)))
	print("[TEST #2] PASSED")
	my3270.save_screen(filename)
	my3270.exec_command(b"Clear")
	my3270.save_screen(filename)
	time.sleep(delayt)
	my3270.terminate()
except:
  print("Something went wrong!")
  sys.exit(-1)
