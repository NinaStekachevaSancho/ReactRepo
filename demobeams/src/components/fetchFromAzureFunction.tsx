// components/fetchFromAzureFunction.tsx

import axios from 'axios';

export const fetchAzureFunctionData = async (): Promise<string | null> => {
  try {
    const requestData = {
      campaign_id: 1
    };

    const res = await axios.post('https://fa-survey-dev-eus2-001.azurewebsites.net/api/campaign_query_function', requestData);
    const fullResponse = res.data;
    const colonIndex = fullResponse.indexOf(':');

    if (colonIndex !== -1) {
      const extractedPart = fullResponse.substring(colonIndex + 2);
      return extractedPart;
    } else {
      return 'Formato de respuesta inesperado';
    }
  } catch (error) {
    console.error('Error al conectar con la Azure Function:', error);
    return 'Error al conectar con la Azure Function';
  }
};




