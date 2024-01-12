import React, { useState } from 'react';
import axios from 'axios';

const GetQuestion: React.FC = () => {
  const [response, setResponse] = useState('');


  const handleTestFunction = () => {

    axios.post('https://fa-survey-dev-eus2-001.azurewebsites.net/api/campaign_query_function', {campaign_id: 1})
        .then((res) => {
            setResponse(res.data); 
        })
        .catch((error) => {
            setResponse('Error al conectar con la Azure Function');
            console.error('Error al conectar con la Azure Function:', error);
        });
  };
  

  return (
    <div>
      <h1>Página de Prueba de Azure Function</h1>
      <button onClick={handleTestFunction}>Probar conexión con Azure Function</button>
      <div>
        {response && (
          <p>Respuesta de la Azure Function: {response}</p>
        )}
      </div>
    </div>
  );
};

export default GetQuestion;
