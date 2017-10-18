import datetime
def which_date(start_date,time):
    """
    This function takes as input a string depicting a date in YYYY/mm/dd
    format and a string stating a time period in the form of "X day(s)" or
    "Y week(s)". Output should be a string in form YYYY/mm/dd with the date
    that is X days or Y weeks after the initial date.
    """
    
    # Replace this with your code!
    #start_date = input('')
    #time = input("")

    day_word=time.split(' ')

    if day_word[1] == "days": 
        days=datetime.datetime.strptime(start_date, '%Y/%m/%d') + datetime.timedelta(days=int(day_word[0]))
        return str(days.strftime('%Y/%m/%d'))

    elif day_word[1] == "weeks" or 'week':
        weeks=datetime.datetime.strptime(start_date, '%Y/%m/%d') + datetime.timedelta(weeks=int(day_word[0]))
        return str(weeks.strftime('%Y/%m/%d'))
    
    return start_date,time
    
def test():
    """
    Here are a few tests to check if your code is working correctly! This
    function will be run when the Test Run button is selected. Additional
    tests that are not part of this function will also be run when the Submit
    Answer button is selected.
    """
    assert which_date('2016/02/10','35 days') == '2016/03/16'
    assert which_date('2016/12/21','3 weeks') == '2017/01/11'
    assert which_date('2015/01/17','1 week') == '2015/01/24'
    print("All tests completed.")


if __name__ == "__main__":
    test()
