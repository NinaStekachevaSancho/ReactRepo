import React, { useState } from 'react';
import { useParams, useSearchParams } from 'react-router-dom'
import RatingComponentProps from '../components/RatingComponentProps'
import Button from '../components/Button'
import { fetchAzureFunctionData } from '../components/fetchFromAzureFunction'


export default function Rating() {

  const {foo} = useParams();
  const [searchParams, setSearchParams] = useSearchParams()
  
  // Obtén el valor del parámetro 'question'
  const question = searchParams.get('question');

  const [response, setResponse] = useState<string | null>(null);

  const handleTestFunction = async () => {
    const extractedPart = await fetchAzureFunctionData();
    console.log('Fetched data',extractedPart)
    setResponse(extractedPart);
  };

  
  
  return (
    <div>
      <> {response} </>
        {question ? (
          
        <>
          <RatingComponentProps ratingStars={undefined} question={question} />
          {response && <p>Respuesta de la Azure Function: {response}</p>}
        </>
      ) : (
        <h1>No question provided</h1>
      )}
      <div className="Button">
      <Button link='/recorder' text="Next" />
      </div>
    </div>
  )
}


