import { useState } from 'react';
import SearchBar from './SearchBar';
import TagList from './TagList';
import './SearchWindow.css';

function SearchWindow(props) {
  const [tags, setTags] = useState([]);

  function handleAddTag(tag){
    if (!tags.includes(tag)){
      setTags([...tags, tag]);
    }
  }

  function handleRemoveag(tag){
    setTags(tags.filter(t => t !== tag));
  }
  

  return (
    <div className={props.className}>
      <h1 className='title'>O que sua mente está procurando? 
Nós te ajudamos a encontrar:</h1>
      <SearchBar 
        tags={tags} 
        setTags={setTags} 
      />
      <TagList 
        addTag={handleAddTag}  
      />
    </div>
  );
}

export default SearchWindow;
