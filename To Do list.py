class Mission():

    def __init__(self):
       self.tasks_list = ['']  

    def add_task(self):
        task_name = str(input('Enter new task: '))
        self.tasks_list.append(task_name)

    def remove_task(self):
        task_name = str(input('Enter the name of task: '))
        self.tasks_list.remove(task_name)

    def show_tasks(self):
        for index in range(len(self.tasks_list)):
            if index != 0 :
                print(f'{index} - {self.tasks_list[index]}')
    
    def Exit(self):
        return False
    
    def options(self):
        print('1 - Add new task')
        print('2 - Remove task')
        print('3 - Show tasks')
        print('4 - Exit')

        option = input('enter a number: ')
        print('---------------------')

        if option in ['1', '2', '3', '4']:
            
            if option in '1':
                self.add_task()
                print('---------------------')
            
            elif option in '2':
                self.remove_task()
                print('---------------------')

            elif option in '3':
                self.show_tasks()
                print('---------------------')

            elif option in '4':
                status = self.Exit()
                print('done')
                return status

        else:
            print("Your input isn't correct. Try again")
            print('---------------------')

status = True
program = Mission()

while status != False:
    status = program.options()
    if status == False:
        print('Thanks :)')