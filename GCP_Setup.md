# **{Incomplete}**
#### Pre-requisites
*  Completed the Raspberry Pi setup
*  A personal Gmail account (i.e. no terpmail, umd, or organization managed account)

#### Gmail Settings Pre-requisites
1.  Go to your account's [Activity Controls page](https://myaccount.google.com/activitycontrols).
2.  Ensure the following options are enabled:
    *  Web & App Activity (Enable additional activities such as Chrome and Device history etc.)
    *  Device Information
    *  Voice & Audio Activity


### Create a Project on the Google Cloud Platform (GCP).

1.  Open the [Actions Console](https://console.actions.google.com) in a separate tab.
2.  Click on <b>Add/Import Project</b> and create your new project or import one you have already created.
    * <b>Make a note of the project-id for future use.</b>
3.  Now navigate to the <b>Device Registration</b> button towards the bottom of the screen and open it in a separate tab (you will need it during the Google Assistant Setup).
4.  Go to the GCP console page for the [Google Assistant API](https://console.developers.google.com/apis/api/embeddedassistant.googleapis.com/overview) and <b>Enable</b> it.
5.  Lastly, you must configure the following settings for the [OAuth consent screen](https://console.developers.google.com/apis/credentials/consent)
    *  Email address
    *  Product name
    
#### Before Proceeding
*  The only tab you will need in future steps is the Device Registration page.

### Register Your Raspberry Pi

1.  On the previously opened Device Registration page, click on <b>Register Model</b>.
2.  Fill out the following fields:
    *  Product Name (Create something simplpe for future steps).
    *  Manufacturer name (You many enter who you are affiliated with).
    *  Device Type (Select "Speaker" or "Light").
    *  Edit the Device Model id to something unique and easy to type.
        *  <b>Make a note of the model-id for future use.</b>
3.  You will now be prompted to download the credentials json file named "client_secret_<...>.json"        
    *  Make sure to store this in the /home/pi folder and not /home/pi/Downloads
    *  You will use this json file in the Google Assistant setup page.
4. The last step in Registering your device is to specify "Traits" which we will be skipping.

 
