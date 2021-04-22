import pymem
import pymem.process
from ReadWriteMemory import ReadWriteMemory
process=pymem.process
far=pymem.Pymem('farcry3.exe')
far_handle=far.process_handle
base_address=pymem.process.module_from_name(far_handle, "FC3.dll").lpBaseOfDll
offsets=['0x8','0x164','0x0','0x10','0x1DC','0xC','0x10']
static_address=0x01EDC7C4
pointer_static_address=static_address + base_address
rwm=ReadWriteMemory()
process=rwm.get_process_by_name('farcry3.exe')
process.open()
my_pointer=process.get_pointer(pointer_static_address, offsets=offsets)
value=99
process.write(my_pointer,value)