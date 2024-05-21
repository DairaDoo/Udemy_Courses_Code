class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected_by = True
    
    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"
    
    def disconnect(self):
        self.connected_by = False
        print("Disconnected")
        

# herencia
class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        #super calls the parent class
        super().__init__(name, connected_by)
        self.capacity = capacity # max capacity
        self.remaining_pages = capacity # current capacity
        
    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"
    
    def print(self, pages):
        if not self.connected_by:
            print("Your printer not connected.")
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages
        
printer = Printer("Printer", "USB", 500)
printer.print(20)
printer.disconnect()

print(printer)