# Project: Maryland Census Data Analytics
# Group Members: Brett Reisman, Devin Sparrow, Rafi Wind

# In[1]:

# Import Library Area #
import pandas as pd
import openpyxl
from tkinter import *
from tkinter import ttk


# In[2]:

# Assigning County Data to Variable #

# Anne Arundel County
aa_population = pd.read_excel('http://planning.maryland.gov/msdc/census/cen2010/pop_70-10/HouseholdPopulation.xls')
aa_size = pd.read_excel("http://planning.maryland.gov/msdc/census/cen2010/pop_70-10/HouseholdSize.xls")

# Baltimore City
bc_population = pd.read_excel("http://planning.maryland.gov/msdc/census/cen2010/pop_70-10/HouseholdPopulation.xls")
bc_size = pd.read_excel("http://planning.maryland.gov/msdc/census/cen2010/pop_70-10/HouseholdSize.xls")

# Howard County
hc_population = pd.read_excel("http://planning.maryland.gov/msdc/census/cen2010/pop_70-10/HouseholdPopulation.xls")
hc_size = pd.read_excel("http://planning.maryland.gov/msdc/census/cen2010/pop_70-10/HouseholdSize.xls")

# Prince George's County
pc_population = pd.read_excel("http://planning.maryland.gov/msdc/census/cen2010/pop_70-10/TotalPopulation.xls")
pc_size = pd.read_excel("http://planning.maryland.gov/msdc/census/cen2010/pop_70-10/HouseholdSize.xls")

# Queen Anne's County
qa_population = pd.read_excel("http://planning.maryland.gov/msdc/census/cen2010/pop_70-10/TotalPopulation.xls")
qa_size = pd.read_excel("http://planning.maryland.gov/msdc/census/cen2010/pop_70-10/HouseholdSize.xls")


# In[3]:

# Display AA Population Datatable #

aa_population.drop(["Unnamed: 2","Unnamed: 3", "Unnamed: 6", "Change", "Unnamed: 8", "Unnamed: 9"], axis=1, inplace=True)
aa_population.drop(aa_population.columns[1], axis=1, inplace=True)

aa_population.drop([0, 1, 3, 4, 5, 7], axis=0, inplace=True)
aa_population.drop(aa_population.index[7:40], axis=0, inplace=True)
aa_population.drop([8, 9, 10, 11, 12,], axis=0, inplace=True)
aa_population.rename(columns={'Unnamed: 0' : 'County',
'Unnamed: 4' : '2000', 'Unnamed: 5' : '2010', 'Unnamed: 10' : '2000-2010 Difference'}, inplace=True)
aa_population


# In[4]:

# Display BC Population Datatable #

bc_population.drop(["Unnamed: 2","Unnamed: 3", "Unnamed: 6", "Change", "Unnamed: 8", "Unnamed: 9"], axis=1, inplace=True)
bc_population.drop(bc_population.columns[1], axis=1, inplace=True)

bc_population.drop([0, 1, 3, 4, 5, 6, 7, 8, 9, 10,12], axis=0, inplace=True)
bc_population.drop([13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41], axis=0, inplace=True)
bc_population.rename(columns={'Unnamed: 0' : 'County',
'Unnamed: 4' : '2000', 'Unnamed: 5' : '2010', 'Unnamed: 10' : '2000-2010 Difference'}, inplace=True)
bc_population


# In[5]:

# Display HC Population Datatable #

hc_population.drop(["Unnamed: 2","Unnamed: 3", "Unnamed: 6", "Change", "Unnamed: 8", "Unnamed: 9"], axis=1, inplace=True)
hc_population.drop(hc_population.columns[1], axis=1, inplace=True)

hc_population.drop([0, 1, 3, 4, 5, 6, 7, 8, 9, 11,12], axis=0, inplace=True)
hc_population.drop([13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41], axis=0, inplace=True)
hc_population.rename(columns={'Unnamed: 0' : 'County',
'Unnamed: 4' : '2000', 'Unnamed: 5' : '2010', 'Unnamed: 10' : '2000-2010 Difference'}, inplace=True)
hc_population


