#!/bin/bash

MIC_CARD=${1}
MIC_DEVICE=${2}
SOUND_CARD=${3}
SOUND_DEVICE=${4}
CLIENT_SECRET=${5}

install_GA_DEP() {
  apt -qq update
  apt -qq install portaudio19-dev libffi-dev libssl-dev python3-dev python3-venv -y
}

install_GA() {
  python3 -m venv env
  env/bin/python3 -m pip install --upgrade pip setuptools wheel
  source env/bin/activate
  python3 -m pip install --upgrade google-assistant-sdk[samples]
  python3 -m pip install --upgrade google-auth-oauthlib[tool]
  google-oauthlib-tool --scope https://www.googleapis.com/auth/assistant-sdk-prototype --save --headless --client-secrets "${CLIENT_SECRET}"
}

update_asoundrc() {
  cat "pcm.!default {
  type asym
  capture.pcm 'mic'
  playback.pcm 'speaker'
  }
  pcm.mic {
    type plug
    slave {
      pcm 'hw:${MIC_CARD},${MIC_DEVICE}'
    }
  }
  pcm.speaker {
    type plug
    slave {
      pcm 'hw:${SOUND_CARD},${SOUND_DEVICE}'
      rate 16000
    }
  }" >>/home/pi/.asoundrc
}


echo "${MIC_CARD}"