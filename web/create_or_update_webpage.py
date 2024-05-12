from bitmath import Byte
import psutil,time,sys

def retrieve_device_details():
	return {
		"cpu_count": psutil.cpu_count(),
		"cpu_used": psutil.cpu_percent(interval=1),
		"ram_size": round(float(Byte(psutil.virtual_memory().total).to_GiB()), 1),
		"ram_used": psutil.virtual_memory().percent,
		"disk_size": round(float(Byte(psutil.disk_usage("C:").total).to_GiB()), 1),
		"disk_used": psutil.disk_usage("C:").percent,
		"ip": psutil.net_if_addrs()["Wi-Fi"][1].address,
	}


def read_html_code():
	return open("index_tmp.html", "r+").read()


def update_html_code(device_details, html_code):
	for key in device_details.keys():
		html_code = html_code.replace(str(key), str(device_details[key]))
	return html_code


def write_html_code(updated_html_code):
	html_file = open("index.html", "w")
	html_file.write(updated_html_code)
	html_file.close()


def main():
	print("Monitoring started...")
	while True:
		device_details = retrieve_device_details()
		html_code = read_html_code()
		updated_html_code = update_html_code(device_details, html_code)
		write_html_code(updated_html_code)
		time.sleep(2)
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("Interrupted. Exiting...")
		sys.exit(0)