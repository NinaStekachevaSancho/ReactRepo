import React, { useEffect, useState } from 'react';

const Gracias: React.FC = () => {
  const storedRating = localStorage.getItem('rating');
  const rating = storedRating ? parseInt(storedRating, 10) : 0;
  const [audioURL, setAudioURL] = useState<string | null>(null);

  useEffect(() => {
    const storedAudio = localStorage.getItem('audioBlob');
    if (storedAudio) {
      setAudioURL(storedAudio);
    }
  }, []);
 

  return (
    <div>
      <h1>¡Gracias por contestar nuestra encuesta!</h1>
      <p>Rating guardado: {rating} estrella{rating !== 1 ? 's' : ''}</p>
      {audioURL && (
        <audio controls>
          <source src={audioURL} type="audio/webm" />
          Tu navegador no soporta audio.
        </audio>
      )}
    </div>
  );
};

export default Gracias;
