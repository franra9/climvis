import tkinter as tk
import cartopy.crs as ccrs  # Projections list
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from enso_functions import clim, yearly_evol
import enso_dwl
import os
import enso_plots

root = tk.Tk()
root.title('ERA5 Visualization App')
screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()
root.geometry(f"{screen_width}x{screen_height}")

#chose date
clicked_year = tk.StringVar()
clicked_year.set("Choose Year")

drop_year = tk.OptionMenu(root, clicked_year, *list(range(1979, 2019)))
drop_year.grid(column=0, row=1, sticky="S")
drop_year.config(font=("Ariel", 30))
menu_year = root.nametowidget(drop_year.menuname)
menu_year.config(font=("Ariel", 30))

# let the user choose a date
global year, start_month, end_year, end_month
start_year, start_month, end_year, end_month = "", "", "", ""


def grab_date():
    date_label.config(text = clicked_year.get())
    global year
    year = clicked_year.get()

chosen_variables = []


# choose variable to plot
#def selected_items():
#    global clicked_items
#    clicked_items = variable_list.curselection()

#    global chosen_variables
#    for i in clicked_items:
#        item = variable_list.get(i)
#        chosen_variables.append(item)

#    printed_text = ''
#    for j in clicked_items:
#        item = variable_list.get(j)
#        printed_text = printed_text + "\n" + str(item)
#        variable_label.config(text=printed_text)


# download the corresponding file from ERA5 server

def download_button():
    #year
    answer = tk.messagebox.askquestion("Download", "Do you want to start the download now?")
    if answer == "yes":
        if os.path.exists('ERA5_Monthly_sst_' + str(year) + '_enso34.nc'):
            answer2 = tk.messagebox.askquestion("File already exists!",
                                                "Attention! A file with the same name as the downloaded one already"
                                                " exist."
                                                "\nIf you continue it will be overwritten with the new file."
                                                "\nDo you want to continue?", icon="warning")
            if answer2 == "yes":
                tk.messagebox.showinfo("Explanation", "The download will start now."
                                                      "\nJust wait until you see 'Your File is downloaded!' on the screen"
                                                      "\nYou can see the progress of the download in the command line.")
                enso_dwl.dwl_era5_enso(int(year), [False, False, True, False])
                if os.path.exists('ERA5_Monthly_sst_' + year + '_enso34.nc'):
                    download_update.config(text="Your file is downloaded!")


        else:
            tk.messagebox.showinfo("Explanation", "The download will start now."
                                                  "\nJust wait until you see 'Your File is downloaded!' on the screen"
                                                  "\nYou can see the progress of the download in the command line.")
            enso_dwl.dwl_era5_enso(year, [False, False, True, False])
            if os.path.exists('ERA5_Monthly_sst_' + year + '_enso34.nc'):
                download_update.config(text="Your file is downloaded!")

def plot_result():
    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np

    # Data for plotting
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
           title='About as simple as it gets, folks')
    ax.grid()

    fig.savefig("test.png")
    plt.show()
    #text.set_visible(False)
    #enso_plots.plot_nino(ano)
    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().grid(column=4, row=1, rowspan=10, columnspan=10)

fig = plt.figure(figsize=(8, 6))
text = fig.text(.4, .75, "Your plot will be shown here")
canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().grid(column=4, row=1, rowspan=10, columnspan=10)

empty_space = tk.Label(root, text='', width=30)
empty_space.grid(column=3, row=0)

some_text = tk.Label(root, text='Choose year of interest:', font=("Ariel", 44), fg="Steel Blue")
some_text.grid(column=0, row=0)

#start_date_button = tk.Button(root, text='Select Start Date', command=grab_date, font=("Ariel", 30))
#start_date_button.grid(column=0, row=3)

date_label = tk.Label(root, text='', font=("Ariel", 30))
date_label.grid(column=0, row=4)

date_button = tk.Button(root, text='Select Year', command=grab_date, font=("Ariel", 30))
date_button.grid(column=1, row=3)

#end_date_label = tk.Label(root, text='', font=("Ariel", 30))
#end_date_label.grid(column=1, row=4)

#some_text_4 = tk.Label(root, text="Choose Location of interest", font=("Ariel", 44), fg="Steel Blue")
#some_text_4.grid(column=0, row=6, sticky="W")

#some_text_5 = tk.Label(root, text="Click the button and choose your location of \ninterest by clicking on the map",
#                       font=("Ariel", 30))
#some_text_5.grid(column=0, row=7, rowspan=2)

#location_button = tk.Button(root, text="Choose Location", command=interactive_map, font=("Ariel", 30))
#location_button.grid(column=1, row=7)

#location_label = tk.Label(root, text='', font=("Ariel", 30))
#location_label.grid(column=1, row=8)

#some_text_6 = tk.Label(root, text="Choose one or more variables", font=("Ariel", 44), fg="Steel Blue")
#some_text_6.grid(column=0, row=9, sticky="W")

#variable_list = tk.Listbox(root, selectmode=tk.SINGLE, font=("Ariel", 30))
#variable_list.grid(column=0, row=10)

#variables = ["Energy Budget", "Snow Depth", "2m_temperature"]

#for i in variables:
#    variable_list.insert(tk.END, i)

#variable_button = tk.Button(root, text="Select Variable", command=selected_items, font=("Ariel", 30))
#variable_button.grid(column=1, row=10, sticky="N")

#variable_label = tk.Label(root, text='', font=("Ariel", 30))
#variable_label.grid(column=1, row=10)

test_button = tk.Button(root, text="Download", command=download_button, font=("Ariel", 30))
test_button.grid(column=0, row=11)

download_update = tk.Label(root, text='', font=("Ariel", 30))
download_update.grid(column=1, row=11)

accept_button = tk.Button(root, text='Make Plot', command=plot_result, font=("Ariel", 30))
accept_button.grid(column=1, row=12)

root.mainloop()
