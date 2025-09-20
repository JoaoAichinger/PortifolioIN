import React, { useState } from 'react';
import './Carousel.css';

function Carousel({ children }) {
  const [currentIndex, setCurrentIndex] = useState(0);

  const getTotalPages = (totalItems, itemsPerPage) => Math.ceil(totalItems / itemsPerPage);
  const itemsPerPage = 3;
  const totalItems = React.Children.count(children);
  //const totalPages = Math.ceil(totalItems / itemsPerPage);
  const totalPages = getTotalPages(totalItems, itemsPerPage); // retorna 4
  console.log(totalPages);

  const nextSlide = () => setCurrentIndex((prev) => (prev + 1) % totalPages);
  const prevSlide = () => setCurrentIndex((prev) => (prev - 1 + totalPages) % totalPages);

  // Pega apenas os itens da página atual
  const startIndex = currentIndex * itemsPerPage;
  const visibleItems = React.Children.toArray(children).slice(
    startIndex,
    startIndex + itemsPerPage
  );

  if (totalItems === 0) {
    return <div className="carousel-empty">Nenhum item para exibir</div>;
  }

  return (
    <div className="carousel">
      <div className="carousel-items">
        {visibleItems}
      </div>

      {totalPages > 1 && (
        <div className="carousel-controls">
          <button className="carousel-btn" onClick={prevSlide}>&#8249;</button>

          <div className="carousel-indicators">
            {Array.from({ length: totalPages }).map((_, index) => (
              <button
                key={index}
                className={`carousel-indicator ${index === currentIndex ? 'active' : ''}`}
                onClick={() => setCurrentIndex(index)}
              />
            ))}
          </div>

          <button className="carousel-btn" onClick={nextSlide}>&#8250;</button>
        </div>
      )}
    </div>
  );
}

export default Carousel;
