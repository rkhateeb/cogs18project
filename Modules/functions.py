import cv2
from pyzbar.pyzbar import decode
import time
import webbrowser

def question_input (user_decision=None):
    """Obtains input from user on whether they want to scan barcodes or not.
    
    Parameters
    ----------
    user_decision: default is None, if passed in, will not ask user for input. string type.
     
    Returns
    -------
    True if user input was 'yes'
    False is user input was anything else
    """ 
    # Ask user if they would like to scan a barcode, and obtain their input
    if user_decision == None:
        decision = input("Would you like to scan a barcode? Type 'yes' to begin.  ")
    else:
        decision = user_decision
    
    # Return boolean value based on user response
    if decision == 'yes':
        return True
    else:
        return False
    

def get_barcodes_from_webcam ():
    """Obtains barcodes scanned using webcam using the OpenCv module and
    pyzbar barcode and QR code reader.
    
    Details of cv2 at: https://docs.opencv.org/master/index.html
    Details of pyzbar at: https://pypi.org/project/pyzbar/
    
    I watched a Youtube video from Kostadin Ristovski https://www.youtube.com/watch?v=IOhZqmSrjlE
    in which he describes the use of the cv2 and pyzbar packages to scan barcodes to create a 
    concert ticketing system. I took inpiration from his code but changed it so that it would 
    close the webcam window after a barcode was detected. I also added the ability to not wait 
    forever incase a barcode is never detected, instead my code will automatically stop the webcam 
    after about 30 seconds. After scanning the detected barcode its added to a list that is then 
    returned.
    
    Parameters
    ----------
    None
      
    Returns
    -------
    used_barcodes: a list of detected barcodes that have been scanned by the webcam
    """ 
    # define an object for video capture
    capture = cv2.VideoCapture(0)
    used_barcodes = []
    timeout = 300 # timeout
    
    # set camera_on to true to start scanning
    while timeout > 0:
        # capture video frame by frame
        success, frame = capture.read()
        #print (timeout)
        # if capture is successful, try to find barcodes using decode from pyzbar
        if success == True:
            #print('successful')
            cv2.imshow('barcode-scan', frame)
            cv2.waitKey(1)
            for code in decode(frame):
                barcode = code.data.decode('utf-8')
                # if webcam has not scanned barcode, scan and add to used_barcodes
                if barcode not in used_barcodes:                    
                    print (f'Barcode detected. {barcode}')
                    used_barcodes.append(barcode)
            
            # freeze the camera for 1 millisecond so it does not continuously scan and print
            time.sleep(1/1000)
            # decrement timeout so code does not run forever and we can close the webcam 
            # if no barcode is detected
            timeout = timeout - 1

            if len(used_barcodes) > 0:
                capture.release()
                cv2.destroyWindow('barcode-scan')
                cv2.waitKey(1)
                return used_barcodes

    # close the webcam and the window
    capture.release()
    cv2.destroyWindow('barcode-scan')
    cv2.waitKey(1)
    return used_barcodes


def get_info_from_website (barcode):
    """Opens a website containing the nutrition info of the scanned barcode in a new tab
    
    For this, I imported and used the webbrowser.open package to open a url in a new window.
    Details at: https://docs.python.org/3/library/webbrowser.html
    
    Parameters
    ----------
    barcode: the barcode for which the nutrition info should be obtained
     
    Returns
    -------
    nutrition_info_page: a website containing the nutrition info of the scanned food item.
    """ 
    # Use webbrowser.open to open the website and use the previously acquired barcode
    # to pull nutritional data on the scanned barcode
    nutrition_info_page = webbrowser.open(f"https://world.openfoodfacts.org/product/{barcode}", new=1)
    return nutrition_info_page


       
