import React, { useState } from 'react';

const ConnectionComponent: React.FC = () => {
  const [rating, setRating] = useState<number>(0);
  const [audioBlob, setAudioBlob] = useState<Blob | null>(null);
  const campaign_id = 11;

  const enviarDatos = async () => {
    if (!audioBlob || rating === 0) {
      console.error('El audio o el rating están vacíos');
      return;
    }

    const data = {
      audio: audioBlob,
      rating: rating,
      campaign_id: campaign_id,
    };

    try {
      const response = await fetch('https://fa-survey-dev-eus2-001.azurewebsites.net/api/VoiceInsightProcessor?', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });

      if (response.ok) {
        console.log('Datos enviados correctamente a la Azure Function');
      } else {
        console.error('Error al enviar los datos a la Azure Function');
      }
    } catch (error) {
      console.error('Error de red:', error);
    }
  };

  return (
    <div>
      <button onClick={enviarDatos}>Enviar datos</button>
    </div>
  );
};

export default ConnectionComponent;
