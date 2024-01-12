import React from 'react';
import RatingComponent from './RatingComponent';
interface propstype {
  ratingStars : any;
  question: string;

  
}

const App: React.FC<propstype> = ({ ratingStars, question }) => {
  
  return (
    <div>
      <RatingComponent question={question}/>
    </div>
  );
};

export default App;