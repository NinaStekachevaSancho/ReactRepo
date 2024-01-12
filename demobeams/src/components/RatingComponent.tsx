import React, { useEffect, useState } from 'react';
import "./RatingComponent.style.css"

interface RatingComponentProps {
  question: string;
}

  const RatingComponent: React.FC<RatingComponentProps> = ({question}) => {
    const [rating, setRating] = useState<number>(0);
    const [hoverRating, setHoverRating] = useState<number>(0);
    const storedRating = localStorage.getItem('rating');
    
    const handleRatingClick = (stars: number): void => {
      if (stars >= 0 && stars <= 5) {
        setRating(stars);
        localStorage.setItem('rating', stars.toString());
      }
    };
    
    useEffect(() => {
      const storedRating = localStorage.getItem('rating');
      if (storedRating) {
        setRating(parseInt(storedRating, 10));
      }
    }, []);
  
    const handleMouseEnter = (stars: number): void => {
      setHoverRating(stars);
    };
  
    const handleMouseLeave = (): void => {
      setHoverRating(0);
    };
  
    return (
      <div className='RatingComponent'>
        <h2>{question}</h2>
        {[...Array(5)].map((_, index) => {
          const starValue = index + 1;
          return (
            <span
              key={index}
              onMouseEnter={() => handleMouseEnter(starValue)}
              onMouseLeave={() => handleMouseLeave()}
              onClick={() => handleRatingClick(starValue)}
              style={{
                color: starValue <= (hoverRating > 0 ? hoverRating : rating) ? '#ff9900' : 'white',
                cursor: 'pointer',
              }}
            >
              ★
            </span>
          );
        })}
        {rating > 0 && <p>Rating: {rating} star{rating !== 1 ? 's' : ''}</p>}
      </div>
    );
  };
  
  export default RatingComponent;
  