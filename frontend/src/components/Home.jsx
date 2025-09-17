import { useState } from 'react'
import SearchWindow from './SearchWindow'
import MyHeader from './MyHeader'
import Introduction from './Introduction'
import MyFooter from './MyFooter'
import AlunoList from './AlunoList'
import Carousel from './Carousel'

function Home() {
  const [selectedTags, setSelectedTags] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");

  function handleSearchChange(term) {
    setSearchTerm(term);
  }

  function handleTagsChange(tags) {
    setSelectedTags(tags);
  }

  return (
    <>
      <MyHeader />
      <Introduction className="intro" />
      <SearchWindow 
        className="searchContainer"
        onSearchChange={handleSearchChange}
        onTagsChange={handleTagsChange}
      />
      
      <div className="students-section">
        <h2 className="section-title">Estudantes e Projetos</h2>
        <AlunoList 
          selectedTags={selectedTags}
          searchTerm={searchTerm}
        />
      </div>
      
      <MyFooter />
    </>
  );
}

export default Home;

