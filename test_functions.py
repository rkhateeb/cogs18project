import functions as fc

def test_question_input():
    """A test to make sure when the user enter 'yes' the boolean True is returned, 
    and when the user enter anything other than 'yes' the boolean False is returned.
    
    Parameters
    ----------
    None
     
    Returns
    -------
    None
    """ 
    
    test_yes = fc.question_input('yes')
    test_no = fc.question_input('no')
    
    assert test_yes == True
    assert test_no == False
    
    
def test_get_barcodes_from_webcam ():
    """A test to make sure that if no barcodes are scanned, the 
    function will return an empty list.
    
    Note that this test function opens up the webcam, 
    so you will need to wait 30 seconds.
    
    Parameters
    ----------
    None
     
    Returns
    -------
    None
    """ 
    barcodes = fc.get_barcodes_from_webcam()
    assert type(barcodes) == list
    assert len(barcodes) == 0
    

def test_get_info_from_website():
    """A test to make sure we can successfully open the browser when a barcode is inputted.
    
    The barcode I used for this test is for some organic coconut milk from Trader Joe's
    just to make sure the test function works.
    
    Parameters
    ----------
    None
     
    Returns
    -------
    None
    """ 
    assert fc.get_info_from_website('00552387') == True