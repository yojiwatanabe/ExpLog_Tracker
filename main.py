
            ###########################################
            #                                         #
            #              Yoji Watanabe              #
            #         Expense Log Entry Program       #
            #          Created Sept. 14 2015          #
            #                 V 0.04                  #
            #                                         #
            ###########################################

import numpy as np
import csv

print "Hello, welcome to your personal expenses log."
print

def load_data():
	categories = np.sort(np.load('categ.npy'))
	return categories

def input_info():
	pro = []; cost = []; cat = []; des =[] 
	pro = raw_input("What did you buy? \n")
	cost = raw_input("How much did it cost? \n")
	print "Your categories are:"
	for i in range(0, len(cats)):
		if i+1 < len(cats):
			print cats[i] + " | ",
		else:
			print cats[i]
	cat_in = raw_input("What category is this product in? Type in \"new cat\" to create a new category. \n")
	flag = False
	while flag == False:
		if any(cat_in in s for s in cats) == True and len(cat_in) > 3:
			cat = cat_in
			flag = True
		elif cat_in == "new cat":
			cat = create_cat()
			flag = True
		else:
			print "That\'s not a valid category, try again."
			cat_in = raw_input("New category: ")
	des = raw_input("Input a short description of purchase. ")
	return pro, cost, cat, des 

def write_info(product, cost, category, description):
	row = [[category]+[product]+[cost]+[description]]
	print "Great, I'm now adding "+ product + ", " + cost + ", " + category + ", " + description + " to your expense log."
	with open("log.csv",  "a") as log:
		writer = csv.writer(log)
		writer.writerows(row)

def create_cat():
	cat_in = raw_input("What category would you like to create? ")
	new_cats = np.append(cats, cat_in)
	np.save('categ.npy', new_cats)
	return new_cats[-1]

# # # # # # # # # # # # # # # # # # # # # # # # #
if __name__ == "__main__":
	cats = load_data()
	pro, cost, cat, des = input_info()
	write_info(pro, cost, cat, des)