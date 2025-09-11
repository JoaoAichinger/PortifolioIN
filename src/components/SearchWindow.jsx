import { useState } from 'react';
import SearchBar from './SearchBar';
import TagList from './TagList';

function SearchWindow() {
  const [searchTerm, setSearchTerm] = useState('');
  

  return (
    <div>
      <SearchBar searchTerm={searchTerm} setSearchTerm={setSearchTerm} />
      <TagList setSearchTerm={setSearchTerm} />
    </div>
  );
}

export default SearchWindow;
