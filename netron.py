import netron
import time

class netron_block:
    def __init__(self):
        self.model_path=""
    def on_start(self):
        self.model_path=self.get_property("model_path")
    def run(self):
        while True:
            if not self.model_path == "":
                print("start")
                netron.start(self.model_path,browse=False,host="0.0.0.0")
                print("end")
                self.model_path=""
            print("sleeping")
            time.sleep(1)
    def on_properties_changed(self, affected_properties):
        print("stop")
        netron.stop(host="0.0.0.0")
        self.model_path=self.get_property("model_path")
        
                
