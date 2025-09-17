import React, { useState, useEffect } from "react";
import api from "../services/api";
import Button from "./Button";
import "./SearchBar.css";

function SearchBar({ searchTerm = "", selectedTags = [], onSearchChange, onTagRemove }) {
  const [inputValue, setInputValue] = useState(searchTerm);
  const [tags, setTags] = useState([]);

  // Buscar informações das tags selecionadas
  useEffect(() => {
    async function fetchTagsInfo() {
      if (selectedTags.length > 0) {
        try {
          const { data } = await api.get("/tag/list");
          const selectedTagsInfo = data.filter(tag => selectedTags.includes(tag.id));
          setTags(selectedTagsInfo);
        } catch (error) {
          console.error("Erro ao buscar informações das tags:", error);
        }
      } else {
        setTags([]);
      }
    }
    
    fetchTagsInfo();
  }, [selectedTags]);

  function handleInputChange(e) {
    const value = e.target.value;
    setInputValue(value);
    
    // Notificar mudança em tempo real (debounce seria ideal aqui)
    if (onSearchChange) {
      onSearchChange(value);
    }
  }

  function handleRemoveTag(tagId) {
    if (onTagRemove) {
      onTagRemove(tagId);
    }
  }

  function handleSearch(e) {
    e.preventDefault();
    if (onSearchChange) {
      onSearchChange(inputValue);
    }
  }

  return (
    <div className="container">
      <div className="tags-container">
        <div className="searchBox">
          <input
            type="text"
            placeholder="Digite sua busca..."
            value={inputValue}
            onChange={handleInputChange}
          />
          <Button name="Buscar" onClick={handleSearch} />
        </div>
        
        {tags.length > 0 && (
          <div className="tags-list">
            {tags.map(tag => (
              <span className="tag" key={tag.id}>
                {tag.name}
                <button
                  className="remove-tag"
                  onClick={() => handleRemoveTag(tag.id)}
                  aria-label={`Remover tag ${tag.name}`}
                >
                  ×
                </button>
              </span>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default SearchBar;

