 # index dictionary by list of key names

def start_loop():
	print("start")

def close_loop():
	print("close")

def pointer_right():
    print("right")

def pointer_left():
    print("left")

def cell_increment():
    print("increment")

def cell_decrement():
    print("decrement")

def print_byte():
    print("print")

def read_byte():
    print("read")


fndict = {
	"[":start_loop,
	"]":close_loop,
	">":pointer_right,
	"<":pointer_left,
	"+":cell_increment,
	"-":cell_decrement,
	".":print_byte,
	",":read_byte,
}

fndict["insert key here"]()

bf_tape_array = [0,0,0,0,]