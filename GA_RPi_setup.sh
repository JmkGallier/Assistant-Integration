#!/bin/bash


declare -A SCRIPT_STATE_OPTIONS
SCRIPT_STATE_OPTIONS=(
  ["none"]=1
  ["plant_sensor"]=1
  ["calendar"]=1
  ["pillbox"]=1
  ["setup"]=1
)

#### Option Input
while [ -n "${1-}" ]; do
  case "$1" in
  -s) CURRENT_SCRIPT_STATE="$2"
    if [[ ${SCRIPT_STATE_OPTIONS[$CURRENT_SCRIPT_STATE]} ]]; then :
    else
      echo "${CURRENT_SCRIPT_STATE} is not a valid option"
      CURRENT_SCRIPT_STATE="none"
    fi
    ;;
  -mic) MIC_test="$2"
    if [[ "$MIC_test" =~ .*",".* ]]; then
      MIC_address="${MIC_test}"
      echo "MICROPHONE SET TO: $MIC_address"
    fi
    ;;
  -speaker) SPEAKER_test="$2"
    if [[ "$SPEAKER_test" =~ .*",".* ]]; then
      SPEAKER_address="${SPEAKER_test}"
      echo "SPEAKER SET TO: $SPEAKER_address"
    fi
    ;;
  --client-secret) CLIENT_SECRET_PATH="$2"
    echo "${CLIENT_SECRET_PATH}"
  ;;
  --) shift ; break ;;
  esac
  shift
done


# Script needs restriction for SUDO users
install_GA_DEP() {
  sudo apt -qq update
  sudo apt -qq install portaudio19-dev libffi-dev libssl-dev python3-dev python3-venv python-serial python3-serial -y
}

install_GA() {
  python3 -m venv env
  env/bin/python3 -m pip install --upgrade pip setuptools wheel
  source env/bin/activate
  python3 -m pip install --upgrade google-assistant-sdk[samples] google-auth-oauthlib[tool]
  google-oauthlib-tool --scope https://www.googleapis.com/auth/assistant-sdk-prototype --save --headless --client-secrets "${CLIENT_SECRET_PATH}"
}

config_Speaker() {
  rm -rf ~/.asoundrc
  touch ~/.asoundrc
  echo "pcm.!default {
    type asym
    capture.pcm 'mic'
    playback.pcm 'speaker'
    }
  pcm.mic {
    type plug
    slave {
      pcm 'hw:${MIC_address}'
    }
  }
  pcm.speaker {
    type plug
    slave {
      pcm 'hw:${SPEAKER_address}'
    }
  }" >> ~/.asoundrc
  amixer set Master 70%
}

start_Plant() {
  pythpn3 /home/pi/Assistant-Integration/Plant\ Sensor/plantSense_rpi_main.py
}

start_Calendar() {
  source /home/pi/Assistant-Integration/env/bin/activate
  python3 /home/pi/Assistant-Integration/Press-sense\ Calendar/velo_detect.py
}

script_Main() {
  while [ "${CURRENT_SCRIPT_STATE}" != "none" ]; do
    case $USER_IS_ROOT in
    true)
      echo "Script should not be run as 'root' user"
      echo "Exiting script"
      CURRENT_SCRIPT_STATE=none
      ;;
    false)
      case $CURRENT_SCRIPT_STATE in
      plant_sensor)
        echo "Script State: Plant Sensor"
        CURRENT_SCRIPT_STATE="none"
        ;;
      calendar)
        echo "Script State: Calendar"
        CURRENT_SCRIPT_STATE="none"
        ;;
      setup)
        echo "Script State: Setup"
        install_GA_DEP
        install_GA
        config_Speaker
        CURRENT_SCRIPT_STATE="none"
        ;;
      *)
        echo "Invalid Script State: ${CURRENT_SCRIPT_STATE}"
        CURRENT_SCRIPT_STATE="none"
        ;;
      esac
      ;;
    esac
  done
}
