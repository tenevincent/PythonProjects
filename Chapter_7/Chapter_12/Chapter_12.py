

def run_plot_demo():
        import matplotlib.pyplot as plt
        y = [1, 4, 9, 16, 25,36,49, 64]
        x1 = [1, 16, 30, 42,55, 68, 77,88]
        x2 = [1,6,12,18,28, 40, 52, 65]
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        l1 = ax.plot(x1,y,'ys-') # solid line with yellow colour and square marker
        l2 = ax.plot(x2,y,'go--') # dash line with green colour and circle marker
        ax.legend(labels = ('tv', 'Smartphone'), loc = 'lower right') # legend placed at lower right
        ax.set_title("Advertisement effect on sales")
        ax.set_xlabel('medium')
        ax.set_ylabel('sales')


        plt.style.use('seaborn')
        plt.grid()
        plt.show()

        
def running_subplot():
        import matplotlib.pyplot as plt
        # plot a line, implicitly creating a subplot(111)
        plt.plot([1,2,3])
        # now create a subplot which represents the top plot of a grid with 2 rows and 1 column.
        #Since this subplot will overlap the first, the plot (and its axes) previously 
        #created, will be removed
        plt.grid() 
        plt.subplot(211)
        plt.plot(range(12))
        plt.subplot(212, facecolor='y') # creates 2nd subplot with yellow background
        plt.plot(range(12))
        # show
        plt.show()

# running_subplot()
#running_subplot()

def running_another_subplot():
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot([1,2,3])
    ax2 = fig.add_subplot(221, facecolor='y')
    ax2.plot([1,2,3])
    # show plot
    plt.show()


def running_subplot():
        import matplotlib.pyplot as plt
        import numpy as np
        import math
        x = np.arange(0, math.pi*2, 0.05)
        fig=plt.figure()
        
        plt.gca()

        axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
        axes1.grid()
        axes2 = fig.add_axes([0.55, 0.55, 0.3, 0.3]) # inset axes
        axes2.grid()

        y = np.sin(x)
        
        axes1.plot(x, y, 'b')
        axes2.plot(x,np.cos(x),'r')
        axes1.set_title('sine')
        axes2.set_title("cosine")
        # plt.grid()
        plt.show()

def subplots_demo():
        import matplotlib.pyplot as plt
        [fig,a] =  plt.subplots(2,2)
        import numpy as np
        x = np.arange(1,5)
        a[0][0].grid()
        plt.style.use("seaborn")
        a[0][0].plot(x,x*x)
        a[0][0].set_title('square')
        plt.style.use("seaborn")
        a[0][1].plot(x,np.sqrt(x))
        a[0][1].set_title('square root')
        plt.style.use("seaborn")
        a[1][0].plot(x,np.exp(x))
        a[1][0].set_title('exp')
        plt.style.use("seaborn")
        plt.style.use("seaborn")
        a[1][1].plot(x,np.log10(x))
        a[1][1].set_title('log')        
        plt.show()


def subplots():
    import matplotlib.pyplot as plt
    a1 = plt.subplot2grid((3,3),(0,0),colspan = 2)
    a2 = plt.subplot2grid((3,3),(0,2), rowspan = 3)
    a3 = plt.subplot2grid((3,3),(1,0),rowspan = 2, colspan = 2)
    import numpy as np
    x = np.arange(1,10)
    a2.plot(x, x*x)
    a2.set_title('square')
    a1.plot(x, np.exp(x))
    a1.set_title('exp')
    a3.plot(x, np.log(x))
    a3.set_title('log')
    plt.tight_layout()
    plt.show()

# running_subplot()
# #subplots_demo()


subplots()


