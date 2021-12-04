"""Single Responsibility Principle or Seperation Of Concerns each class has only one responsibility"""


class Journal:
    # each class have single responsibility
    def __init__(self, entries: list, count: int = 0):
        self.entries = entries
        self.count = count

    def add_entry(self, text: str):
        self.count += 1
        self.entries.append(f'{self.count} : {text}')

    def remove_entry(self, position: int):
        del self.entries[position]

    def __str__(self):
        return '\n'.join(self.entries)
    #breaking responsibility by adding additional functionality like the ability to save itself after executing (adding persistance like saving loading etc)
    # def save_entries(self,filename: str):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()
    #this is considered a bad idea if you see the general idea of complete application have different types their own save and load etc along with this implemented class then if we add additional data or implement additional features we had to implement them in each single class look for (persistance_manager class file) for more details and implentation      