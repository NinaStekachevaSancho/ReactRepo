import React, { ReactNode } from 'react';
import { Link } from 'react-router-dom';
import './Button.style.css';

interface ButtonLinkProps {
  link?: string;
  text: ReactNode;
  onClick?: () => void;
}

function Button(props: ButtonLinkProps) {
  const { link, text, onClick } = props;

  if (link) {
    return (
      <Link to={link} className='Button'>
        {text}
      </Link>
    );
  }

  return (
    <div className='Button' onClick={onClick}>
      {text}
    </div>
  );
}

export default Button;
