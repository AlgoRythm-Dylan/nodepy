"""

https://nodejs.org/api/events.html

TODO: Implement max listeners, listener_count(event_name)

NOTE: By default, a maximum of 10 listeners can be registered for any single event
This limit can be changed for individual EventEmitter instances using the emitter.setMaxListeners(n) method. 
To change the default for all EventEmitter instances, the EventEmitter.defaultMaxListeners property can be used
Take caution when setting the EventEmitter.defaultMaxListeners because the change affects all 
EventEmitter instances, including those created before the change is made
However, calling emitter.setMaxListeners(n) still has precedence over EventEmitter.defaultMaxListeners.

"""

class events:

    class EventEmitter:

        def __init__(self):
            self._listeners = {}

        def add_listener(self, event_name, listener, once):
            if not event_name in self._listeners.keys():
                self._listeners[event_name] = []
            self._listeners[event_name].append({"execute": listener, "once": once, "executed": False})

        def emit(self, event_name, *args):
            had_listeners = False
            if event_name in self.event_names():
                for listener in self._listeners[event_name]:
                    if not (listener["once"] and listener["executed"]):
                        listener["execute"](*args)
                        had_listeners = True
                        if listener["once"]:
                            listener["executed"] = True
                # Clean up executed items
                self._listeners[event_name] = [listener for listener in self._listeners[event_name] if not listener["executed"]]
            return had_listeners

        def event_names(self):
            return self._listeners.keys()

        def listeners(self, event_name):
            if event_name in self.event_names():
                return [listener["execute"] for listener in self._listeners[event_name]]

        def off(self, event_name, listener):
            return self.remove_listener(event_name, listener)

        def on(self, event_name, listener):
            return self.add_listener(event_name, listener, False)
            
        def once(self, event_name, listener):
            return self.add_listener(event_name, listener, True)

        def prepend(self, event_name, listener):
            if not event_name in self.event_names():
                self.listeners[event_name] = []
            self._listeners[event_name].insert(0, {"execute": listener, "once": False, "Executed": False})
            return self

        def prepend_once_listener(self, event_name, listener):
            if not event_name in self.event_names():
                self.listeners[event_name] = []
            self._listeners[event_name].insert(0, {"execute": listener, "once": True, "Executed": False})
            return self

        def remove_all_listeners(event_name):
            if event_name in self.event_names():
                del self._listeners[event_name]
            return self

        def remove_listener(self, event_name, listener):
            for event_listener in self._listeners[event_name]:
                if event_listener["execute"] is listener:
                    self._listeners[event_name].remove(event_listener)
                    break
            return self
        
        def raw_listeners(self, event_name):
            if event_name in self.event_names():
                return self._listeners[event_name]