# In[6]:

# Display PC Population Datatable #

pc_population.drop(["Unnamed: 2","Unnamed: 3", "Unnamed: 6", "Change", "Unnamed: 8", "Unnamed: 9"], axis=1, inplace=True)
pc_population.drop(pc_population.columns[1], axis=1, inplace=True)

pc_population.drop([0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11,12], axis=0, inplace=True)
pc_population.drop([13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41], axis=0, inplace=True)
pc_population.rename(columns={'Unnamed: 0' : 'County',
'Unnamed: 4' : '2000', 'Unnamed: 5' : '2010', 'Unnamed: 10' : '2000-2010 Difference'}, inplace=True)
pc_population


# In[7]:

# Display QC Population Datatable #

qa_population.drop(["Unnamed: 2","Unnamed: 3", "Unnamed: 6", "Change", "Unnamed: 8", "Unnamed: 9"], axis=1, inplace=True)
qa_population.drop(qa_population.columns[1], axis=1, inplace=True)

qa_population.drop([0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11,12], axis=0, inplace=True)
qa_population.drop([13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,37,38,39,40,41], axis=0, inplace=True)
qa_population.rename(columns={'Unnamed: 0' : 'County',
'Unnamed: 4' : '2000', 'Unnamed: 5' : '2010', 'Unnamed: 10' : '2000-2010 Difference'}, inplace=True)
qa_population


# In[8]:

def county_input(event):
    output_area.delete(1.0, "end")
    user_input = countyEntry.get()
    user_input_modified = user_input.lower()
    if user_input_modified == "aa":
        for i in range(1):
            if var1.get():
                output_variable = aa_population.shape
                output_area.insert(1.0, '{}\n'.format(output_variable))
            if var2.get():
                output_variable = aa_population.loc[3:]
                output_variable_modified = output_variable['2000'].sum()
                output_area.insert(1.0, '{}\n'.format(output_variable_modified))
            if var3.get():
                output_variable = aa_population.loc[3:]
                output_variable_modified = output_variable['2010'].sum()
                output_area.insert(1.0, '{}\n'.format(output_variable_modified))
            if var4.get():
                output_variable = aa_population.dtypes
                output_area.insert(1.0, '{}\n'.format(output_variable))
            if var5.get():
                output_variable = aa_population.loc[3:]
                data_sum = output_variable['2010'].sum() - output_variable['2000'].sum()
                output_area.insert(1.0, '{}\n'.format(data_sum))
    elif user_input_modified == "bc":
        for i in range(1):
            if var1.get():
                output_variable = bc_population.shape
                output_area.insert(1.0, '{}\n'.format(output_variable))
            if var2.get():
                output_variable = bc_population.loc[3:]
                output_variable_modified = output_variable['2000'].sum()
                output_area.insert(1.0, '{}\n'.format(output_variable_modified))
            if var3.get():
                output_variable = bc_population.loc[3:]
                output_variable_modified = output_variable['2010'].sum()
                output_area.insert(1.0, '{}\n'.format(output_variable_modified))
            if var4.get():
                output_variable = bc_population.dtypes
                output_area.insert(1.0, '{}\n'.format(output_variable))
            if var5.get():
                output_variable = bc_population.loc[3:]
                data_sum = output_variable['2010'].sum() - output_variable['2000'].sum()
                output_area.insert(1.0, '{}\n'.format(data_sum))
    elif user_input_modified == "hc":
        for i in range(1):
            if var1.get():
                output_variable = hc_population.shape
                output_area.insert(1.0, '{}\n'.format(output_variable))
            if var2.get():
                output_variable = hc_population.loc[3:]
                output_variable_modified = output_variable['2000'].sum()
                output_area.insert(1.0, '{}\n'.format(output_variable_modified))
            if var3.get():
                output_variable = hc_population.loc[3:]
                output_variable_modified = output_variable['2010'].sum()
                output_area.insert(1.0, '{}\n'.format(output_variable_modified))
            if var4.get():
                output_variable = hc_population.dtypes
                output_area.insert(1.0, '{}\n'.format(output_variable))
            if var5.get():
                output_variable = hc_population.loc[3:]
                data_sum = output_variable['2010'].sum() - output_variable['2000'].sum()
                output_area.insert(1.0, '{}\n'.format(data_sum))
    elif user_input_modified == "pc":
        for i in range(1):
            if var1.get():
                output_variable = pc_population.shape
                output_area.insert(1.0, '{}\n'.format(output_variable))
            if var2.get():
                output_variable = pc_population.loc[3:]
                output_variable_modified = output_variable['2000'].sum()
                output_area.insert(1.0, '{}\n'.format(output_variable_modified))
            if var3.get():
                output_variable = pc_population.loc[3:]
                output_variable_modified = output_variable['2010'].sum()
                output_area.insert(1.0, '{}\n'.format(output_variable_modified))
            if var4.get():
                output_variable = pc_population.dtypes
                output_area.insert(1.0, '{}\n'.format(output_variable))
            if var5.get():
                output_variable = pc_population.loc[3:]
                data_sum = output_variable['2010'].sum() - output_variable['2000'].sum()
                output_area.insert(1.0, '{}\n'.format(data_sum))
    elif user_input_modified == "qa":
        for i in range(1):
            if var1.get():
                output_variable = qa_population.shape
                output_area.insert(1.0, '{}\n'.format(output_variable))
            if var2.get():
                output_variable = qa_population.loc[3:]
                output_variable_modified = output_variable['2000'].sum()
                output_area.insert(1.0, '{}\n'.format(output_variable_modified))
            if var3.get():
                output_variable = qa_population.loc[3:]
                output_variable_modified = output_variable['2010'].sum()
                output_area.insert(1.0, '{}\n'.format(output_variable_modified))
            if var4.get():
                output_variable = qa_population.dtypes
                output_area.insert(1.0, '{}\n'.format(output_variable))
            if var5.get():
                output_variable = qa_population.loc[3:]
                data_sum = output_variable['2010'].sum() - output_variable['2000'].sum()
                output_area.insert(1.0, '{}\n'.format(data_sum))
    else:
        sys.exit()

