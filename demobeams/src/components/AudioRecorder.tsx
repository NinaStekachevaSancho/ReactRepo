import React, { useState } from 'react';
import { AudioRecorder } from 'react-audio-voice-recorder';
import "./AudioRecorderComponent.style.css"

const AudioRecorderComponent: React.FC = () => {
  const [audioBlob, setAudioBlob] = useState<Blob | null>(null);

  const saveToVariable = (blob: Blob) => {
    setAudioBlob(blob);
    localStorage.setItem('audioBlob', URL.createObjectURL(blob));
  };

  return (
    <div className="RecorderContainer">
      <AudioRecorder 
        onRecordingComplete={saveToVariable}
        audioTrackConstraints={{
          noiseSuppression: true,
          echoCancellation: true,
        }} 
        downloadOnSavePress={false}
        downloadFileExtension="webm"
      />
      {audioBlob && (
        <audio controls>
          <source src={URL.createObjectURL(audioBlob)} type="audio/webm" />
          Tu navegador no soporta audio.
        </audio>
      )}
    </div>
  );
};

export default AudioRecorderComponent;