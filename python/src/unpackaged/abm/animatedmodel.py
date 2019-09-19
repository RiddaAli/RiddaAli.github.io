import random
import matplotlib
matplotlib.use('TkAgg')
matplotlib.use('macosx')
import tkinter
import matplotlib.pyplot
import matplotlib.animation 
import agentframework
import csv


num_of_agents = 20
num_of_iterations = 100
agents = []
# 20 is the radius around agents
neighbourhood = 20

# Setting the figure size for the plot to (width = 7, height = 7)
fig = matplotlib.pyplot.figure(figsize=(7, 7))

# Adding axes at position [left, bottom, widht, height]
ax = fig.add_axes([0, 0, 1, 1])

carry_on = True

#ax.set_autoscale_on(False)

# =============================================================================
# # Creating an empty list called "environment" 
# (as it will store environmental data) to move the data read from the csv
# file into a 2D list  
# =============================================================================
environment = []
# Reading the csv file called "in.csv" 
f = open('in.csv', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
 # A list of rows
for row in reader:
    # Creating an empty list called "rowlist" to store all the values
     rowlist = []
     
     # A list of value
     for value in row:
         rowlist.append(value)
# =============================================================================
#    # Adding the values from each row to the "environment" list making it a 
#    #2D List
# =============================================================================
     environment.append(rowlist)
     
# Once done with the reader close the file
f.close()

# Creating the agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

def update(frame_number):
    
    global carry_on
    fig.clear()   

    # Using the matplot librabry to plot our agents        
    matplotlib.pyplot.xlim(0, 300)
    matplotlib.pyplot.ylim(300, 0)
    
    # Checking that the data has been imported correctly by plotting it
    matplotlib.pyplot.imshow(environment)
    
    # Randomly shuffling the agents
    random.shuffle(agents)
    
    for i in range(num_of_agents):
        print('store - {0}'.format(agents[i].store))
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

        matplotlib.pyplot.scatter(agents[i].get_x(),agents[i].get_y())
        if agents[i].store > 300:
            print("Agent {} is full!".format(i))
            carry_on = False
        print('store - {0}'.format(agents[i].store))
        
    

def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1,
            repeat=False, frames=gen_function)
    canvas.show()


root = tkinter.Tk()
root.wm_title("Model")

canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

tkinter.mainloop()













