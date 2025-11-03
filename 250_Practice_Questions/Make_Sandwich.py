
def make_sandwich(*args, default="butter only"):
    sandwich_sentence = "Sandwich prepared with "
    if not args:
        return sandwich_sentence + default + "."
    else:
        return sandwich_sentence + ", ".join(args)+"."


print(make_sandwich("tomato", "keera", "gongura"))
print(make_sandwich())


"""
1)Stage : New -> Creating a new form, tasks to be completed mandatorily in this stage are
    1) Enter Customer name
    2) Contact Number
    3) Address
    4) Created by (Should be automatically assigned to the person who created the form)
    5)Assigned Engineer
    6)Installation Start Date (From this date 2 days after if the site survey has not been started and finished then 
        an alarm OR NOTIFICATION should trigger)
    7)Update the engineer comments once finished with this section
    A notification should trigger to the Customer
    
2)Stage : Site Survey -> After doing the survey the engineer should determine if the site is feasible for 
installation or not with attachments as proof, till then the feasibility button should be hidden or disabled (
Additionally feature -> Engineer should enter the estimated materials used, estimated cost, actual materials used, 
actual cost etc in a related Material sheet)A notification should trigger to the Customer

3) Stage : Shadow Analysis -> In this stage the engineer will analyze the rooftop and have pics uploaded as proof and get 
confirmation from higher ups to start the installation, all this conversation should be recorded in the engineering 
comments or in the decision of the confirmation should be in a field. A notification should trigger to the Customer   

4) Stage : Structure Building -> Where in the engineer will build the structure as per the structure given through the 
shadow analysis ( Additionally will Update the Material sheet) A notification should trigger to the Customer and 
Engineer Comments should be entered

5) Stage : Panel Installation -> The Engineer will install the panels, (Additionally update the Material sheet) 
A notification should trigger to the Customer and Engineer Comments should be entered

6) Stage : Wiring -> The Engineer will install the wiring, (Additionally update the Material sheet) 
A notification should trigger to the Customer and Engineer Comments should be entered

7) Stage : Structural Testing -> Perform initial structural testing 
A notification should trigger to the Customer and Engineer Comments should be entered

8) Stage : Grid Connection -> Engineers will connect to the grid 
A notification should trigger to the Customer and Engineer Comments should be entered

9) Stage : Monitoring System Installation -> Engineers will connect Monitoring System
A notification should trigger to the Customer and Engineer Comments should be entered

10) Stage : Final Testing ->  Final Testing to see if data is being transferred to the grid

11) Stage : Completed -> A comment from customer with pics should be uploaded

"""