from nodepy import events

emitter = events.EventEmitter()

def msgHandler1(msg):
    print("Handler 1 says: " + msg)

def onceHandler(msg):
    print("once handler says: " + msg)

def msgHandler2(msg):
    print("Handler 2 says: " + msg)

print("\n\tALL LISTENERS:\n")

emitter.on("message", msgHandler1)
emitter.once("message", onceHandler)
emitter.on("message", msgHandler2)

print(emitter.listeners("message"))
print(emitter.raw_listeners("message"))

emitter.emit("message", "Hello world!")

print("\n\tHANDLER 2 AND TEMP LISTENER REMOVED:\n") 
# NOTE: Temp handler removed automatically

emitter.remove_listener("message", msgHandler2)

emitter.emit("message", "Hello world!")