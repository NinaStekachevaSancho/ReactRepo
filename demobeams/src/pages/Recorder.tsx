import React from 'react';
import Button from '../components/Button';
import AudioRecorder from '../components/AudioRecorder';

const RecorderComponent: React.FC = () => {
  return (
    <div>
      <h1>Añade tu opinión</h1>
      <div className='RecorderButtonsContainer'>
        <AudioRecorder />
      </div>
      <Button link="/terms" text="Next" />
    </div>
  );
};

export default RecorderComponent;