def clear_console(event):
    output_area.delete(1.0, "end")


root = Tk()
root.title("Maryland Census Data Analtics")

Label(root, text="Please Select From The Following Counties", fg="red", font="none 18 bold").pack()
Label(root, text='''Anne Arundel County = please enter AA
Baltimore City = please enter BC
Howard County = please enter HC
Prince George's County = please enter PC
Queen Anne's County = please enter QA''').pack()

countyEntry = Entry(root, width="10")
countyEntry.pack()

var1=IntVar()
testCheck = Checkbutton(root, text="Shape (rows, columns)", onvalue=1, offvalue=0, variable=var1)
testCheck.pack()

var2=IntVar()
testCheck2 = Checkbutton(root, text="Population in 2000", onvalue=1, offvalue=0, variable=var2)
testCheck2.pack()

var3=IntVar()
testCheck2 = Checkbutton(root, text="Population in 2010", onvalue=1, offvalue=0, variable=var3)
testCheck2.pack()

var4=IntVar()
testCheck2 = Checkbutton(root, text="Category Data Types", onvalue=1, offvalue=0, variable=var4)
testCheck2.pack()

var5=IntVar()
testCheck2 = Checkbutton(root, text="Difference Between 2010 and 2000", onvalue=1, offvalue=0, variable=var5)
testCheck2.pack()

countyButton = Button(root, text="Run")
countyButton.bind("<Button-1>", county_input)
countyButton.pack()
clearButton = Button(root, text="Clear Console")
clearButton.bind("<Button-1>", clear_console)
clearButton.pack()

#outputEntry = Entry

output_area = Text(root, width="40", height="15")
output_area.pack()
exit = Button(root, text='Exit', command=root.destroy)
exit.pack()
root.mainloop()
