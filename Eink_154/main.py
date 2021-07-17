import serial
import time
from dora import IMAGE_BLACK, IMAGE_RED

ser = serial.Serial('/dev/ttyS0', '230400', timeout=0.1)
#------------------------------
#------------------------------
def serial_send_data(buf):
	while True:
		if ser.out_waiting == 0:
			break
	cnt=0
	for b in buf:
		ser.write( [b] )
		if 0==(cnt%76):
			time.sleep(70/1000.0)
		cnt=cnt+1

#------------------------------
#------------------------------
def write_image_picture():
	serial_send_data(IMAGE_BLACK)
	print("Black transmitted")
	time.sleep(70/1000.0)

	serial_send_data(IMAGE_RED)
	print("Red transmitted")
	ser.flush()

#------------------------------
#------------------------------
def send_begin():
	print(ser.write('a'))

	while True:
		str1=str(ser.read(1))
		if(str1=='b'):
			print(str1)
			break
		else:
			if(str1<255):
				print(str1)
		time.sleep(0.1)
	print("Enter write_image_picture()")
	write_image_picture()

send_begin()
ser.close()
