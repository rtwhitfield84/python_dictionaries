stockDict = { 'GM': 'General Motors',
 'CAT':'Caterpillar', 'EK':"Eastman Kodak" }

purchases = [ ( 'GM', 100, '10-sep-2001', 48 ),
 ( 'CAT', 100, '1-apr-1999', 24 ),
 ( 'GM', 200, '1-jul-1998', 56 ) ]

 #shares * dollars
 
for purchase in purchases:
	ticker = purchase[0]
	full_company_name = stockDict[ticker]
	full_purchase_price = purchase[1] * purchase[3]

	print("I purchased {0} stock for ${1}".format(full_company_name,full_purchase_price) )



# my_purchase_history = {'I purchased ' + k + ' stock for ' + v for (k,v) in purchases.items()}

# print(my_purchase_history)