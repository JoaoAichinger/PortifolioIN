import React, { useEffect, useState } from 'react';
import api from "../services/api";
import "./TagList.css";

function TagList({ selectedTags = [], onTagToggle }) {
  const [tags, setTags] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  

  useEffect(() => {
    async function fetchTags() {
      try {
        setLoading(true);
        const { data } = await api.get("/tag/list");
        setTags(data);
      } catch (error) {
        console.error("Erro ao buscar tags:", error);
        setError("Erro ao carregar tags");
      } finally {
        setLoading(false);
      }
    }
    
    fetchTags();
  }, []);

  function handleTagClick(tagId) {
    if (onTagToggle) {
      onTagToggle(tagId);
    }
  }

  if (loading) {
    return <div className="tagContainer loading">Carregando tags...</div>;
  }

  if (error) {
    return <div className="tagContainer error">{error}</div>;
  }

  return (
    <div className="tagContainer">
      <ul className="tagList">
        {tags.map((tag, index) => {
          const isSelected = selectedTags.includes(tag.id);
          return (
            <li 
              className={`tagEl ${isSelected ? 'selected' : ''}`} 
              key={tag.id}
            >
              <button
                className={`tagBtn ${isSelected ? 'active' : ''}`}
                onClick={() => handleTagClick(tag.id)}
              >
                {tag.name}
                {isSelected && <span className="tag-check">✓</span>}
              </button>
            </li>
          );
        })}
      </ul>
    </div>
  );
}

export default TagList;

