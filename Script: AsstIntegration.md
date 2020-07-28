# AsstIntegration Script
This script handles the setup and driver code for projects developed with University 
Maryland's HCI Lab for the purpose of developing prototypes which would aid in user
studies with people living with dementia. 

This script can be divided into 4 main procedures and their respective options.
(e.g. ./AsstIntegration Setup googlesample )

1. Setup
    * googlesample
    * calendar
2. Proto
    * calendar
    * plant
3. GA
    * -e [STILL IN BETA -> OPTIONAL]
4. Virtmic
    * config
    * undo
    * reset
    * play
    

At present, there is no script functionality that requires the script to be called 
with sudo. Due to this, calling the script
with sudo will cause it to automatically exit.

## Prerequisites 
* GCP Model ID
* GCP Project ID
* Microphone and Speaker addresses <CARD#,DEVICE#>
* client-secrets JSON file

### Recommendations
* Save your client-secrets.json file to the Google Drive of the account you will be setting
the prototype up for. This will reduce the amount of accounts you will log in to during
installations.

## Setup

There are 4 setup options available for this script. They handle most
of the bash installation legwork.

##### Google Assistant Sample
###### Start Installation
To setup the Google Assistant sample, run the following code where '/PATH/TO/JSON'
is the path to the client-secrets JSON file you downloaded while setting up your
Raspberry Pi with Google Cloud Platform.

```bash
./AsstIntegration Setup googlesample --client-secrets /PATH/TO/JSON
```

NOTE: If the file path is incorrect, the script will exit and you will be able to
start again.

###### Script Input
You will be prompted to provide the Project and Model ID for your GCP project as 
well as the Card and Device addresses for your microphone and speaker. These can 
be found by typing the following into a different terminal:

For Microphone:
```bash
arecord -l
```
For Speaker:
```bash
aplay -l
```
###### Google Assistant Permissions
Towards the end of the installation, a link will be provided in the terminal. You must
navigate to the link and give permissions to the project. After you accept, you will
be given an confirmation code that you will paste back into the terminal.

NOTE: To paste into the terminal using the keyboard, use 'CTRL+SHIFT+V'

## Prototype Device Use
#### Smart Calendar
The smart calendar procedure automatically triggers the Google Assistant with an
audio input command which asks it to "Add an event to my calendar". To test out
the functionality of this procedure, enter the following command:
```bash
./AsstIntegration Proto calendar
```

#### Plant Sensor
The Plant Sensor procedure begins detecting soil moisture levels and will request
more water if it falls below a certain level.
```bash
./AsstIntegration Proto plant
```

## Google Assistant Sample
The Google Assistant sample can be triggered directly with this scipt using the
'GA' option:
```bash
./AsstIntegration GA
```

!! NOTE: The following feature is currently in development. !!

Using the -e flag will cause the the Google Assistant to be automatically 
triggered and listening for commands. 
```bash
./AsstIntegration GA -e
```

## Virtual Microphone
The virtual microphone was a workaround developed to pipe pre-recorded audio from a file
to the google assistant while making it think was user input. Virtmic should be 
handled by the the googlesample installation, but problems may arise. 

##### Config
Configure the modules and file structure for the Virtual Microphone
```bash
./AsstIntegration Virtmic config
```

##### Undo
Undo any Virtmic-related configuration
```bash
./AsstIntegration Virtmic undo
```

##### Reset
Reset pulseaudio driver and run 'Virtmic undo'
```bash
./AsstIntegration Virtmic reset
```

##### Play
Send "Add event to my calendar" file to virtmic pipe
```bash
./AsstIntegration Virtmic play
```
