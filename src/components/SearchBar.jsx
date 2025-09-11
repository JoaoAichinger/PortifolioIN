import Button from "./Button";
import "./SearchBar.css";

function SearchBar({ searchTerm, setSearchTerm }) {

  function handleInputChange(e) {
    setSearchTerm(e.target.value);
  }

  function buscar(e) {
    e.preventDefault();
    console.log("Buscando por:", searchTerm);
  }

  return (
    <div className="container">
      <input
        type="text"
        placeholder="Digite sua busca..."
        value={searchTerm}
        onChange={handleInputChange}
      />
      <Button name="Buscar" onClick={buscar} />
    </div>
  );
}

export default SearchBar;
