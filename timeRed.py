from datetime import datetime,timedelta

def timenow():
    return(str(datetime.now())[:19])
def timeAfter():
    timeAfterBooking = datetime.now() + timedelta(hours=1)
    return(str(timeAfterBooking)[:19])