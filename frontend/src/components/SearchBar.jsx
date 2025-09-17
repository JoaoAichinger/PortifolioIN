import React, { useState } from "react";
import Button from "./Button";
import "./SearchBar.css";

function SearchBar({ tags, setTags }) {
  const [searchTerm, setSearchTerm] = useState("");

  // 🔧 aqui estava o erro — precisa ser arrow function ou function
  const handleRemoveTag = (tagToRemove) => {
    setTags(tags.filter(tag => tag !== tagToRemove));
  };

  function handleInputChange(e) {
    setSearchTerm(e.target.value);
  }

  function buscar(e) {
    e.preventDefault();
    console.log("Buscando por:", [...tags, searchTerm].join(" "));
  }

  return (
    <div className="container">
      <div className="tags-container">
        <div className="searchBox">
          <input
          type="text"
          placeholder="Digite sua busca..."
          value={searchTerm}
          onChange={handleInputChange}
          />
          <Button name="Buscar" onClick={buscar} />
        </div>
        <div className="tags-list">
          {tags.map(tag => (
          <span className="tag" key={tag}>
            {tag}
            <button
              className="remove-tag"
              onClick={() => handleRemoveTag(tag)}
            >
              x
            </button>
          </span>
        ))}
        </div>
        
      </div>
    </div>
  );
}

export default SearchBar;
