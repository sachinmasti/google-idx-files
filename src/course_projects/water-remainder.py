import time 
# from plyer import notification

while True:
    from win10toast import ToastNotifier
    toaster = ToastNotifier()
    toaster.show_toast("💧 Drink Water", "It's time to hydrate!",)
    time.sleep(3)
