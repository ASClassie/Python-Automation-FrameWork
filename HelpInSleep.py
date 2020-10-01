from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import time

volume_value = 1
sessions = AudioUtilities.GetAllSessions()
while True:
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process and session.Process.name() == 'chrome.exe':
            print(volume.GetMasterVolume())
            volume.SetMasterVolume(volume_value, None)

    time.sleep(2)
    volume_value -= 0.1

    if volume_value <0:
        print('Music Over Sleeping Successful')
        break


