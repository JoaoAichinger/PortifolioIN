import tags from "../data/tags.json";
import "./TagList.css";

function TagList({ setSearchTerm }) {

  const coloring = ['red', 'blue', 'pink', 'green'];

  function handleTagClick(name) {
    setSearchTerm(name);
  }

  return (
    <div className="tagContainer">
      <ul className="tagList">
        {tags.map((tag) => (
          <li className="tagEl" key={tag.id}>
            <button
              className="tagBtn"
              onClick={() => handleTagClick(tag.name)}
            >
              {tag.name}
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TagList;
