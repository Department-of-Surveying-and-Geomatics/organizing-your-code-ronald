import matplotlib.pyplot as plt

# Basic function to open a file

def get_file(choice):
    
    if choice == 1:
        file_path = (x_y_coordinate)
    else:
        print("File choice invalid")
        return None
# Function to plot_data

def plot_data(file_object):
    
        
    x_coords = []
    y_coords = []
    
    for line in file_object:
        x, y = map(float, line.split())
        x_coords.append(x)
        y_coords.append(y)
    
    plt.scatter(x_coords, y_coords)
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('Scatter Plot of Coordinates')
    plt.show()


    