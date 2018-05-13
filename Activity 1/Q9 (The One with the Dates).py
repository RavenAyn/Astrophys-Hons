x=input("Enter the Date in dd/mm/yy format: ")
day=int(x[0:2])
month=int(x[3:5])
year=int(x[6:10])
md=31
if month>2:
    if year%4==0:
        md=md+29
    else:
        md=md+28
    if month>3:
        md=md+31
        if month>4:
            md=md+30
            if month>5:
                md=md+31
                if month>6:
                    md+=30
                    if month>7:
                        md+=31
                        if month>8:
                            md+=31
                            if month>9:
                                md+=30
                                if month>10:
                                    md+=31
                                    if month>11:
                                        md+=30
print("Day of the Year is", md+day)
