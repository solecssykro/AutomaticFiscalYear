from datetime import datetime 

strDate = input("Enter Date (format yyyy-mm-dd): ")
format_string = "%Y-%m-%d"

##hint dates are not a default data type in Python so you need to use the datetime library to bring in that data type. 
dtDate = datetime.strptime(strDate, format_string)




##Desired output should read FY#### where #### is the fiscal year.
print(f"FY{dtDate}")


