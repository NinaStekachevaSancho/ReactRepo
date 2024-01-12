import React, { useState } from 'react';
import Button from '../components/Button';

const Terms: React.FC = () => {
  const [accepted, setAccepted] = useState(false);

  const handleCheckboxChange = () => {
    setAccepted(!accepted);
  };

  const handleNextButtonClick = () => {
    // Aquí podrías realizar alguna acción si el usuario ha aceptado los términos y ha presionado Next
  };

  return (
    <div>
      <h1>Términos y Condiciones</h1>
      <div>
        <label>
          <input
            type="checkbox"
            checked={accepted}
            onChange={handleCheckboxChange}
          />
          Acepto los términos y condiciones
        </label>
      </div>
      <div style={{ marginTop: '20px' }}>
        {accepted && (
          <Button
            link="/gracias"
            text="Next"
            onClick={handleNextButtonClick}
          />
        )}
      </div>
      {/* Otro contenido */}
    </div>
  );
};

export default Terms;
