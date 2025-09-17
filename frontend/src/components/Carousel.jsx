import React, { useState } from 'react';
import './Carousel.css';

function Carousel({ children }) {
  const [currentIndex, setCurrentIndex] = useState(0);
  
  // Dividir os itens em grupos de 3 para exibir 3 por vez
  const itemsPerPage = 3;
  const totalItems = React.Children.count(children);
  const totalPages = Math.ceil(totalItems / itemsPerPage);
  
  const nextSlide = () => {
    setCurrentIndex((prevIndex) => 
      prevIndex === totalPages - 1 ? 0 : prevIndex + 1
    );
  };
  
  const prevSlide = () => {
    setCurrentIndex((prevIndex) => 
      prevIndex === 0 ? totalPages - 1 : prevIndex - 1
    );
  };
  
  const goToSlide = (index) => {
    setCurrentIndex(index);
  };
  
  // Dividir os filhos em páginas
  const pages = [];
  for (let i = 0; i < totalItems; i += itemsPerPage) {
    pages.push(React.Children.toArray(children).slice(i, i + itemsPerPage));
  }
  
  if (totalItems === 0) {
    return <div className="carousel-empty">Nenhum item para exibir</div>;
  }
  
  return (
    <div className="carousel">
      <div className="carousel-container">
        {/* Botão anterior */}
        {totalPages > 1 && (
          <button 
            className="carousel-btn carousel-btn-prev" 
            onClick={prevSlide}
            aria-label="Slide anterior"
          >
            &#8249;
          </button>
        )}
        
        {/* Conteúdo do carrossel */}
        <div className="carousel-content">
          <div 
            className="carousel-track"
            style={{ 
              transform: `translateX(-${currentIndex * 100}%)`,
              width: `${totalPages * 100}%`
            }}
          >
            {pages.map((page, pageIndex) => (
              <div 
                key={pageIndex} 
                className="carousel-page"
                style={{ width: `${100 / totalPages}%` }}
              >
                <div className="carousel-items">
                  {page}
                </div>
              </div>
            ))}
          </div>
        </div>
        
        {/* Botão próximo */}
        {totalPages > 1 && (
          <button 
            className="carousel-btn carousel-btn-next" 
            onClick={nextSlide}
            aria-label="Próximo slide"
          >
            &#8250;
          </button>
        )}
      </div>
      
      {/* Indicadores */}
      {totalPages > 1 && (
        <div className="carousel-indicators">
          {Array.from({ length: totalPages }).map((_, index) => (
            <button
              key={index}
              className={`carousel-indicator ${index === currentIndex ? 'active' : ''}`}
              onClick={() => goToSlide(index)}
              aria-label={`Ir para slide ${index + 1}`}
            />
          ))}
        </div>
      )}
    </div>
  );
}

export default Carousel;

