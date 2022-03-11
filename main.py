from network_config import ap, samsung
from picoweb_config import app
import upip
from time import sleep

print('Starting AP')
ap.toggle_ap(True)
print('AP has been started')
ip_adress, netmask, something, dns = ap.show_info()


print('Running PicoWeb')
app.run(debug=True, host=ip_adress)