class Youtube_Channel:
    def __init__(self, channel_name, subscribers):
        self.channel_name = channel_name
        self.subscribers = subscribers

    def add_subscribers(self):
        self.subscribers = self.subscribers + 1

    def show_status(self):
        print(f"{self.channel_name} has {self.subscribers} subscribers.")

my_channel = Youtube_Channel("MRC" , 63)
my_channel.add_subscribers()
my_channel.show_status()