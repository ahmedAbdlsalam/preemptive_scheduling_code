from matplotlib import pyplot
import numpy as np


class Priority:

    def processData(self, no_of_processes):
        process_data = []

        for i in range(no_of_processes):
            temporary = []
            process_id = int(input("Enter Process ID: "))
            arrival_time = int(input(f"Enter Arrival Time for Process {process_id}: "))
            periodic = int(input(f"Enter periodic Time for Process {process_id}: "))
            execution = int(input(f"Enter execution for Process {process_id}: "))
            deadline = int(input(f"Enter deadline for Process {process_id}: "))
            temporary.extend([process_id, arrival_time, periodic, execution, deadline, 0])
            '''
            '0' is the state of the process. 0 means not executed and 1 means execution complete
            '''
            process_data.append(temporary)

        Priority.schedulingProcess(self, process_data)

    def schedulingProcess(self, process_data):
        start_time = []
        exit_time = []
        s_time = 0  # time unit
        sequence_of_process = []  # store the execution sequence
        process_data.sort(key=lambda x: x[1])
        '''
        Sort processes according to the Arrival Time
        '''
        while 1:
            ready_queue = []
            normal_queue = []
            temp = []
            for i in range(len(process_data)):
                if process_data[i][1] <= s_time and process_data[i][5] == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][3],
                                 process_data[i][4]])
                    ready_queue.append(temp)
                    temp = []
                # process didn't execute yet
                elif process_data[i][5] == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4],
                                 process_data[i][4]])
                    normal_queue.append(temp)
                    temp = []
            if len(ready_queue) == 0 and len(normal_queue) == 0:
                break
            if len(ready_queue) != 0:
                # sort the process according to the priority
                ready_queue.sort(key=lambda x: x[0], reverse=True)
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(ready_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == ready_queue[0][0]:
                        process_data[k][3] = process_data[k][3] - 1
                        break

                if process_data[k][3] == 0:  # if execution time is zero, it means process is completed
                    process_data[k][5] = 1  # indicator set to one if the task completed
                    process_data[k].append(e_time)

            """
            if a condition at the current time there no process to run
            and all the process in the ready queue already executed
            then we jump to the normal queue and raise the s_time value 
            the the first task in the normal queue
            """
            if len(ready_queue) == 0:

                normal_queue.sort(key=lambda x: x[0])
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(normal_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == normal_queue[0][0]:
                        process_data[k][2] = process_data[k][3] - 1
                        break

                if process_data[k][3] == 0:  # if execution time is zero, it means process is completed
                    process_data[k][5] = 1  # task completion indicator
                    process_data[k].append(e_time)
        print(sequence_of_process)
        # time_unit = 1
        # for j in sequence_of_process:
        #     print(f"job{j}", time_unit, end=" ")
        #     time_unit += 1

        Priority.plot(self, sequence_of_process)

    def plot(self, sequence_of_process):
        colors = ['w', 'y', 'b', 'r']
        fig, ax = pyplot.subplots(figsize=(10, 6))
        ax.set_ylim(0, 40)
        ax.set_xlim(0, 50)
        ax.set_xlabel('time')
        ax.set_yticks([12.5, 22.5, 32.5])

        ax.set_yticklabels(['Task1', "Task2", "Task3"])
        a = 0
        for i in sequence_of_process:
            ax.broken_barh([(a, 1)], (i * 10, 5), facecolors=colors[i])
            a = a + 1
        pyplot.show()


if __name__ == "__main__":
    no_of_processes = int(input("Enter number of processes: "))
    priority = Priority()
    priority.processData(no_of_processes)
