import base64

def decode_base64(msg):
	message_bytes = msg.encode('ascii')
	base64_bytes = base64.b64decode(message_bytes)
	return base64_bytes.decode('ascii')
