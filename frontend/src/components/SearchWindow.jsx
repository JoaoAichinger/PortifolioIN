import { useState } from 'react';
import SearchBar from './SearchBar';
import TagList from './TagList';
import './SearchWindow.css';

function SearchWindow({ onSearchChange, onTagsChange }) {
  const [selectedTags, setSelectedTags] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");

  function handleTagToggle(tagId) {
    let newSelectedTags;
    if (selectedTags.includes(tagId)) {
      // Remover tag se já estiver selecionada
      newSelectedTags = selectedTags.filter(id => id !== tagId);
    } else {
      // Adicionar tag se não estiver selecionada
      newSelectedTags = [...selectedTags, tagId];
    }
    
    setSelectedTags(newSelectedTags);
    
    // Notificar o componente pai sobre a mudança
    if (onTagsChange) {
      onTagsChange(newSelectedTags);
    }
  }

  function handleSearchChange(term) {
    setSearchTerm(term);
    
    // Notificar o componente pai sobre a mudança
    if (onSearchChange) {
      onSearchChange(term);
    }
  }

  return (
    <div className="search-window">
      <h1 className='title'>
        O que sua mente está procurando? 
        <br />
        Nós te ajudamos a encontrar:
      </h1>
      
      <SearchBar 
        searchTerm={searchTerm}
        selectedTags={selectedTags}
        onSearchChange={handleSearchChange}
        onTagRemove={handleTagToggle}
      />
      
      <TagList 
        selectedTags={selectedTags}
        onTagToggle={handleTagToggle}
      />
    </div>
  );
}

export default SearchWindow;

